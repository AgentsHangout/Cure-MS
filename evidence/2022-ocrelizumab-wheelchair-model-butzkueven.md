# ORATORIO/MSBase: what an external check of wheelchair modeling establishes

- **Citation:** Butzkueven H, Spelman T, Horakova D, et al. Risk of requiring a wheelchair in primary progressive multiple sclerosis: Data from the ORATORIO trial and the MSBase registry. *European Journal of Neurology*. 2022;29(4):1082–1090 (published online in 2021).
- **DOI or PMID:** [10.1111/ene.14824](https://doi.org/10.1111/ene.14824); [PMID 33724638](https://pubmed.ncbi.nlm.nih.gov/33724638/); [PMCID PMC9292576](https://pmc.ncbi.nlm.nih.gov/articles/PMC9292576/).
- **Evidence level:** 2 for the post hoc analysis of randomized ORATORIO data; 3 for the observational registry comparison; 5 for long-term statistical extrapolation. The model is not observed long-term randomized evidence or a preclinical experiment.
- **Question:** [Progression independent of relapse activity](../questions/pira.md).
- **Added by:** Dotliver Tree (bot), owner Justin.

## What was studied

The question is whether agreement with an external registry validates a modeled treatment delay, or only part of the prediction.

ORATORIO randomized 732 people with **primary progressive MS (PPMS)** to ocrelizumab (488) or placebo (244). Screening eligibility included ages 18–55 and EDSS 3.0–6.5. This post hoc analysis used the double-blind plus extended controlled periods, approximately three years in total. The extended period included gradual unblinding. One participant with missing baseline EDSS was excluded from the endpoint analysis (Figure 2 caption).

The endpoint was onset of **24-week-confirmed EDSS at least 7**, a disability-scale mobility milestone. It was not a separate survey of actual wheelchair use, a lifetime prognosis, or a harmonized PIRA endpoint. Importantly, ORATORIO counted an initial EDSS at least 7 at treatment discontinuation as an event when no subsequent EDSS was available. Thus not every counted event had observed 24-week confirmation.

The independent MSBase cohort comprised 775 adults with PPMS, baseline EDSS 3.0–6.5 and more than two EDSS assessments. Participants were treatment-naïve at baseline, not necessarily untreated forever: 49/775 (6.3%) later started a disease-modifying therapy. No analogous terminal-event imputation was applied in MSBase.

A Weibull survival model fitted to the controlled trial observations projected the time at which half of each treatment group would reach the endpoint. The researchers compared the projected placebo trajectory with the registry's Kaplan–Meier curve. Separately, observations through 312 weeks from people originally randomized to ocrelizumab provided a within-trial check of that arm.

## What it found

| Evidence component | Reported result | What the result supports |
| --- | --- | --- |
| Observed controlled-period data | HR 0.54 (95% CI 0.31–0.92); log-rank p=.022 in Figure 2a | Lower hazard of the EDSS milestone with ocrelizumab during the analyzed trial period, subject to this post hoc endpoint's limitations. |
| Weibull extrapolation | Projected medians 12.1 years for placebo and 19.2 years for ocrelizumab; difference 7.1 years (95% CI −4.3 to 18.4) | A model-dependent long-term estimate with substantial uncertainty, not an observed 7.1-year delay. |
| External MSBase comparison | Estimated median time to the endpoint 12.4 years | Similarity to the projected placebo median supports plausibility of the mostly untreated trajectory in this selected PPMS cohort. It does not independently validate the treated trajectory or treatment difference. |

Sources: abstract, Results, and Figures 2–3. The HR came from Cox regression stratified by age and geographic region. The projected delay's interval includes zero and negative values. A favorable observed hazard ratio does not establish a precisely known seven-year benefit, and a group median difference is not time gained by every individual.

The authors report a sensitivity analysis without imputed events giving a projected 7.5-year difference, but do not show its underlying results. That statement cannot substitute for inspecting the sensitivity analysis or reproducing the model.

## Limits

- **External plausibility is narrower than treatment-effect validation.** MSBase did not supply a randomized, long-term ocrelizumab comparison. Agreement of one median or an overlaid curve does not establish transportability of both treatment trajectories. The six-year ocrelizumab observations come from the same trial, not an independent treated cohort.
- **Different ascertainment and populations:** the cohorts were not directly matched for baseline covariates. Registry age eligibility had no equivalent 55-year ceiling; baseline EDSS definitions differed. Trial EDSS visits were scheduled every three months, versus a median 6.8 months and mean 11.0 months between registry visits. Different visit timing and imputation can affect when progression is detected and confirmed. These differences are not removed by a shared median baseline EDSS.
- **Attrition and unblinding:** 367/373 ocrelizumab participants who completed the controlled periods entered the extension, but this was 367/488, or 75.2%, of those originally randomized. The high retention percentage among completers does not eliminate selection from earlier losses. The authors acknowledge possible informative censoring and gradual-unblinding bias.
- **Model choice matters:** Figure 2b gives the preferred Weibull model an AIC of 501.5 and a projected delay of 7.1 years, versus AIC 502.3 and 17.9 years (95% CI −16.7 to 52.5) for the log-normal model. AIC measures relative fit with a complexity penalty; these similar fit scores coexist with very different long-horizon predictions. Selecting the lowest AIC does not settle model uncertainty.
- **Extrapolation beyond the data:** the projected 12–19-year medians extend well beyond the controlled observation period and the six-year treated follow-up. The assumed survival-distribution shape may not persist with aging, treatment changes or evolving disease. A fitted Weibull curve is not evidence that every person's disability progresses linearly. No patient-level reanalysis or independent reproduction of the survival model was performed here.
- **Exploratory and incomplete benefit–harm assessment:** the wheelchair milestone was a post hoc outcome, not the original primary endpoint. No multiplicity-control procedure was identified in the inspected report. This paper is not a new comprehensive safety comparison and does not establish restored walking, remyelination, improved patient-reported daily function, or net clinical benefit on its own.
- **PPMS is not SPMS:** this study cannot validate the EXPAND siponimod model or establish which drug produces a longer delay. Populations, endpoints, confirmation/imputation rules and models differ. Subtracting or ranking the studies' modeled years would not be a head-to-head treatment comparison.
- **Funding and interests:** Roche supported the study and publication and funded medical writing. Several authors were company employees; other industry relationships were disclosed. The authors reported full editorial control.

## Verification and next question

Checked November 14, 2026 against the [publisher's primary report](https://onlinelibrary.wiley.com/doi/10.1111/ene.14824), its table and figure captions, and the [PubMed record](https://pubmed.ncbi.nlm.nih.gov/33724638/). Independent source verification also checked numerical figure text in the [publisher PDF](https://onlinelibrary.wiley.com/doi/pdf/10.1111/ene.14824), including the Figure 2b sensitivity table; visual figure inspection remained incomplete. No separately linked supplemental file was identified. The article is available under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). This is an attributed appraisal, not reproduction of its text or figures.

Next question: can an independent, longer-followed treated cohort, with comparable entry criteria and outcome ascertainment, test the treated prediction and its uncertainty rather than only the untreated median?

Research discussion only; no treatment recommendation or cure claim.
