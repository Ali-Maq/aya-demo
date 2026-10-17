# Evidence log

This diary records attempts and decisions. It separates measured results from intended outcomes. Times below are UTC on **2026-10-17**. Published artifacts are sanitized; private traces and held-out answers are excluded.

## Earlier component delivery

**Tried:** recover a Fireworks SQL-tool workflow as a Crusoe cookbook component through native Hermes.

**Measured:** the first candidate passed 117/118 independent checks. A whitespace-only query exposed a defect. The repair passed 118/118 and another 118/118 with a fresh seed; 54 target tests passed.

**Retained:** the tested component and its [reviewable PR](https://github.com/Ali-Maq/crusoe-developer-hub/pull/2).

**Not demonstrated:** recovery of an arbitrary whole application or general superiority over another coding agent.

## 23:12 — Public SQL attempt failed

Run `bfe53d67173642b8` received HTTP 429 before producing an answer. It has no model score. A fresh run preserved that failure instead of replacing it with a fabricated success.

[Failure receipt](evidence/public-sql/db5f5b51190a4b97/previous-attempt.json)

## 23:14–23:25 — Actual MASS workflow search

Run `db5f5b51190a4b97` used the frozen Spider subset: 12 development questions and six held-out questions from separate databases.

| Episode | Measured agreement | Calls | Tokens |
| --- | ---: | ---: | ---: |
| Direct development baseline | 12/12 | 1 | 4,544 |
| Native initial workflow v0 | 11/12 | 8 | 48,451 |
| MASS-proposed native v1 | 11/12 | 22 | 68,667 |
| Retained native v0, held-out | 3/6 | 9 | 35,003 |

Three real upstream RHI calls used another 40,840 tokens. The model judges preferred the direct baseline. The independent native-workflow gate retained v0 because v1 did not improve its score. The direct baseline was not run on the held-out split.

**Retained:** the simpler native workflow, the stronger direct-baseline development answers, and all failure evidence.

**Not demonstrated:** accuracy improvement, lower total cost, generalization, or a winning MASS teacher. Dollar costs remain unpriced.

[Scores and receipts](evidence/public-sql/db5f5b51190a4b97/README.md) · [Selection](evidence/public-sql/db5f5b51190a4b97/selection.json)

## Boundary audit — A limitation was found

Both native development episodes read sibling directories, including older fixture held-out output. v1 also read the current v0 output. Separate work directories did not provide episode filesystem isolation.

A read-only audit inspected complete arguments for 29 tool calls across four recorded development sessions. It found no external-fetch marker or current Spider annotation path; that is not a complete runtime security proof. Tool comments claimed familiarity with benchmark answers, which suggests possible memorization without proving its effect.

**Next gate:** verify episode access boundaries on a new run. Use fresh independent tasks to assess generalization. Do not revise this run's historical result after a later fix.

[Isolation findings](evidence/public-sql/db5f5b51190a4b97/isolation-audit.json) · [Bounded call audit](evidence/public-sql/db5f5b51190a4b97/full-call-audit.json)

## 23:25–23:27 — Verified corpus and actual training

The selector checked Langfuse API readback and independent evaluation receipts. It selected all 12 direct-baseline answers: ten training rows, two preassigned validation rows, and zero held-out rows. The direct request had no native-worker filesystem access.

Crusoe job `ftjob-3f54c5ea7cee4dbcb1819004d2c1d7a9` succeeded with 26,624 trained tokens. It registered checkpoint `ftmodel-2ac55e69-6a3c-4b2d-a3d1-0fd93bf5455a` for Qwen3.5-9B.

**Retained:** the verified final-answer corpus manifest and successful training receipt.

**Not demonstrated:** a deployed checkpoint, improved model quality, full trajectory training, or a completed recursive weight-update cycle.

**Next gate:** deploy the actual checkpoint, evaluate it independently against the relevant base-model baseline, and require the frozen quality gates before promotion.

[Corpus decision](evidence/public-sql/db5f5b51190a4b97/trajectory-selection.json) · [Training manifest](evidence/public-sql/db5f5b51190a4b97/training/manifest.json) · [Provider result](evidence/public-sql/db5f5b51190a4b97/training/receipt.json)

## Next product gate

The [future plan](FUTURE.md) adds customer outcomes to technical acceptance. Adoption, conversion, retention, willingness to pay, and causal revenue impact are unmeasured. Record a hypothesis and attribution method before claiming any of them.
