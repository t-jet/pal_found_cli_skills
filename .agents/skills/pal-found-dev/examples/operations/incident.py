"""Classify synthetic production evidence without contacting Foundry."""

from __future__ import annotations

import json
from pathlib import Path


def assess(record: dict) -> dict[str, str]:
    """Return incident cause and next verification from recorded states."""
    if record["consumer_branch"] != record["build_branch"]:
        return {
            "cause": "consumer reads a different branch",
            "next_check": "trace consumer branch and committed output",
        }
    if record["required_input"] != record["build_input"]:
        return {
            "cause": "build used an older input transaction",
            "next_check": "trace branch fallback and rebuild intended input",
        }
    if record["job_status"] != "SUCCEEDED":
        return {
            "cause": "target job failed",
            "next_check": "inspect first failing job and reconcile writes before retry",
        }
    if record["output_transaction"] != record["consumer_transaction"]:
        return {
            "cause": "consumer has not read committed output",
            "next_check": "verify output transaction and downstream refresh",
        }
    if record["check_evaluated_at"] < record["output_committed_at"]:
        return {
            "cause": "health result predates output",
            "next_check": "evaluate check after commit and inspect result",
        }
    if record["check_status"] != "PASS":
        return {
            "cause": "latest health check failed",
            "next_check": "inspect check value and repair business condition",
        }
    return {"cause": "no discrepancy in supplied evidence", "next_check": "verify business rows and next schedule run"}


def main() -> None:
    """Print classifications for bundled synthetic incidents."""
    records = json.loads(Path(__file__).with_name("incidents.json").read_text(encoding="utf-8"))
    for record in records:
        print(json.dumps({"id": record["id"], **assess(record)}, sort_keys=True))


if __name__ == "__main__":
    main()
