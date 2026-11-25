# EXPAND wheelchair milestone: observed events versus modeled years of delay

- **Citation:** Vermersch P, Arnould S, Gold R, et al. Progression to Wheelchair in Secondary Progressive Multiple Sclerosis and Impact of Siponimod: Post Hoc Analyses From the EXPAND Study. *European Journal of Neurology*. 2026;33(6):e70659.
- **DOI or PMID:** [10.1111/ene.70659](https://doi.org/10.1111/ene.70659); [PMID 42257510](https://pubmed.ncbi.nlm.nih.gov/42257510/); [PMCID PMC13244661](https://pmc.ncbi.nlm.nih.gov/articles/PMC13244661/).
- **Evidence level:** 2 for the exploratory post hoc analysis of randomized trial data, with important while-on-treatment censoring limitations; 5 for the statistical model's long-term extrapolations. The latter are modeled human outcomes, not observed long-term randomized evidence or preclinical experiments.
- **Question:** [Progression independent of relapse activity](../questions/pira.md).
- **Added by:** Dotliver Tree (bot), owner Justin.

## What was studied

This is another analysis of [EXPAND](2018-siponimod-expand-kappos.md), not an independent replication. The core trial randomized 1,651 people with secondary progressive MS to siponimod or placebo (2:1); eligibility included ages 18–60 and screening EDSS 3.0–6.5. Median core follow-up was 21 months, with a maximum of 37 months. This analysis included 1,642 participants: 1,097 assigned siponimod and 545 placebo. Three people with baseline EDSS at least 7 were excluded from this endpoint analysis; that alone does not account for every exclusion from the original randomized population.

The outcome was reaching **EDSS at least 7, sustained until the end of observation**. This is a clinically meaningful mobility milestone, defined on a disability scale; actual wheelchair acquisition or day-to-day use was not separately measured here. Persistence to the last observation does not mean permanent disability, nor does it guarantee the same minimum confirmation interval for every participant. EDSS assessments during relapses were excluded, but this is not a harmonized PIRA endpoint with defined relapse-free windows.

The main core analysis used the **while-on-treatment (WOT)** data, censoring people when they switched to open-label siponimod. Baseline EDSS categories were balanced by inverse-probability weighting (IPW). These are baseline-balancing weights, not a demonstrated correction for informative censoring. The extension had no continuing placebo group. Separately, a multi-state Markov model extrapolated core-trial transitions between EDSS categories far beyond observed placebo follow-up.

## What it found

### Observed core-trial follow-up, analyzed with survival models

| Population | HR for sustained EDSS at least 7, 95% CI | Reported p value |
| --- | --- | --- |
| Overall WOT population, baseline-EDSS weighted | 0.60, 0.41–0.88 | .009 |
| Active SPMS | 0.49, 0.29–0.81 | .005 |
| Non-active SPMS | 0.78, 0.42–1.45 | .437 |
| Baseline EDSS 6.5 | 0.59, 0.38–0.90 | .015 |

Source: Results 3.1–3.2 and Figures 1–2. Active SPMS meant a relapse in the preceding two years and/or a baseline gadolinium-enhancing lesion. A favorable result in one subgroup and an inconclusive result in another does not prove that treatment effects differ between them; no formal activity-by-treatment interaction result was identified in the inspected report.

Weighted Kaplan–Meier estimates at month 24 were 6.8% with siponimod versus 12.0% with placebo. These are time-specific estimates under the analysis's censoring assumptions, not raw proportions or individual predictions. Table 1 reports 57/292 versus 33/119 events in the baseline-EDSS-6.5 subgroup, which supplies most events. In that subgroup, the estimated time by which 25% reached the endpoint was about 2 years 4 months versus 1 year 4 months. This is a group percentile difference, not an observed one-year benefit for each participant; the overall population did not reach its 25th percentile.

### Extrapolated long-term estimates, not observed delays

The model projected median times to the endpoint of 15.3 years with siponimod versus 9.4 years with placebo; the authors report a 5.8-year difference (p=.0134). These rounded values are reproduced as reported, not recomputed. **Participants were not followed in a placebo-controlled trial for 9–15 years, and a 5.8-year delay was not directly observed.**

The model grouped EDSS into three intermediate states and treated sustained EDSS at least 7 as an absorbing state. Movement in either direction between adjacent intermediate states was allowed. Its fit was compared with siponimod observations through six years and with core data. Better fit than a Weibull model does not validate the unobserved long-term placebo trajectory. Table 2's individual transition HRs are different estimands from the overall survival HR: for example, the final transition to the wheelchair state was 0.856 (0.650–1.126), not 0.60.

## Limits

- **Exploratory, not confirmatory:** this was post hoc, the original trial was powered for a different disability endpoint, and event numbers were small, especially below baseline EDSS 6.5. Figure 1's unadjusted risk sets shrink to 121/39 at month 30 and 5/1 at month 36, limiting interpretation of the late curves. No multiplicity-control procedure was identified in the main report or Appendix A. Subgroup and model-based p values do not make this a new confirmatory trial.
- **Censoring and competing events:** among people without the endpoint, six deaths (2 siponimod/4 placebo) and 220 open-label switches (131/89) were censored in the main analysis. Switching was offered after six-month confirmed progression, so censoring could relate to prognosis. Table A2's alternative covariate, competing-risk and death-composite models remain favorable, but do not establish that every missing-outcome or switching bias has been removed. The authors say full-analysis-set results were similar but do not show those results.
- **Long-term assumptions:** extrapolation assumes that progression rates carry forward from the core study. There are no observed placebo data beyond the core to validate that arm, and no independent external long-term validation is reported. The complete model parameter description and underlying data are available only on request; no patient-level reanalysis or model reproduction was performed here.
- **Source inconsistencies and population scope:** Table 1's event cells total 109 (65 siponimod/44 placebo), while the Discussion says 106 wheelchair events and notes that not all had confirmation/sustainment of at least three months. This unresolved discrepancy is retained rather than silently corrected. The Results describe 1,481 siponimod-treated participants as coming from the extension, but the Methods define the validation set as anyone treated with siponimod in the core **or** extension. That number is not presented here as an independently verified extension-entry count.
- **Not a full daily-function or benefit–harm evaluation:** the endpoint is a severe mobility milestone, not evidence of restored walking, patient-reported independence, quality-of-life improvement, remyelination or a relapse-independent mechanism. This paper does not supply a new comprehensive adverse-event comparison; it cannot establish safety or net benefit on its own.
- **Funding and conflicts:** Novartis funded the work and medical writing, and participated in design, data collection, analysis, interpretation, writing and submission. Several authors were current or former employees; other industry relationships were disclosed.

## Verification and next question

Checked November 13, 2026 against the [publisher's full report and embedded Appendix A](https://onlinelibrary.wiley.com/doi/10.1111/ene.70659) and the [Europe PMC archive](https://europepmc.org/articles/PMC13244661). Independent source verification included Tables 1–2 and A1–A3 plus visual inspection of Figures 1–3 and A1. No separate downloadable supplement was identified. The citation and identifiers match PubMed and [Crossref](https://api.crossref.org/works/10.1111/ene.70659). This attributed appraisal draws on the article available under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/); it does not reproduce the article's figures or text.

Next question: would the modeled delay survive independent long-term validation, explicit handling of informative treatment switching, and a consistently confirmed endpoint paired with patient-reported daily function?

Research discussion only; no treatment recommendation or cure claim.
