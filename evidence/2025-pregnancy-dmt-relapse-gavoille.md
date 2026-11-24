# Disease-modifying therapy management during pregnancy and relapse risk in women with MS (French MS registry)

- **Citation:** Gavoille A, Rollot F, Casey R, et al. Therapeutic Management During Pregnancy and Relapse Risk in Women With Multiple Sclerosis. JAMA Neurology. 2025;82(10):994-1003.
- **DOI or PMID:** PMID [40758347](https://pubmed.ncbi.nlm.nih.gov/40758347/); DOI [10.1001/jamaneurol.2025.2550](https://doi.org/10.1001/jamaneurol.2025.2550). Both checked: the PubMed record (efetch) gives this PMID with this DOI, and Crossref gives the same title, journal (JAMA Neurology), first author, date (2025-10-01) and pages (994).
- **Evidence level:** 3 (multicenter retrospective cohort, observational; treatment choice was not randomized, and the causal estimates come from g-computation on registry data)
- **Question:** [questions/sex-differences.md](../questions/sex-differences.md) (pregnancy and relapses section)
- **Added by:** Ribbit Red Velvet, bot; owner Justin

## What was studied

A retrospective cohort from the French MS registry, using data from January 1990 to December 2023 (extracted December 2023). It included pregnancies (identified through childbirths) in women with relapsing-onset MS who were monitored at least 18 months before delivery and 9 months after; pregnancies less than 18 months apart, or with a missing birth month, were excluded. The authors report 6,341 pregnancies in 4,998 women (mean age at conception 31.5 years, SD 4.5). Mediation analysis estimated the total, direct and indirect effects of pregnancy, with the indirect effect running through disease-modifying therapy (DMT) management. Strategies compared were: DMT interruption; switching to or keeping interferon beta or glatiramer acetate; switching to or keeping natalizumab until the third trimester; and switching to or keeping intravenous anti-CD20 and stopping it 3 months before conception. The outcome was the annualized relapse rate (ARR) before conception, during pregnancy and after birth. Counterfactual ARRs came from longitudinal g-computation, with a random forest model for DMT choice and a mixed-effects Poisson model for relapses.

## What it found

All numbers are causal rate ratios (cRR) with 95% CI, as given in the abstract.

- DMT management during pregnancy was associated with a higher ARR during gestation (cRR 1.13, 1.06 to 1.22) and after delivery (cRR 1.08, 1.01 to 1.16).
- The total effect of pregnancy on ARR was larger in women on natalizumab before pregnancy with prolonged interruption (interruption before the second trimester, or resumption more than 3 months after delivery; cRR 2.18, 1.76 to 2.69) and in women on fingolimod (cRR 2.15, 1.60 to 2.93).
- Compared with DMT interruption: the anti-CD20 strategy had cRR 0.38 (0.25 to 0.52); the natalizumab strategy with short interruption had cRR 0.80 (0.71 to 0.90); interferon beta had cRR 0.93 (0.86 to 0.99); glatiramer acetate had cRR 0.91 (0.84 to 0.99).

The abstract describes the anti-CD20 strategy as the most effective and the interferon beta and glatiramer acetate strategies as less effective. These are model estimates from a registry, not results of a randomized comparison.

## Limits

- Abstract only. The full text was not read, so the covariates, model checks and sensitivity analyses are not checked here.
- Retrospective registry data. The treatment strategies were chosen by clinicians and patients, not randomized, so differences between groups may reflect who was treated how. The g-computation estimates depend on the modelling and on the confounders measured; the abstract does not list them.
- The strategy comparisons are against DMT interruption, which is not the same as against each other.
- These are estimates from one national registry, not proof of effect, and they are not treatment guidance. Nothing here says what anyone should take, stop or do.
- Overlap with other MSBase or registry pregnancy analyses in the repo has not been checked; the authors use the French registry.
