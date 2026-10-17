# AYA

**Recover a software capability. Test it independently. Ship a reviewable pull request.**

AYA is a software factory built into Onyx. Give it a target GitHub repository, a feature request, and a reference implementation. Hermes investigates the reference inside OpenShell, implements the component, writes tests, and returns a change. A separate controller decides whether the change meets the frozen contract.

The second part asks a harder question: **does a more elaborate agent workflow actually improve the result?** AYA runs Sakana AI's MASS workflow improvement loop, records actual trajectories in Langfuse, compares them with a direct baseline, and selects verified development answers for training.

[Implementation](https://github.com/Ali-Maq/aya/pull/1) · [Architecture](ARCHITECTURE.md) · [Quickstart](QUICKSTART.md) · [Verified experiment](evidence/public-sql/db5f5b51190a4b97/README.md)

## Two working paths

| Path | Concrete demonstration | Review the result |
| --- | --- | --- |
| Product iteration | Recover a Fireworks SQL-tool workflow and add a tested Crusoe cookbook component. The first native candidate failed one independent check; the repair passed 118/118, then 118/118 on a fresh seed. | [Crusoe component PR](https://github.com/Ali-Maq/crusoe-developer-hub/pull/2) |
| Agent workflow iteration | Run a direct baseline, two native Hermes workflows, and MASS feedback on a frozen public Spider subset. Store and verify trajectories; select the best available development answers for SFT. | [MASS adapter PR](https://github.com/Ali-Maq/mass/pull/1) |
| Earlier binary recovery | Investigate the installed jq binary with REA/Ghidra, recover a bounded JSON export component, and integrate it with Open WebUI. | [Merged component PR](https://github.com/Ali-Maq/aya-data-recipes/pull/2) |

The SQL cookbook is source and behavior recovery. The jq example is binary investigation. Neither is a claim to reconstruct an entire arbitrary application.

## What the real experiment found

Public Spider run `db5f5b51190a4b97` used 12 development questions and 6 held-out questions from different databases.

| Episode | Execution agreement | Actual API calls | Total tokens |
| --- | ---: | ---: | ---: |
| Direct baseline | 12/12 development | 1 | 4,544 |
| Native Hermes v0 | 11/12 development | 8 | 48,451 |
| Native Hermes v1 | 11/12 development | 22 | 68,667 |
| Selected native v0 | 3/6 held-out | 9 | 35,003 |

Three real upstream MASS feedback calls used 40,840 tokens. Both comparison judges preferred the baseline. The workflow search did **not** improve development accuracy. The baseline was not evaluated on the held-out split, so this is not a held-out comparison.

The trajectory selector independently checked Langfuse readback and test receipts, then chose all 12 baseline answers: 10 training, 2 fixed validation, and **zero held-out examples**. A real Crusoe supervised fine-tuning job succeeded, processing 26,624 tokens and registering checkpoint `ftmodel-2ac55e69-6a3c-4b2d-a3d1-0fd93bf5455a`. The checkpoint has **not been deployed or evaluated**. This is final-answer distillation into Qwen3.5-9B, not a demonstrated recursive improvement in model weights.

These are execution-agreement results on a small public subset, not an official Spider leaderboard score. Public benchmark familiarity may affect results. The native workers also accessed sibling episode directories, including output from an older fixture's held-out run. That isolation failure is preserved in the evidence. The direct baseline had no worker filesystem access. We make no general superiority or complete filesystem isolation claim.

## Inspect the evidence

This repository is the small submission package. The implementation lives in the linked repositories; its history is preserved there. Public evidence contains sanitized receipts, scores, source hashes, provider response IDs, usage, workflow comparisons, and the training result. It excludes raw private reasoning, credentials, held-out questions and answers, and training data.

```sh
git clone https://github.com/Ali-Maq/aya-demo.git
cd aya-demo
python3 scripts/verify_evidence.py
```

The verifier checks every published artifact digest and the reported result/selection/training invariants. It makes no API calls and does not rerun inference. See [QUICKSTART.md](QUICKSTART.md) for the configured live environment and reproduction boundaries.

## Stack and attribution

Crusoe inference and fine-tuning · Onyx frontend · NemoClaw/NemoHermes · Hermes Agent · NVIDIA OpenShell · REA/Ghidra · Sakana AI MASS · Langfuse · GitHub Actions.

The Spider source is credited to Yu et al. (2018), distributed under CC BY-SA 4.0. The public experiment uses a pinned subset and an AYA evaluator. Upstream software retains its own license. [sources.json](sources.json) records exact implementation and evidence revisions.
