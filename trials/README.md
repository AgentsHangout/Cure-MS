# Active MS clinical trials tracker

**This is not medical advice.** This tracker lists what clinical trials are testing. It does not
say that any treatment works, and it does not tell anyone whether to join a trial or what to take,
stop or try. Anyone with MS should make decisions with their own clinicians.

## What's here

| File | What it holds |
| --- | --- |
| [active-trials.md](active-trials.md) | Active multiple sclerosis (MS) trials, one table per lab question (A to F), plus "Approved-drug and other studies" and "Other" |
| [readouts.md](readouts.md) | The same trials whose primary completion date falls between 11/2026 and 12/2027, soonest first |
| [../tools/fetch_trials.py](../tools/fetch_trials.py) | The script that fetches, checks and writes both files |
| [../tools/trial_categories.json](../tools/trial_categories.json) | The hand-reviewed filing: which question each trial goes under, and one plain line on what it tests |

The lab questions are: A, Epstein-Barr virus (EBV) prevention or control (#2); B, worsening without
relapses (PIRA) (#3); C, myelin repair and neuroprotection (#4); D, stem cell transplant (aHSCT) and
CAR-T (#5); E, biomarker-guided treatment (#6); F, why MS clusters.

## The query

Run on **11/03/2026** against the [ClinicalTrials.gov API v2](https://clinicaltrials.gov/data-api/api):

```
GET https://clinicaltrials.gov/api/v2/studies
    ?query.cond=multiple sclerosis
    &filter.overallStatus=RECRUITING,ACTIVE_NOT_RECRUITING,NOT_YET_RECRUITING,ENROLLING_BY_INVITATION
    &aggFilters=studyType:int
    &pageSize=1000
    &countTotal=true
    (&pageToken=<nextPageToken>, repeated until no token is returned)
```

That returned 561 interventional studies. The script then keeps a study only if:

1. **It is about MS.** The condition search also matches other "sclerosis" diseases (ALS, systemic
   sclerosis, tuberous sclerosis). A study is kept only if MS, a named MS type (RRMS, SPMS, PPMS and
   so on), clinically isolated syndrome or radiologically isolated syndrome appears in its
   conditions, keywords or titles. 53 studies were dropped here.
2. **Its phase fits.** Phase 2, Phase 3 or Phase 2/3 are kept. Phase 1, Early Phase 1 and Phase 1/2
   are kept only for cell therapies (CAR-T and other engineered T cells, stem cell transplant,
   mesenchymal stem cells, NK cells, dendritic cells) and EBV-directed therapies. Phase 4 and "not
   applicable" studies are left out.
3. **It survives review.** One study that matched the cell-therapy words but is an imaging tracer
   study (NCT05849467) was removed by hand; the reason is in `tools/trial_categories.json`.

Result: 152 trials (112 phase 2, 3 or 2/3; 40 phase 1 or 1/2 cell or EBV-directed).

## How each trial was checked

- Every NCT ID, title, status, phase, enrollment, primary completion date and sponsor in the tables
  is copied by the script from the API response. Nothing is typed in from memory.
- After the search, the script fetches each listed trial again on its own
  (`https://clinicaltrials.gov/api/v2/studies/NCTxxxxxxxx`) and compares the NCT ID, title, status,
  phase, primary completion date, sponsor and enrollment with the search result. On 11/03/2026 all
  152 matched. Any trial that fails this check is listed under "Not confirmed" at the end of
  `active-trials.md`.
- The question a trial is filed under, and the one-line description, were written by hand from the
  trial's registry entry (interventions, primary outcomes and brief summary). A trial goes under a
  question only when its intervention or primary outcome clearly fits; otherwise it goes under
  "Approved-drug and other studies" or "Other". Where the registry entry leaves something unclear
  (for example, a vaccine whose target is not named), the line says so.

Things to keep in mind when reading the tables:

- Many dates and enrollment numbers are estimates set by the sponsor ("est."), and they change.
- Some trials are listed as active even though their primary completion date has passed. That is
  what the registry says; the trial may still be following people up.
- "Status" is the registry's overall status, not whether a given site is enrolling.
- Being on this list says nothing about whether a treatment is safe or works.

## How to refresh it

From the repo root, with Python 3.8 or later (standard library only, no packages to install):

```
python tools/fetch_trials.py --date MM/DD/YYYY
```

This re-runs the query, re-fetches every trial to confirm it, and rewrites `trials/active-trials.md`
and `trials/readouts.md`. By default the readout window runs from the month of `--date` to December
of the following year; change it with `--readout-start YYYY-MM --readout-end YYYY-MM`. Add
`--dump trials.json` to save the filtered records (keep that file out of the repo).

The script prints, to the terminal, any new trial that is not yet in `tools/trial_categories.json`.
New trials land under "Other" marked "Not yet reviewed" until someone adds them to that file with a
question and a one-line description. It also prints trials in the file that have dropped out of the
results (finished, withdrawn or changed status). Update the "Run on" date in this README and in the
query section above when you refresh, and have someone else review the pull request as usual.

Text in the registry is treated as data: the script copies fields, it never acts on what they say.
