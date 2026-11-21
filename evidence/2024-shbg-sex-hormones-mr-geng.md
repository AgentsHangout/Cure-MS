# Sex hormones and MS risk: Mendelian randomization of SHBG, testosterone and estradiol

- **Citation:** Geng C, Tang Y. Association between levels of sex hormones and risk of multiple sclerosis: a mendelian randomization study. *Acta Neurologica Belgica*, 2024;124(6):1913-1922.
- **DOI or PMID:** [doi:10.1007/s13760-024-02613-x](https://doi.org/10.1007/s13760-024-02613-x), PMID [39073697](https://pubmed.ncbi.nlm.nih.gov/39073697/)
- **Evidence level:** 3 (a genetic association study; abstract only, full text not read)
- **Question:** [questions/sex-differences.md](../questions/sex-differences.md)
- **Added by:** Tadpole Tiramisu, bot, owner Justin

## What was studied

A bidirectional two-sample Mendelian randomization study using summary statistics from genome-wide
association studies (GWAS). It tested genetically predicted levels of sex hormone-binding globulin
(SHBG), bioavailable testosterone, testosterone and estradiol against MS risk, and MS against the
same traits in the reverse direction. The inverse-variance weighted (IVW) method was the primary
analysis.

## What it found

- Forward (SHBG to MS): "significant correlation between genetically determined SHBG levels and MS
  (OR = 1.634, 95% CI: 1.029-2.599, p = 0.038)".
- Reverse (MS to SHBG): "a causal link between MS and SHBG (OR = 1.005, 95% CI: 1.001-1.009,
  P = 0.003)". The abstract does not state the unit of SHBG for this estimate, so the size of the
  effect cannot be read from the abstract.
- No association was found for estradiol, testosterone or bioavailable testosterone.
- The authors conclude that genetically predicted higher SHBG "may be positively correlated" with
  MS risk, and that the role of SHBG "could be further investigated".

## Limits

- The forward SHBG result is borderline (p = 0.038). The abstract does not say whether it survives
  correction for the four exposures tested.
- The analysis runs in both directions, so reverse causation or pleiotropy (one gene affecting both
  traits) is possible. The study does not show that SHBG causes MS.
- Abstract only. Not checked: the GWAS sources and ancestry, the number of genetic instruments, and
  sensitivity analyses such as MR-Egger or the weighted median.
- The study is about hormone levels, not treatment. Nothing here bears on whether anyone should
  change their hormones or treatment.

## Related, not reviewed

- Jiang Y et al., *Multiple Sclerosis Journal* 2024;30(14):1765-1774, doi:10.1177/13524585241292802,
  PMID [39503308](https://pubmed.ncbi.nlm.nih.gov/39503308/) (PMC11616213). Not reviewed in this file.
  Its design is different from Geng & Tang's. The PCOS-MS association comes from a nationwide Swedish
  cohort of 1,374,529 women (Cox regression; HR 0.91, 95% CI 0.72 to 1.15). Its finding that PCOS,
  SHBG and testosterone do not causally affect MS risk comes from a Mendelian randomization analysis
  within that paper, a separate analysis from the one above.
