# Does blood NfL improve prediction of treatment response?

- **Citation:** Moradi N, Sharmin S, Malpas CB, et al. Neurofilament Light Chain Concentration in the Prediction of Treatment Response in Multiple Sclerosis. *European Journal of Neurology*, 2026;33(2):e70505.
- **DOI or PMID:** [doi:10.1111/ene.70505](https://doi.org/10.1111/ene.70505), PMID [41622995](https://pubmed.ncbi.nlm.nih.gov/41622995/)
- **Evidence level:** 3 (pooled cohorts)
- **Question:** [questions/biomarkers.md](../questions/biomarkers.md)
- **Added by:** ron (bot), owner morgkorg

## What was studied

A prediction study pooling cohorts from University Hospital Basel, the SET cohort in Prague, and the
Swedish EIMS and IMSE cohorts. Each person had one serum or plasma NfL measurement within 90 days of
a disability assessment, which was taken as the study baseline. People were either already on a
treatment at baseline or started one within 60 days (pooled mean treatment duration at baseline
200 days, SD 482, with negative values for later starts), so this is not a uniformly pre-treatment
sample. NfL was age-normalized against a reference
population.

Cox models predicted relapse, 6-month confirmed disability worsening and 9-month confirmed
disability improvement, with and without NfL, on top of clinical and demographic information
summarized as principal components. Discrimination (Uno's concordance index) was assessed over a
4-year prediction horizon with 5,000-repeat bootstrap validation.

## What it found

- 1,716 people were in the pooled analysis, followed for a mean of 9 years. Three treatments had
  enough people and events for separate models: interferon beta (554), fingolimod (307) and
  natalizumab (369). The other 486 were on other treatments, which the main text does
  not name, and appear only in the pooled models.
- In the pooled cohort, no statistically significant association between NfL and the outcomes was
  detected after adding the clinical and demographic components. Models without those components
  did show associations.
- Pooled discrimination was moderate (concordance 63.4% for relapse, 56.4% for worsening, 67.7% for
  improvement), and adding NfL changed it little.
- In treatment-specific models, discrimination with and without NfL was mostly similar. Two
  exceptions: the fingolimod models for disability improvement did not converge, so there is no
  result; and Table 3 lists natalizumab disability-improvement concordance as 50.6% without NfL and
  65.0% with NfL, although the text describes similar performance. That discrepancy is unresolved.
- In the natalizumab group, higher age-normalized NfL was associated with a lower chance of
  disability improvement (HR 0.819, reported 95% CI 0.814 to 0.823).
- In a sensitivity cohort on stable treatment, NfL was associated with disability worsening after
  adjustment, while discrimination changed little, showing that an association and better
  prediction are different things.
- The authors conclude that NfL adds minimal predictive value beyond clinical information for these
  treatments.

## Limits

- The natalizumab HR interval is present in the source (and the supplement also reports very narrow
  intervals), but its unusually high precision for 369 people is unexplained. The bootstrap repeats
  apply to the concordance validation and do not by themselves explain it.
- The table and text disagree about natalizumab improvement, as above.
- The cohorts had different structures and protocols and come from different treatment eras; the
  authors mapped variables across them to reduce this.
- No separate estimates for any treatment other than these three, so it does not address newer
  high-efficacy treatments.
- Hazard ratios are for scaled age-normalized NfL, not a change of one pg/mL.
- This tests a single NfL measure for prediction. It is not a trial showing that NfL-guided
  decisions improve outcomes, and it does not test repeated monitoring (see
  [2026-nfl-z-score-change-treatment-monitoring-fernandez](2026-nfl-z-score-change-treatment-monitoring-fernandez.md)).
- **Funding and disclosures:** funded by the National Health and Medical Research Council of
  Australia. Several authors report fees or research support from companies that make MS
  treatments.
- Numbers come from the open-access full text, tables and supplement (PMC12862443).
