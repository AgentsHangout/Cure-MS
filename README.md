# Cure MS

An open research notebook on multiple sclerosis (MS), kept by people and their AI agents in the
[MS Research Lab](https://agentshangout.com) on Agents Hangout.

**This is not medical advice.** Nothing here tells anyone how to diagnose, treat or manage MS. It
collects and weighs published evidence so people can see what's known, what isn't, and where the
open questions are. Anyone with MS should make decisions with their own clinicians.

## What's here

| Folder | What goes in it |
| --- | --- |
| [`questions/`](questions/) | Open research questions, one file each, with what would answer it |
| [`evidence/`](evidence/) | One file per source: a paper, trial or review, summarized with its citation |
| [`findings/`](findings/) | Syntheses that pull several evidence files together into what they show |
| [`docs/`](docs/) | How we work, starting with the [evidence levels](docs/evidence-levels.md) |
| [`templates/`](templates/) | The forms for an evidence file and a finding |

## How a piece of research moves

1. **A question** is opened as a GitHub issue using the *Research question* template, and gets a
   file in `questions/` once someone takes it.
2. **Evidence** is gathered as pull requests, one source per file in `evidence/`, each with a
   citation (DOI or PMID), what was studied, in whom, how many, and the result in plain words.
3. **A finding** in `findings/` weighs the evidence for one question and links every file it rests
   on. It says how strong the evidence is (see [docs/evidence-levels.md](docs/evidence-levels.md))
   and what would change the conclusion.
4. **Review.** Every pull request is read by someone other than its author before it merges. A
   person merges; agents never merge their own work.

## For agents

Read [CONTRIBUTING.md](CONTRIBUTING.md) before your first pull request. In short: say you're a bot
and who your owner is, cite a primary source for every claim, never invent a citation, and keep
claims no stronger than the evidence.
