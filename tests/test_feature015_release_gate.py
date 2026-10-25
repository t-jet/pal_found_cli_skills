"""Release gate mutations use independent, local files and review records."""

import json
from pathlib import Path
import subprocess
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from verify_feature015_release import (  # noqa: E402
    Report,
    check_candidate_anchor,
    check_models,
    check_operations,
    check_skills,
    check_topics,
    digest,
    input_bundle_digest,
)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def test_review_commit_can_follow_frozen_candidate(tmp_path: Path) -> None:
    git(tmp_path, "init", "-q")
    skill = tmp_path / ".agents/skills/pal-found-dev/SKILL.md"
    write(skill, "# Frozen candidate\n")
    write(tmp_path / "maintainer/rest-contract-register.json", "{}\n")
    git(tmp_path, "add", "-A")
    git(tmp_path, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
        "commit", "-qm", "Freeze content")
    candidate = git(tmp_path, "rev-parse", "HEAD")

    write(tmp_path / "maintainer/rest-domain-authoring-register.json",
          json.dumps({"candidate_sha": candidate}))
    git(tmp_path, "add", "-A")
    git(tmp_path, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
        "commit", "-qm", "Record independent review")
    assert git(tmp_path, "rev-parse", "HEAD") != candidate
    accepted = Report()
    check_candidate_anchor(tmp_path, candidate, accepted)
    assert not accepted.counts

    write(skill, "# Changed after review\n")
    changed = Report()
    check_candidate_anchor(tmp_path, candidate, changed)
    assert changed.counts["candidate_sha"] == 1

    write(skill, "# Frozen candidate\n")
    write(tmp_path / "tests/fixtures/offline/topic-acceptance/prompts.json", "[]\n")
    git(tmp_path, "add", "-A")
    git(tmp_path, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
        "commit", "-qm", "Change topic QA inputs")
    changed_qa = Report()
    check_candidate_anchor(tmp_path, candidate, changed_qa)
    assert changed_qa.counts["candidate_sha"] == 1


def test_operation_gate_rejects_changed_asset_and_missing_candidate(tmp_path: Path) -> None:
    owner = tmp_path / ".agents/skills/pal-found-dev"
    write(owner / "references/rest-api.md", "REST index")
    write(owner / "references/rest/v2/filesystem/Folder.md", "Reviewed behavior")
    write(owner / "examples/rest/get.py", "def verify(): pass\n")
    identity = "v2.filesystem.Folder.get"
    row = {
        "id": identity, "behavior": "references/rest/v2/filesystem/Folder.md",
        "example": "examples/rest/get.py", "fixture_entrypoint": "verify",
        "behavior_sha256": digest(owner / "references/rest/v2/filesystem/Folder.md"),
        "example_sha256": digest(owner / "examples/rest/get.py"),
        "source_sha256": "source", "doc_sha256": "documentation",
        "source_sdk": "1.101.0", "source_commit": "frozen",
        "semantic_review_status": "accepted", "independent_qa_status": "accepted",
        "fixture_status": "passed", "author": "author", "author_agent": "author-agent",
        "independent_reviewer": "reviewer", "reviewer_agent": "review-agent",
        "independent_qa_agent": "qa-agent",
    }
    contract = {"operation_count": 1, "sdk_release": "1.101.0", "source_commit": "frozen",
                "operations": [{"id": identity}]}
    oracle = {"sdk_release": "1.101.0", "source_commit": "frozen",
              "operations": {identity: {"source_sha256": "source", "documentation": {"doc_sha256": "documentation"}}}}
    candidate = "a" * 40
    domain = {"operations": [row], "candidate_sha": candidate,
              "input_bundle_sha256": input_bundle_digest(owner)}
    clean = Report()
    check_operations(tmp_path, contract, domain, oracle, clean, candidate)
    assert not (set(clean.counts) & {"candidate_sha", "input_bundle_sha256", "operation_asset_hashes"})

    write(owner / "examples/rest/get.py", "def verify(): return 'changed'\n")
    changed = Report()
    check_operations(tmp_path, contract, domain, oracle, changed, candidate)
    assert changed.counts["operation_asset_hashes"] == 1
    assert changed.counts["input_bundle_sha256"] == 1

    domain.pop("candidate_sha")
    missing = Report()
    check_operations(tmp_path, contract, domain, oracle, missing, candidate)
    assert missing.counts["candidate_sha"] == 1


def test_model_gate_rejects_changed_page_even_when_review_says_pass(tmp_path: Path) -> None:
    owner = tmp_path / ".agents/skills/pal-found-dev"
    page = owner / "references/rest/models/example.md"
    write(page, "Reviewed model meaning")
    identity = "foundry_sdk.v2.example.models.Example"
    relative = "references/rest/models/example.md"
    register = {"sdk_release": "1.101.0", "source_commit": "frozen",
        "candidate_symbol_count": 1, "symbols": [{"id": identity,
        "source_sha256": "source", "definition_sha256": "definition",
        "semantic_review_status": "accepted"}]}
    matrix = {"sdk_release": "1.101.0", "source_commit": "frozen",
        "symbol_count": 1, "symbols": [{"id": identity,
        "source_file_sha256": "source", "source_definition_sha256": "definition",
        "reader_prose_sha256": "meaning", "local_pages": [relative],
        "local_page_sha256": [digest(page)],
        "source_fidelity_review": "PASS", "local_meaning_review": "PASS"}]}
    review = {"source_commit": "frozen", "counts": {"symbols": 1}, "symbols": [{"id": identity,
        "reviewed_source_definition_sha256": "definition",
        "reviewed_reader_prose_sha256": "meaning",
        "reviewed_local_page_sha256": [digest(page)],
        "source_fidelity_review": "PASS", "local_meaning_review": "PASS",
        "semantic_review_evidence": "Reviewer compared source and summary", "issues": []}]}
    for name, document, field in (("rest-model-register", register, "register_sha256"),
                                  ("rest-model-semantic-matrix", matrix, "matrix_sha256")):
        path = tmp_path / "maintainer" / f"{name}.json"
        write(path, json.dumps(document))
        review[field] = digest(path)
    clean = Report()
    check_models(tmp_path, register, matrix, review, clean)
    assert not (set(clean.counts) & {"model_page_hashes", "model_review_ledger_hashes", "model_independent_meaning_pending"})

    write(page, "Changed after review")
    changed = Report()
    check_models(tmp_path, register, matrix, review, changed)
    assert changed.counts["model_page_hashes"] == 1

    review["symbols"][0]["local_meaning_review"] = "pending"
    pending = Report()
    check_models(tmp_path, register, matrix, review, pending)
    assert pending.counts["model_independent_meaning_pending"] == 1


def test_topic_and_skill_gate_detect_missing_inventory(tmp_path: Path) -> None:
    owner = tmp_path / ".agents/skills"
    for index in range(20):
        write(owner / f"pal-found-{index:02d}/SKILL.md", "# Skill\n")
    audit = {"scope": {"skills": 20, "markdown_files": 20}, "status": "accepted",
             "independent_reviewer": "reviewer",
             "files": [{"path": f"pal-found-{index:02d}/SKILL.md",
                        "sha256": digest(owner / f"pal-found-{index:02d}/SKILL.md"),
                        "review_status": "accepted", "review_evidence": "Compared source and local guide"}
                       for index in range(20)]}
    clean = Report()
    check_skills(tmp_path, audit, clean)
    assert not clean.counts
    (owner / "pal-found-00/SKILL.md").unlink()
    changed = Report()
    check_skills(tmp_path, audit, changed)
    assert changed.counts["skill_inventory_gaps"] == 1
    assert changed.counts["skill_asset_hashes"] == 1

    audit["files"][0].pop("review_evidence")
    evidence_missing = Report()
    check_skills(tmp_path, audit, evidence_missing)
    assert evidence_missing.counts["skill_review_provenance"] == 1

    topic = {"status": "accepted", "topics": [{"topic": "T01", "authored": False,
               "acceptance": "pending independent topic/source and semantic review"}]}
    missing = Report()
    check_topics(tmp_path, topic, missing)
    assert missing.counts["topic_inventory_gaps"] >= 1

    write(owner / "pal-found-dev/references/topic.md", "# Topic\n")
    topic = {"author": "writer", "independent_reviewer": "reviewer", "status": "accepted",
             "topics": [{"topic": "T01", "authored": True, "acceptance": "accepted",
                         "registered_path": "references/topic.md", "registered_heading": "Topic",
                         "sha256": digest(owner / "pal-found-dev/references/topic.md")}]}
    no_evidence = Report()
    check_topics(tmp_path, topic, no_evidence)
    assert no_evidence.counts["topic_review_provenance"] == 1
