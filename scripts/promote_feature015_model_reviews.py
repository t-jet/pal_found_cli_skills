"""Sync model acceptance ledgers from independent, per-symbol review evidence."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MAINTAINER = ROOT / "maintainer"
SKILL = ROOT / ".agents" / "skills" / "pal-found-dev"


def load(name: str) -> tuple[Path, dict, bytes]:
    path = MAINTAINER / f"{name}.json"
    raw = path.read_bytes()
    return path, json.loads(raw), b"\r\n" if raw.count(b"\r\n") == raw.count(b"\n") else b"\n"


def write(path: Path, value: dict, newline: bytes) -> None:
    raw = (json.dumps(value, indent=2, ensure_ascii=True) + "\n").encode()
    path.write_bytes(raw.replace(b"\n", newline))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reconcile() -> tuple[int, int]:
    register_path, register, register_newline = load("rest-model-register")
    matrix_path, matrix, matrix_newline = load("rest-model-semantic-matrix")
    review_path, review, review_newline = load("rest-model-independent-review")

    registered = {row["id"]: row for row in register["symbols"]}
    mapped = {row["id"]: row for row in matrix["symbols"]}
    reviewed = {row["id"]: row for row in review["symbols"]}
    if (len(registered), len(mapped), len(reviewed)) != (3251, 3251, 3251):
        raise ValueError("model inventories must contain exactly 3251 unique symbols")
    if registered.keys() != mapped.keys() or mapped.keys() != reviewed.keys():
        raise ValueError("model inventories have different symbol IDs")

    source_pass = 0
    meaning_pass = 0
    for identity, row in mapped.items():
        reg = registered[identity]
        rev = reviewed[identity]
        source_valid = (
            rev["source_fidelity_review"] == "PASS"
            and reg["source_sha256"] == row["source_file_sha256"]
            and reg["definition_sha256"] == row["source_definition_sha256"]
            and rev["reviewed_source_definition_sha256"] == row["source_definition_sha256"]
        )
        row["source_fidelity_review"] = "PASS" if source_valid else "pending_independent_review"
        source_pass += source_valid

        page_valid = (
            row["local_page_sha256"] == rev["reviewed_local_page_sha256"]
            and len(row["local_pages"]) == len(row["local_page_sha256"])
            and all(digest(SKILL / path) == expected for path, expected in
                    zip(row["local_pages"], row["local_page_sha256"]))
        )
        meaning_valid = (
            source_valid and page_valid and rev["local_meaning_review"] == "PASS"
            and bool(rev.get("semantic_review_evidence")) and not rev.get("issues")
            and rev["reviewed_reader_prose_sha256"] == row["reader_prose_sha256"]
        )
        row["local_meaning_review"] = "PASS" if meaning_valid else "pending_independent_review"
        reg["semantic_review_status"] = "accepted" if meaning_valid else "unreviewed"
        meaning_pass += meaning_valid

    matrix["source_fidelity_review"] = "PASS" if source_pass == 3251 else "pending_independent_review"
    matrix["local_meaning_review"] = "PASS" if meaning_pass == 3251 else "pending_independent_review"
    register["independent_closure_status"] = "accepted" if meaning_pass == 3251 else "pending"
    statuses = Counter(row["local_meaning_review"] for row in review["symbols"])
    review["counts"] = {
        "symbols": 3251,
        "source_pass": sum(row["source_fidelity_review"] == "PASS" for row in review["symbols"]),
        "source_fail": sum(row["source_fidelity_review"] == "FAIL" for row in review["symbols"]),
        "local_meaning_fail": statuses["FAIL"],
        "local_meaning_pass": statuses["PASS"],
        "local_meaning_pending": 3251 - statuses["PASS"] - statuses["FAIL"],
    }

    write(register_path, register, register_newline)
    write(matrix_path, matrix, matrix_newline)
    review["register_sha256"] = digest(register_path)
    review["matrix_sha256"] = digest(matrix_path)
    write(review_path, review, review_newline)
    return source_pass, meaning_pass


if __name__ == "__main__":
    source, meaning = reconcile()
    print(f"Model review synced: {source}/3251 source, {meaning}/3251 meaning accepted")
