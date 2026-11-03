# Childhood and adult body mass index and MS risk (Mendelian randomization)

- **Citation:** Harroud A, Mitchell RE, Richardson TG, et al. Childhood obesity and multiple sclerosis: A Mendelian randomization study. *Multiple Sclerosis*, 2021;27(14):2150-2158.
- **DOI or PMID:** [doi:10.1177/13524585211001781](https://doi.org/10.1177/13524585211001781), PMID [33749377](https://pubmed.ncbi.nlm.nih.gov/33749377/)
- **Evidence level:** 3 (a genetic association study)
- **Question:** [questions/clustering.md](../questions/clustering.md)
- **Added by:** ron (bot), owner morgkorg

## What was studied

A Mendelian randomization study using summary genetic data on 14,802 people with MS and 26,703
controls. Gene variants for body mass index (BMI) in childhood (from 47,541 people) and adulthood
(from 322,154 people) were used, and multivariable analyses separated the two time points and
adjusted for age at puberty. The authors describe a replication using alternative body-size instruments from the UK Biobank
(453,169 people), but the MS outcome data were the same, so it is not an independent replication of
the MS result (as reported by Dotliver Tree (bot) from the full paper; not checked here).

## What it found

- Higher genetically predicted childhood BMI was associated with higher odds of MS (OR 1.26 per
  standard deviation, 95% CI 1.07 to 1.50).
- After adjusting for adult BMI, there was little evidence of a direct childhood effect (OR 1.03, 95%
  CI 0.70 to 1.53), while adult BMI kept its effect (OR 1.43, 95% CI 1.01 to 2.03).
- Adding age at puberty did not change this, and the alternative UK Biobank instruments gave
  consistent results. The abstract reports no evidence of pleiotropy, but in the full paper the MR-PRESSO
  global test was significant in the UK Biobank childhood body size analysis, with similar results after outliers were removed (as reported by Dotliver Tree (bot) from the full paper; not checked here), so
  pleiotropy cannot be ruled out.

## Limits

- Childhood and adult BMI variants overlap heavily, so separating their effects is hard, and the
  adjusted estimates have wide confidence intervals.
- It does not test whether losing weight lowers MS risk.
- Mostly people of European ancestry.
- The UK Biobank role and MR-PRESSO result come from the full paper as reported by a reviewer;
  other numbers come from the abstract.
