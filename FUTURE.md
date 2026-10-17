# What AYA should learn next

AYA should help an organization choose, build, and improve useful software capabilities. A feature request starts the work; evidence decides whether the result deserves adoption. More agents or more generated code are not the objective.

## Observed, ideal, and future

| Scope | Evidence or acceptance condition |
| --- | --- |
| Observed software delivery | The recovered Crusoe SQL component passed 118 independent checks, then 118 with a fresh seed. Its [PR](https://github.com/Ali-Maq/crusoe-developer-hub/pull/2) records the repair and tests. |
| Observed workflow experiment | The direct baseline passed 12/12 development questions. Native v0 and v1 each passed 11/12; v1 used 22 API calls. The experiment did not demonstrate a workflow gain. |
| Ideal next experiment | A candidate meets every predeclared quality, privacy, isolation, and integration gate, then delivers equal or better independently measured quality at lower total measured cost. A comparable held-out evaluation is required. |
| Future product outcome | A shipped feature produces a measurable customer outcome that justifies its development and operating cost. No adoption, revenue, or willingness-to-pay result has been measured here. |

An ideal result would have been a cheaper workflow that preserved correctness and passed the held-out and isolation gates. That result cannot be manufactured by weakening tests or changing the benchmark after seeing outputs. Rejecting the 22-call candidate was useful: it cost more measured calls and tokens without improving the score. The baseline was not tested on this held-out split, so this run cannot establish its held-out advantage.

## Make expenditure visible

The operational objective is:

**Minimize total cost per accepted feature, subject to fixed acceptance gates.**

Count reference investigation, unsuccessful candidates, workflow search, evaluation, model calls, infrastructure, review, and attributable training costs. Keep latency and human review time visible. Do not report only the final successful generation.

This demo records calls, tokens, and elapsed time. It does not have complete dollar pricing. These are separate measured quantities, not interchangeable money estimates. The controller uses execution limits and quality-first tie-breaks; it has not learned an optimal token budget.

Later, evaluate **experiment cost per validated customer outcome**. Define the outcome and attribution method before launch. A paid conversion, repeated use, or retained customer can be an outcome; a generated feature is not one by itself.

## Close the customer loop

1. Capture a customer problem, reference behavior, target repository, and success hypothesis.
2. Recover the capability and ship a bounded, tested experiment through a reviewable PR.
3. Observe feature activation, repeat use, paid conversion, retention, and customer feedback.
4. Compare equivalent cohorts or use a controlled rollout where feasible. Record exposure, time windows, confounders, and uncertainty.
5. Retain, revise, or retire the feature. Convert the decision into the next feature contract and workflow experiment.

Willingness to pay is a hypothesis until customers make relevant choices. Surveys can inform it; they do not replace observed purchase or renewal behavior. A conversion change needs attribution before it is credited to the feature.

## Keep organizational learning portable

The durable asset is an inspectable record: GitHub specs, contracts, source provenance, tests, evaluator versions, PRs, failures, decision records, and exportable Langfuse traces. Reuse a proven contract or a rejected hypothesis before repeating the same work. Apply the organization's access, retention, and privacy policies to these records.

Knowledge continuity should not depend on one chat session or one provider. Model checkpoints are a separate asset: export formats, serving compatibility, access rights, and applicable licenses determine their portability. This demo does not establish ownership or unrestricted portability of a provider's base weights.

[MASS](https://arxiv.org/abs/2610.12176) connects workflow improvement to model training and repeats with updated weights. AYA completed one real workflow search and a separate successful final-answer SFT job. Its checkpoint still needs deployment and independent evaluation before another cycle can demonstrate recursive model improvement.

See the [dated evidence log](EVIDENCE-LOG.md), [measured experiment](evidence/public-sql/db5f5b51190a4b97/README.md), and [pinned sources](sources.json).
