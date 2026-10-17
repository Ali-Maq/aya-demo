# AYA

**Bring a specification and a working reference. Get a tested component and a reviewable pull request.**

AYA is a software factory built into Onyx. Hermes investigates a reference with REA inside OpenShell, implements a bounded component, and writes tests. Independent checks and CI control delivery. A second loop uses MASS and recorded trajectories to test whether a different workflow is better.

[Watch the demo](https://ali-maq.github.io/aya-demo/) · [Download video](https://github.com/Ali-Maq/aya-demo/releases/download/v1.0.0/AYA-demo.mp4) · [Slides](https://github.com/Ali-Maq/aya-demo/releases/download/v1.0.0/AYA-MASS-demo.pptx) · [Architecture](ARCHITECTURE.md) · [Quickstart](QUICKSTART.md) · [Actual experiment record](EVIDENCE-LOG.md)

## Target outcome

This is the intended operating model, not a claim that every step has been demonstrated:

1. Start with a feature specification, target repository, and working reference.
2. Recover a component that matches the required behavior.
3. Pass independent checks and deliver a PR with CI.
4. Choose the cheapest workflow that meets the quality bar, including review and repair costs.
5. Release to a limited customer group and measure adoption and willingness to pay.
6. Retain contracts, tested approaches, failures, and permitted customer feedback so the next feature and workflow decision starts with evidence.

The goal is lower total cost per accepted feature, followed by cost per validated paying-customer outcome. Customer value needs its own measurement and attribution; successful code generation does not establish revenue. [Future operating model and success criteria](FUTURE.md).

## What exists now

The prototype has produced real pull requests and a completed Crusoe training job; checkpoint deployment and any quality gain remain unproven.

- [Onyx factory and controller](https://github.com/Ali-Maq/aya/pull/1)
- [Fireworks SQL workflow adapted into a Crusoe component](https://github.com/Ali-Maq/crusoe-developer-hub/pull/2)
- [Actual Sakana AI MASS adapter](https://github.com/Ali-Maq/mass/pull/1)
- [Earlier jq binary investigation and merged export component](https://github.com/Ali-Maq/aya-data-recipes/pull/2)

The current prototype supports bounded feature contracts. A new domain needs a contract and an independent evaluator. The SQL example uses source and behavior analysis; jq is the separate binary example. Neither reconstructs an entire arbitrary application.

[Read the measured results, failures, isolation limits, and training status](EVIDENCE-LOG.md). The original sanitized receipts are preserved unchanged in [the public experiment bundle](evidence/public-sql/db5f5b51190a4b97/README.md). The record does not establish general agent superiority or a completed recursive weight-improvement loop.

## Verify the published evidence

```sh
git clone https://github.com/Ali-Maq/aya-demo.git
cd aya-demo
python3 scripts/verify_evidence.py
```

This checks artifact hashes and receipt consistency without credentials or API calls. It does not rerun inference. [Quickstart](QUICKSTART.md) explains the configured live environment and reproduction boundaries.

This is the small submission package; implementation histories remain in the linked repositories. [sources.json](sources.json) pins the actual run and publication revisions.

## Built with

Crusoe inference and fine-tuning, Onyx, NemoClaw/NemoHermes, Hermes Agent, NVIDIA OpenShell, REA/Ghidra, Sakana AI MASS, Langfuse, and GitHub Actions.

Spider is credited to Yu et al. (2018), distributed under CC BY-SA 4.0. Upstream software retains its own license. The intended organizational memory is exportable across model providers; customer feedback integration and controlled commercial rollout are future work.
