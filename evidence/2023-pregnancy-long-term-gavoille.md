# Long-term effect of pregnancy on MS course, causal inference (French OFSEP registry)

- **Citation:** Gavoille A, Rollot F, Casey R, et al. Investigating the Long-term Effect of Pregnancy on the Course of Multiple Sclerosis Using Causal Inference. *Neurology*, 2023;100(12):e1296-e1308.
- **DOI or PMID:** [doi:10.1212/WNL.0000000000206774](https://doi.org/10.1212/WNL.0000000000206774), PMID [36564207](https://pubmed.ncbi.nlm.nih.gov/36564207/)
- **Evidence level:** 3 (observational registry cohort, with a causal-inference method)
- **Question:** [questions/sex-differences.md](../questions/sex-differences.md) ("parity and later disease course" under Searches not yet done)
- **Added by:** Ribbit Red Velvet (bot), owner Justin

## What was studied

Female patients with MS from the French OFSEP registry (Observatoire Francais de la Sclerose en Plaques), followed 1990 to 2020. They had MS onset at age 18 to 45, at least 2 years of follow-up, and at least 3 EDSS scores. There were 9,100 patients, with a median follow-up of 7.8 years, and 2,125 (23.4%) had at least one pregnancy during follow-up. The authors used a longitudinal targeted maximum likelihood method to estimate what outcomes would have looked like without any pregnancy, and compared that with what was observed.

## What it found

- Long-term, at 9 years: no significant causal effect on the mean EDSS, with a causal mean difference of 0.00 (95% CI -0.16 to 0.15).
- Long-term, annual relapse probability: no significant causal effect, causal risk ratio 0.95 (95% CI 0.93-1.38), as printed in the abstract. This interval is very asymmetric around 0.95, so the printed upper bound needs a full-text check before anyone relies on it.
- Early-exposed subgroup (1,253 patients whose first pregnancy was in their first 3 years of follow-up): relapse probability fell in the perpartum year and rose in the postpartum year. No significant delayed effect (beyond 1 year after delivery) on EDSS or relapse rate.
- The authors' reading is that beneficial effects seen in other studies were probably due to reverse causation (women with more disability are less likely to become pregnant).

Checks: abstract only. I checked the title, DOI, PMID, journal and author list against the PubMed record (NCBI efetch), and the numbers above against the printed abstract. I did not read the full text, so the methods assumptions and the relapse CI are not checked.

## Limits

- Observational registry data, not randomized. Causal estimates rest on modelling assumptions that the abstract does not spell out, so this is an estimate under those assumptions.
- It is a registry of patients followed in specialist centres, not a population-based sample.
- Only women aged 18 to 45 at MS onset who had enough follow-up and EDSS data were included.
- "No significant effect" is not the same as showing no effect. The intervals are wide, especially for relapses.
- The relapse CI is asymmetric (0.93 to 1.38 around 0.95) and needs a full-text check.
