#!/usr/bin/env python3
"""Fetch active multiple sclerosis (MS) clinical trials from ClinicalTrials.gov and
write the tracker files in trials/.

Usage (from the repo root):
    python tools/fetch_trials.py                 # fetch, verify, write trials/*.md
    python tools/fetch_trials.py --date 11/03/2026
    python tools/fetch_trials.py --no-verify     # skip the per-trial re-fetch (faster, not for PRs)
    python tools/fetch_trials.py --dump trials.json   # also save the filtered records

Only the Python standard library is used. Every field written to the tables comes from the
ClinicalTrials.gov API v2 response. The only hand-written text is in tools/trial_categories.json:
which lab question a trial is filed under, and one plain line on what it could help answer.
Trials that are not in that file go to "Other" and are marked "not yet reviewed".

API text is treated as data. Nothing in it is followed as an instruction.
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://clinicaltrials.gov/api/v2/studies"
STATUSES = ["RECRUITING", "ACTIVE_NOT_RECRUITING", "NOT_YET_RECRUITING", "ENROLLING_BY_INVITATION"]
QUERY = {
    "query.cond": "multiple sclerosis",
    "filter.overallStatus": ",".join(STATUSES),
    "aggFilters": "studyType:int",
    "pageSize": "1000",
    "countTotal": "true",
}
MAIN_PHASES = [["PHASE2"], ["PHASE3"], ["PHASE2", "PHASE3"]]
EARLY_PHASE_TAGS = {"EARLY_PHASE1", "PHASE1"}  # includes Phase 1/2

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(ROOT, "trials")
CATEGORY_FILE = os.path.join(HERE, "trial_categories.json")

# The search engine expands "multiple sclerosis" to other "sclerosis" conditions (ALS,
# systemic sclerosis, tuberous sclerosis). Keep a study only if MS is named in its conditions,
# keywords or titles.
MS_RE = re.compile(
    r"multiple sclerosis|multiple-sclerosis|\b(?:RR|SP|PP|R|P|C|A)?MS\b|clinically isolated syndrome|"
    r"radiologically isolated syndrome",
    re.I,
)
NOT_MS_RE = re.compile(r"\bMSA\b|multiple system atrophy", re.I)

# Phase 1 and Phase 1/2 studies are kept only for cell therapies and EBV-directed therapies.
CELL_RE = re.compile(
    r"\bCAR[- ]?T\b|\bCAR\b|chimeric antigen receptor|autoleucel|cabtagene|leucel|\bcel\b|"
    r"stem cell|mesenchymal|stromal cell|\bMSCs?\b|h(?:a)?ematopoietic|\bA?HSCT\b|transplant|"
    r"T[- ]cells?\b|\bTregs?\b|regulatory T|\bNK\b|natural killer|cell injection|cell therapy|"
    r"cellular therapy|\bCTLs?\b|STAR-T|UCAR",
    re.I,
)
# The brief summary is checked only for phrases that clearly mean the study product is a cell therapy.
SUMMARY_CELL_RE = re.compile(
    r"chimeric antigen receptor|\bCAR[- ]?T\b|cell therapy|cellular therapy|cellular (?:pharmaco)?kinetics",
    re.I,
)
EBV_RE = re.compile(r"\bEBV\b|epstein[- ]barr", re.I)
NOT_CELL_RE = re.compile(r"extracellular vesicle|\bsEV\b|exosome", re.I)

SECTIONS = [
    ("A", "A. Epstein-Barr virus (EBV) prevention or control (issue #2)"),
    ("B", "B. Worsening without relapses, PIRA and progressive MS (issue #3)"),
    ("C", "C. Myelin repair and neuroprotection (issue #4)"),
    ("D", "D. Stem cell transplant (aHSCT) and CAR-T cell therapy (issue #5)"),
    ("E", "E. Biomarker-guided treatment (issue #6)"),
    ("F", "F. Why MS clusters in families and places"),
    ("APPROVED", "Approved-drug and other studies"),
    ("OTHER", "Other"),
]
OTHER_LIMIT = 25

STATUS_WORDS = {
    "RECRUITING": "Recruiting",
    "ACTIVE_NOT_RECRUITING": "Active, not recruiting",
    "NOT_YET_RECRUITING": "Not yet recruiting",
    "ENROLLING_BY_INVITATION": "Enrolling by invitation",
}
PHASE_WORDS = {"EARLY_PHASE1": "Early 1", "PHASE1": "1", "PHASE2": "2", "PHASE3": "3", "PHASE4": "4", "NA": "N/A"}


def get_json(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "cure-ms-trial-tracker"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception:  # network hiccup: back off and retry
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))

    return None


def fetch_all():
    studies, token, total = [], None, None
    while True:
        q = dict(QUERY)
        if token:
            q["pageToken"] = token
        data = get_json(API + "?" + urllib.parse.urlencode(q))
        total = data.get("totalCount", total)
        studies.extend(data.get("studies", []))
        token = data.get("nextPageToken")
        if not token:
            break
    return studies, total


def g(d, *path, default=None):
    for p in path:
        if not isinstance(d, dict):
            return default
        d = d.get(p)
        if d is None:
            return default
    return d


def record(study):
    p = study.get("protocolSection", {})
    ivs = g(p, "armsInterventionsModule", "interventions", default=[]) or []
    return {
        "nct": g(p, "identificationModule", "nctId"),
        "title": g(p, "identificationModule", "briefTitle", default=""),
        "official_title": g(p, "identificationModule", "officialTitle", default=""),
        "acronym": g(p, "identificationModule", "acronym", default=""),
        "status": g(p, "statusModule", "overallStatus", default=""),
        "phases": g(p, "designModule", "phases", default=[]) or [],
        "study_type": g(p, "designModule", "studyType", default=""),
        "enrollment": g(p, "designModule", "enrollmentInfo", "count"),
        "enrollment_type": g(p, "designModule", "enrollmentInfo", "type", default=""),
        "pcd": g(p, "statusModule", "primaryCompletionDateStruct", "date", default=""),
        "pcd_type": g(p, "statusModule", "primaryCompletionDateStruct", "type", default=""),
        "sponsor": g(p, "sponsorCollaboratorsModule", "leadSponsor", "name", default=""),
        "conditions": g(p, "conditionsModule", "conditions", default=[]) or [],
        "keywords": g(p, "conditionsModule", "keywords", default=[]) or [],
        "interventions": [
            {"type": i.get("type", ""), "name": i.get("name", ""), "description": i.get("description", "")}
            for i in ivs
        ],
        "primary_outcomes": [o.get("measure", "") for o in g(p, "outcomesModule", "primaryOutcomes", default=[]) or []],
        "summary": g(p, "descriptionModule", "briefSummary", default=""),
    }


def is_ms(r):
    text = " | ".join(r["conditions"] + r["keywords"] + [r["title"], r["official_title"]])
    text = NOT_MS_RE.sub("", text)
    return bool(MS_RE.search(text))


def is_cell(r):
    texts = [r["title"], r["official_title"]] + [i["name"] + " " + i["description"] for i in r["interventions"]]
    t = " | ".join(texts)
    return bool(CELL_RE.search(t) or SUMMARY_CELL_RE.search(r["summary"])) and not NOT_CELL_RE.search(" ".join(i["name"] for i in r["interventions"]))


def is_ebv(r):
    t = " | ".join([r["title"], r["official_title"]] + [i["name"] + " " + i["description"] for i in r["interventions"]])
    return bool(EBV_RE.search(t))


def keep(r, cats=None):
    if cats and cats.get(r["nct"], {}).get("exclude"):
        return False, "excluded by review"
    if r["study_type"] != "INTERVENTIONAL" or r["status"] not in STATUSES:
        return False, "type/status"
    if not is_ms(r):
        return False, "not MS"
    if r["phases"] in MAIN_PHASES:
        return True, "phase 2/3"
    if set(r["phases"]) & EARLY_PHASE_TAGS and (is_cell(r) or is_ebv(r)):
        return True, "phase 1 cell/EBV"
    return False, "phase"


def verify(r):
    """Re-fetch one study by NCT ID and compare the fields we publish."""
    d = get_json(f"{API}/{r['nct']}")
    v = record(d)
    fields = ["nct", "title", "status", "phases", "pcd", "sponsor", "enrollment"]
    diffs = [f for f in fields if v[f] != r[f]]
    return diffs, v


def phase_text(phases):
    return "/".join(PHASE_WORDS.get(p, p) for p in phases) or "N/A"


def md(s):
    return (s or "").replace("|", "/").replace("\n", " ").strip()


def short_title(r):
    t = r["title"]
    if r["acronym"] and r["acronym"].lower() not in t.lower():
        t = f"{r['acronym']}: {t}"
    return md(t)


def intervention_text(r, limit=3):
    names, seen = [], set()
    for i in r["interventions"]:
        n = md(i["name"])
        if re.fullmatch(r"(?i)placebo.*|matching placebo.*", n) or n.lower() in seen:
            continue
        seen.add(n.lower())
        names.append(n)
    if len(names) > limit:
        names = names[:limit] + [f"+{len(names) - limit} more"]
    has_placebo = any(re.match(r"(?i)(matching )?placebo", i["name"]) for i in r["interventions"])
    return "; ".join(names) + ("; placebo" if has_placebo else "")


def enrollment_text(r):
    if r["enrollment"] is None:
        return "n/a"
    suffix = " (est.)" if r["enrollment_type"] == "ESTIMATED" else ""
    return f"{r['enrollment']}{suffix}"


def date_key(s):
    parts = (s or "").split("-")
    if len(parts) == 2:
        parts.append("28")  # month-only date: treat as end of month for sorting
    try:
        return dt.date(int(parts[0]), int(parts[1]), int(parts[2]))
    except Exception:
        return dt.date(9999, 12, 31)


def us_date(s):
    parts = (s or "").split("-")
    if len(parts) == 3:
        return f"{parts[1]}/{parts[2]}/{parts[0]}"
    if len(parts) == 2:
        return f"{parts[1]}/{parts[0]}"
    return s or "n/a"


def pcd_text(r):
    t = us_date(r["pcd"])
    return t + (" (est.)" if r["pcd_type"] == "ESTIMATED" else "")


def row(r, note):
    return (
        f"| [{r['nct']}](https://clinicaltrials.gov/study/{r['nct']}) | {short_title(r)} | {intervention_text(r)} | "
        f"{phase_text(r['phases'])} | {STATUS_WORDS.get(r['status'], r['status'])} | {enrollment_text(r)} | "
        f"{pcd_text(r)} | {md(r['sponsor'])} | {md(note)} |"
    )


HEADER = (
    "| NCT ID | Short title | Intervention | Phase | Status | Enrollment | Primary completion | Sponsor | What it could help answer |\n"
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"
)


def write_tables(kept, cats, run_date, total, counts, unverified, notes, excluded):
    by = {k: [] for k, _ in SECTIONS}
    for r in kept:
        c = cats.get(r["nct"], {})
        by[c.get("q", "OTHER")].append((r, c.get("note", "Not yet reviewed; filed here by default."), c.get("rank", 99)))
    for k in by:
        by[k].sort(key=lambda x: (x[2], date_key(x[0]["pcd"])) if k == "OTHER" else (date_key(x[0]["pcd"]), x[0]["nct"]))

    out = []
    out.append("# Active MS clinical trials, by lab question\n")
    out.append(
        f"Run on {run_date} from the [ClinicalTrials.gov API v2](https://clinicaltrials.gov/data-api/api). "
        "See [README.md](README.md) for the exact query and how to refresh it.\n"
    )
    out.append(
        "**This is not medical advice.** These tables list what trials are testing. They do not say "
        "that any treatment works, and they are not a guide to joining a trial. Talk to your own "
        "clinicians about any trial.\n"
    )
    out.append(
        f"The query returned {total} interventional studies; {counts['kept']} passed the filters and review "
        f"({counts['main']} phase 2, 3 or 2/3 and {counts['early']} phase 1 or 1/2 cell or EBV-directed therapies). "
        "A trial is filed under a question only when its intervention or main outcome clearly fits it. "
        "Each trial appears once. Dates are MM/DD/YYYY or MM/YYYY; \"est.\" means the registry lists the "
        "date or enrollment as an estimate.\n"
    )
    out.append("| Section | Trials |\n| --- | --- |")
    for k, name in SECTIONS:
        n = len(by[k])
        out.append(f"| [{name}](#{anchor(name)}) | {n} |")
    out.append("")
    for k, name in SECTIONS:
        rows = by[k]
        out.append(f"## {name}\n")
        if notes.get(k):  # hand-written section notes from tools/trial_categories.json
            out.append(notes[k] + "\n")
            if not rows:
                continue
        if not rows:
            out.append("None in this run.\n")
            continue
        shown = rows
        if k == "OTHER" and len(rows) > OTHER_LIMIT:
            shown = rows[:OTHER_LIMIT]
            out.append(
                f"Showing the {OTHER_LIMIT} most relevant of {len(rows)} trials (new drugs and treatment "
                f"approaches first, ordered by the rank in `tools/trial_categories.json`). "
                f"{len(rows) - OTHER_LIMIT} were left out; their NCT IDs are listed below the table.\n"
            )
        out.append(HEADER)
        for r, note, _ in shown:
            out.append(row(r, note))
        out.append("")
        if k == "OTHER" and len(rows) > OTHER_LIMIT:
            left = ", ".join(f"[{r['nct']}](https://clinicaltrials.gov/study/{r['nct']})" for r, _, _ in rows[OTHER_LIMIT:])
            out.append(f"Left out of the table: {left}.\n")
    if excluded:
        out.append("## Left out after review\n")
        out.append(
            "These passed the automatic filters but were removed by hand (reasons in "
            "`tools/trial_categories.json`): "
            + "; ".join(
                f"[{n}](https://clinicaltrials.gov/study/{n}), {md(cats.get(n, {}).get('reason', ''))}" for n in excluded
            )
            + ".\n"
        )
    if unverified:
        out.append("## Not confirmed\n")
        out.append("These could not be confirmed by a separate fetch of the study record: " + ", ".join(unverified) + ".\n")
    return "\n".join(out), by


def anchor(name):
    a = name.lower()
    a = re.sub(r"[^a-z0-9 \-]", "", a)
    return a.replace(" ", "-")


def write_readouts(kept, cats, run_date, start, end):
    names = dict(SECTIONS)
    sel = [r for r in kept if start <= date_key(r["pcd"]) <= end]
    sel.sort(key=lambda r: (date_key(r["pcd"]), r["nct"]))
    out = ["# Upcoming primary completion dates\n"]
    out.append(
        f"Trials from [active-trials.md](active-trials.md) whose primary completion date falls between "
        f"{start.strftime('%m/%Y')} and {end.strftime('%m/%Y')}, soonest first. Run on {run_date}.\n"
    )
    out.append(
        "**This is not medical advice.** The primary completion date is when the last participant is "
        "measured for the main outcome. Results are often published months or years later, and the "
        "sponsor can change the date. Most of these dates are estimates.\n"
    )
    out.append(f"{len(sel)} trials.\n")
    out.append(
        "| Primary completion | NCT ID | Short title | Intervention | Phase | Status | Enrollment | Sponsor | Lab question |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"
    )
    for r in sel:
        q = cats.get(r["nct"], {}).get("q", "OTHER")
        label = q if q in "ABCDEF" else ("Approved-drug and other" if q == "APPROVED" else "Other")
        out.append(
            f"| {pcd_text(r)} | [{r['nct']}](https://clinicaltrials.gov/study/{r['nct']}) | {short_title(r)} | "
            f"{intervention_text(r)} | {phase_text(r['phases'])} | {STATUS_WORDS.get(r['status'], r['status'])} | "
            f"{enrollment_text(r)} | {md(r['sponsor'])} | {label} |"
        )
    out.append("")
    return "\n".join(out), len(sel)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=dt.date.today().strftime("%m/%d/%Y"), help="run date, MM/DD/YYYY")
    ap.add_argument("--no-verify", action="store_true")
    ap.add_argument("--dump", help="write filtered records to this JSON file")
    ap.add_argument("--readout-start", default=None, help="YYYY-MM, default: month of --date")
    ap.add_argument("--readout-end", default=None, help="YYYY-MM, default: December of the following year")
    a = ap.parse_args()

    run = dt.datetime.strptime(a.date, "%m/%d/%Y").date()
    rs = a.readout_start or run.strftime("%Y-%m")
    re_ = a.readout_end or f"{run.year + 1}-12"
    start = dt.date(int(rs[:4]), int(rs[5:7]), 1)
    ey, em = int(re_[:4]), int(re_[5:7])
    end = (dt.date(ey + (em == 12), em % 12 + 1, 1) - dt.timedelta(days=1))

    studies, total = fetch_all()
    recs = [record(s) for s in studies]
    cats, notes = {}, {}
    if os.path.exists(CATEGORY_FILE):
        with open(CATEGORY_FILE, encoding="utf-8") as f:
            raw = json.load(f)
        notes = raw.get("_section_notes", {})
        cats = {k: v for k, v in raw.items() if not k.startswith("_")}

    kept, reasons, excluded, excluded_recs = [], {}, [], []
    for r in recs:
        ok, why = keep(r, cats)
        if why == "excluded by review":
            excluded.append(r["nct"])
            excluded_recs.append(r)
        reasons[why] = reasons.get(why, 0) + 1
        if ok:
            kept.append(r)
    counts = {
        "kept": len(kept),
        "main": sum(1 for r in kept if r["phases"] in MAIN_PHASES),
        "early": sum(1 for r in kept if r["phases"] not in MAIN_PHASES),
    }
    print(f"API total {total}, fetched {len(recs)}, kept {len(kept)}; reasons {reasons}", file=sys.stderr)

    unverified = []
    if not a.no_verify:
        for r in kept + excluded_recs:  # also confirm studies named in "Left out after review"
            try:
                diffs, v = verify(r)
            except Exception as e:
                unverified.append(f"{r['nct']} (fetch failed: {e})")
                continue
            if diffs:
                unverified.append(f"{r['nct']} (fields differ: {', '.join(diffs)})")
            time.sleep(0.2)
        n_checked = len(kept) + len(excluded_recs)
        print(f"verified {n_checked - len(unverified)}/{n_checked} by individual re-fetch", file=sys.stderr)
        for u in unverified:
            print("  NOT CONFIRMED:", u, file=sys.stderr)

    missing = [r["nct"] for r in kept if r["nct"] not in cats]
    stale = [k for k in cats if k not in {r["nct"] for r in kept} and k not in excluded]
    if missing:
        print("not in trial_categories.json (filed under Other): " + ", ".join(missing), file=sys.stderr)
    if stale:
        print("in trial_categories.json but not in this run: " + ", ".join(stale), file=sys.stderr)

    os.makedirs(OUT_DIR, exist_ok=True)
    text, by = write_tables(kept, cats, a.date, total, counts, unverified, notes, excluded)
    with open(os.path.join(OUT_DIR, "active-trials.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    rtext, nread = write_readouts(kept, cats, a.date, start, end)
    with open(os.path.join(OUT_DIR, "readouts.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(rtext)
    for k, name in SECTIONS:
        print(f"  {k}: {len(by[k])}", file=sys.stderr)
    print(f"  readouts: {nread}", file=sys.stderr)
    if a.dump:
        with open(a.dump, "w", encoding="utf-8") as f:
            json.dump(kept, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
