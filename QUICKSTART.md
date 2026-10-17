# Quickstart

## Review without credentials

```sh
git clone https://github.com/Ali-Maq/aya-demo.git
cd aya-demo
python3 scripts/verify_evidence.py
```

Python 3.10 or newer is sufficient. There are no Python dependencies. This checks the published receipt bundle and its claims, not the original execution. Read the implementation pull requests for actual code and CI:

- [Factory frontend and controller](https://github.com/Ali-Maq/aya/pull/1)
- [Crusoe SQL cookbook component](https://github.com/Ali-Maq/crusoe-developer-hub/pull/2)
- [MASS adapter](https://github.com/Ali-Maq/mass/pull/1)
- [Merged jq export component](https://github.com/Ali-Maq/aya-data-recipes/pull/2)

## Inspect the actual experiment source

The source used for the public run and the later evidence publication are pinned separately in `sources.json`.

```sh
git clone --filter=blob:none https://github.com/Ali-Maq/aya.git aya-source
cd aya-source
git checkout 0fe69eac1290d39115ff51fc0655bc25093c22cd
```

The current implementation and setup documentation are on the `aya/factory` branch. The pinned run precedes the future-only public-file staging fix. The raw private `.state` directory, credentials, and provider datasets are intentionally not part of this submission.

## Run in an already configured environment

The live system requires Python 3.12, Bun, Docker, configured Onyx services, installed NemoHermes/OpenShell and a worker, REA/Ghidra with its trusted CA, Langfuse, GitHub authentication, a Crusoe key, and the MASS adapter checkout. This is not a clean-machine one-command installer.

Use the implementation's [AYA README](https://github.com/Ali-Maq/aya/blob/aya/factory/aya/README.md) and [MASS instructions](https://github.com/Ali-Maq/aya/blob/aya/factory/aya/MASS.md) for configuration. Keep secrets in local environment or a credential store, never in the repository. The optional fine-tuning and dedicated inference deployment paths incur provider costs.

From a configured AYA directory, these services run in separate terminals:

```sh
docker compose --env-file .env -f deployment/compose.yml up -d
bash deployment/run-rea.sh
python3 -m aya_factory.server
```

From the configured Onyx `web` directory:

```sh
bun run dev --port 3021 --hostname 127.0.0.1
```

Open `http://localhost:3021/app/factory`. Existing services must be checked before starting replacements. This submission package does not alter local services, fetch secrets, create deployments, or launch billable jobs.

## What a rerun must establish

A reproducible rerun freezes the feature request, repository/reference revisions, workflow, development and held-out split, evaluator, and executor hashes before inference. It records actual calls and independent results, then verifies source bindings before publishing a PR or selecting training rows. Evaluate a trained checkpoint against the same student base model before claiming improved weights.
