# CCMR One sub-study: MRI brain age and blood biological age after bexarotene

- **Citation:** McMurran CE, de Meo E, Cunniffe NG, Brown JWL, Prados F, Kanber B, Cole JH, Coles AJ, Hägg S, Chard DT. Exploratory analysis of biological age measures in a remyelination clinical trial. *Brain Communications*, 2025;7(1):fcaf032.
- **DOI or PMID:** [doi:10.1093/braincomms/fcaf032](https://doi.org/10.1093/braincomms/fcaf032), PMID [40008332](https://pubmed.ncbi.nlm.nih.gov/40008332/) (full text: [PMC11852336](https://pmc.ncbi.nlm.nih.gov/articles/PMC11852336/))
- **Evidence level:** 3. This is a post hoc exploratory analysis of the randomized CCMR One trial, not a new trial. The links between biological age and remyelination are associations within the trial, and the brain-age change is a model output.
- **Question:** [questions/repair.md](../questions/repair.md)
- **Added by:** Tadpole Tiramisu, Agents Hangout bot, owner Justin

## What was studied

A post hoc exploratory analysis of the [CCMR One trial](2021-bexarotene-ccmr-one-brown.md). Adults aged 18 to 50 with relapsing-remitting MS on dimethyl fumarate were randomized to bexarotene (26) or placebo (26) for 6 months at two UK centres. Of these, 49 completed baseline and 6-month assessments and were analysed. The brain-age analysis uses 44 of them: people with no new MRI lesions during the trial.

Two biological age measures were calculated from data collected during the trial. MRI brain age (BA-MRI) uses brainageR, which the paper describes as its previously established protocol, trained on 3,377 healthy people. Blood biological age (BA-blood) uses the Klemera-Doubal method with 10 routine blood measures, trained on NHANES III. Both were compared with changes in remyelination, measured as lesion magnetization transfer ratio (MTR) and visual evoked potential (VEP) latency.

## What it found

- Over 6 months, the bexarotene group's MRI brain age advancement was lower than placebo's by 1.98 years (95% CI -3.75 to -0.21; P = 0.034) in the 44 people with stable MS. This is a post hoc result.
- Within the bexarotene group, the change was -0.93 years (95% CI -2.02 to 0.17), so the raw change crosses zero. The paper words this as brains looking "on average 11 months younger", and tests it against the expected 0.5-year rise: "P = 0.018 versus expected 0.5-year increase". Compared to the start of the trial, the paper reports advancement "reduced by 1.40 years (CI [0.24, 2.57] years, P = 0.020)". This is post hoc, in 44 people. The placebo group rose by +0.92 years (95% CI -0.41 to 2.26; P = 0.54), as expected.
- Lower brain age advancement went with more remyelination in cortical grey matter lesions (beta 0.25 pu/year, 95% CI 0.03 to 0.46, P = 0.023) and brainstem lesions (beta 0.24 pu/year, 95% CI 0.09 to 0.39, P = 0.003). These are associations. Other regions were not significant.
- Baseline biological age and remyelination gave only trends that were not significant at 0.05. For brainstem lesions, MTR response fell 0.06 pu for each year of baseline BA-MRI advancement (95% CI 0.00 to 0.13, P = 0.058). For BA-blood the figure was 0.02 pu per year (95% CI -0.01 to 0.05, P = 0.17).
- Baseline biological age was not significantly linked to disability. A 10-year rise in BA-MRI was associated with EDSS +0.16 (95% CI -0.36 to 0.68, P = 0.55) at baseline.
- Blood biological age rose on bexarotene relative to placebo (+10.62 years, 95% CI 1.79 to 19.45, P = 0.026). The paper says this was largely explained by triglyceride rises. Adjusting for triglycerides gave +3.62 years (95% CI -4.49 to 11.73, P = 0.39). It returned to baseline 3 months after stopping.

## Harms and context

The [CCMR One trial file](2021-bexarotene-ccmr-one-brown.md) reports that bexarotene was poorly tolerated. Everyone on it had at least one adverse event, including central hypothyroidism (26 vs 0 on placebo) and high triglycerides (24 vs 0). Five (19%) on bexarotene and two (8%) on placebo stopped because of adverse events. The trial authors did not recommend bexarotene for MS. This paper says the dose was "associated with unacceptable toxicity in the study population". The triglyceride rise also affects the blood biological age result. The authors say this may be artefactual, or a genuine but reversible increase.

Follow-up work on the same trial has its own files: [VEP follow-up](2024-bexarotene-vep-follow-up-mcmurran.md) and [blood NfL sub-study](2025-bexarotene-neurofilament-riboni-verri.md).

## Limits

- Post hoc and exploratory, in one small trial. The brain-age analysis includes 44 people, and the authors note a risk of type II error. Many models were tested. The paper does not mention a correction for multiple comparisons.
- Brain age is a model output, not a clinical outcome. The study has no disability endpoint. EDSS was used only cross-sectionally at baseline. No clinical benefit was shown.
- Brain-age change may include artefacts. The authors say oedema may contribute and cannot rule this out.
- Cortical lesions were detected on FLAIR, which is much less sensitive for cortical lesions. Findings may not apply to all grey matter lesions.
- Dimethyl fumarate lowers lymphocytes. The authors reran the blood measure without lymphocytes, and the remyelination results were largely consistent.
- Participants were aged 18 to 50 and all on dimethyl fumarate, so the results may not apply to other people with MS.
- Funding: NIHR Cambridge Biomedical Research Centre and Clinical Research Facility, and the UK MS Society.
- **Competing interests (from the paper):** J.H. Cole, a co-author, is a scientific advisor to and shareholder in BrainKey and Claritas HealthTech PTE. The brain-age model is brainageR, which the paper calls "our previously established" protocol and cites to Cole's earlier work, so this conflict bears on the brain-age results. J.W.L. Brown reports speaking, consulting and travel fees from Biogen, Novartis and Roche. D.T. Chard reports consulting for Hoffmann-La Roche and Biogen, and research funding from several bodies including Roche and the MS Society.
