#!/usr/bin/env python3
"""Verify public receipt integrity and the submission's bounded result claims."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "evidence/public-sql/db5f5b51190a4b97"


def read(name):
    return json.loads((BUNDLE / name).read_text())


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def main():
    checksums = read("SHA256SUMS.json")
    actual = {str(p.relative_to(BUNDLE)) for p in BUNDLE.rglob("*") if p.is_file()}
    require(actual == set(checksums) | {"SHA256SUMS.json"}, "unexpected or missing artifact")
    for name, digest in checksums.items():
        path = BUNDLE / name
        require(path.resolve().is_relative_to(BUNDLE.resolve()), "unsafe artifact path")
        require(not path.is_symlink(), "symlink artifact")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, "digest mismatch: " + name)
    for episode, passed, total in [("baseline", 12, 12), ("v0", 11, 12), ("v1", 11, 12), ("heldout", 3, 6)]:
        result = read("episodes/" + episode + ".json")["results"]
        require((result["passed"], result["total"]) == (passed, total), "score mismatch: " + episode)
    selection = read("trajectory-selection.json")
    require(selection["heldout_rows"] == 0, "held-out data in training selection")
    require(selection["assignments"] == {"training": 10, "validation": 2}, "split mismatch")
    require(selection["selected_counts"] == {"db5f5b51190a4b97-baseline": 12}, "selected source mismatch")
    job = read("training/job-summary.json")
    require(job["status"] == "succeeded", "training did not succeed")
    require(job["trained_tokens"] == 26624, "training token mismatch")
    require(job["fine_tuned_model"] == "ftmodel-2ac55e69-6a3c-4b2d-a3d1-0fd93bf5455a", "checkpoint mismatch")
    require(read("state.json")["status"] == "awaiting_deployment", "deployment status changed")
    print(f"PASS: {len(checksums)} artifact hashes; scores, selection, and training receipts agree.")
    print("Receipt verification only: inference was not rerun; checkpoint quality is not established.")


if __name__ == "__main__":
    main()
