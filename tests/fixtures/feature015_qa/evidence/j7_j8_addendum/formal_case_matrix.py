"""Record per-case J7/J8 results from the guarded frozen reader run."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
SNAPSHOT = ROOT / ".ept/tmp/feature015_j7j8_addendum_resume_skill"
RUN = json.loads((HERE / "formal_run_output.json").read_text(encoding="utf-8"))
READER = (HERE.parent / "feature015_j7_j8_reader_results.md").read_text(encoding="utf-8")
ADDENDUM = (HERE / "reader_resume_answer.md").read_text(encoding="utf-8")
OBSERVED = json.loads((HERE / "reader_resume_output.json").read_text(encoding="utf-8"))["cases"]
EXPECTED_MANIFEST = "5cbf2fc67b3bc706262884b40942caf7a345738edb965dfc0a979e3d785b56b8"


def case(name, topic, page, section, data, expected, actual, reader_phrase):
    assert expected == actual, (name, expected, actual)
    assert reader_phrase in READER or reader_phrase in ADDENDUM, (name, reader_phrase)
    content = (SNAPSHOT / page).read_text(encoding="utf-8")
    assert f"## {section}" in content, (name, page, section)
    return {
        "case": name,
        "topic": topic,
        "consulted_local_heading": f"{page}#{section}",
        "reader_trace": reader_phrase,
        "test_data": data,
        "expected": expected,
        "actual": actual,
        "status": "PASS",
        "mode": "guarded synthetic fixture and local reader procedure; no live tenant execution",
    }


def main():
    assert RUN["snapshot_manifest_sha256"] == EXPECTED_MANIFEST
    assert RUN["snapshot_files_verified"] == 4379
    assert RUN["live_tenant_tested"] is False
    assert len(RUN["runs"]) == 4 and all(row["exit_code"] == 0 for row in RUN["runs"])
    assert "fetch, DNS, TCP and UDP entry points denied" in OBSERVED["J7-4"].get("networkProbe", "") or \
        "fetch, DNS, TCP and UDP entry points denied" in json.loads(RUN["runs"][3]["stdout"])["networkProbe"]
    assert hashlib.sha256((HERE / "snapshot_manifest.txt").read_bytes()).hexdigest() == EXPECTED_MANIFEST
    docs = {
        "T20": "references/applications/osdk.md",
        "T21": "references/applications/react.md",
        "T22": "references/widgets/lifecycle.md",
        "T23": "references/widgets/testing.md",
        "T24": "references/widgets/integration.md",
        "T25": "references/widgets/distribution.md",
    }
    required = ["Concept and lifecycle", "Prerequisites", "Procedure", "Worked example",
                "Expected result and checks", "Failures and recovery"]
    for path in docs.values():
        content = (SNAPSHOT / path).read_text(encoding="utf-8")
        assert all(f"## {heading}" in content for heading in required), path

    j74, j75, j84, j85 = (OBSERVED[name] for name in ("J7-4", "J7-5", "J8-4", "J8-5"))
    runs = RUN["runs"]
    rows = [
        case("J7-1", "T20/T21", docs["T21"], "Worked example",
             {"user": "permitted", "page_size": 10},
             {"ui_states": True, "client_query_trace": True},
             {"ui_states": "loading, denied, empty" in runs[0]["stdout"],
              "client_query_trace": "useOsdkObjects(Todo" in READER}, "useOsdkObjects(Todo"),
        case("J7-2", "T20/T21", docs["T20"], "Failures and recovery",
             {"user": "bob", "grant": "read only"},
             {"rows": [{"todoId": "todo-1", "status": "OPEN"}], "action": "ACTION_DENIED"},
             {"rows": j74["bobRows"], "action": j74["deniedAction"]}, "Action denial"),
        case("J7-3", "T21", docs["T21"], "Failures and recovery",
             {"action": "reply lost", "target": "todo-1"},
             {"effect": "RESPONSE_TIMEOUT_EFFECT_UNKNOWN", "reread": [], "action_calls": 1},
             {"effect": j75["lostReply"], "reread": j75["reread"],
              "action_calls": j75["uncertainActionCount"]}, "fetch Todo again"),
        case("J8-1", "T22/T25", docs["T22"], "Expected result and checks",
             {"release": "none", "mode": "playground"},
             {"first_release_required": True, "fixture_has_no_publication": True},
             {"first_release_required": "first published release" in READER,
              "fixture_has_no_publication": "did not render" in READER}, "first published release"),
        case("J8-2", "T23/T24", docs["T23"], "Worked example",
             {"host_count": [0, 5], "event_count": 6, "bad_event": "seven"},
             {"host": 6, "second_widget": 6, "bad_type": "TypeError: invalid host count",
              "unchanged_host": 6},
             {"host": j84["afterEvent"]["reviewCounter"],
              "second_widget": j84["afterEvent"]["reviewSummary"],
              "bad_type": j84["rejectedType"],
              "unchanged_host": j84["afterRejected"]["reviewCounter"]}, "host owns retained state"),
        case("J8-3", "T25", docs["T25"], "Failures and recovery",
             {"host": "1.0.0", "new_release": "1.1.0"},
             {"explicit_selection": True, "prior_version_retained": True},
             {"explicit_selection": "explicit host release selection" in runs[2]["stdout"],
              "prior_version_retained": "pinned to `1.0.0` retain" in READER}, "pinned to `1.0.0` retain"),
        case("J7-4", "T20", docs["T20"], "Prerequisites",
             {"callback": "wrong", "grant": "none", "scopes": "missing read/write"},
             {"callback": "CALLBACK_MISMATCH", "grant": "APPLICATION_GRANT_DENIED",
              "read_scope": "READ_SCOPE_MISSING", "write_scope": "SCOPE_DENIED", "prequery_calls": 0},
             {"callback": j74["loginFailures"]["callback"],
              "grant": j74["loginFailures"]["applicationGrant"],
              "read_scope": j74["loginFailures"]["missingReadScope"],
              "write_scope": j74["loginFailures"]["deniedWriteScope"],
              "prequery_calls": j74["preQueryActionCalls"]}, "CALLBACK_MISMATCH"),
        case("J7-5", "T21", docs["T21"], "Expected result and checks",
             {"initial": "OPEN", "confirmed": "DONE", "preview": "working-tree"},
             {"refreshed": [], "website_release": "1.1.0", "asset": "todo-app.1.1.0.js"},
             {"refreshed": j75["afterConfirmed"], "website_release": j75["deployed"]["version"],
              "asset": j75["deployed"]["asset"]}, "todo-app.1.1.0.js"),
        case("J8-4", "T24", docs["T24"], "Procedure",
             {"host_parameter": [0, 5], "event": 6, "bad": "seven"},
             {"host_0": 0, "host_5": 5, "after_event": 6,
              "second_widget": 6, "bad_preserved": 6},
             {"host_0": j84["host0"]["reviewCounter"],
              "host_5": j84["host5"]["reviewCounter"],
              "after_event": j84["afterEvent"]["reviewCounter"],
              "second_widget": j84["afterEvent"]["reviewSummary"],
              "bad_preserved": j84["afterRejected"]["reviewCounter"]}, "countChanged"),
        case("J8-5", "T25", docs["T25"], "Failures and recovery",
             {"selected": "1.1.0", "verified_prior": "1.0.0"},
             {"selected_release": "1.0.0", "asset": "counter.1.0.0.js", "host_after_event": 7},
             {"selected_release": j85["selectedRelease"], "asset": j85["rollback"]["asset"],
              "host_after_event": j85["rollbackEvent"]["reviewCounter"]}, "counter.1.0.0.js"),
    ]
    evidence = {
        "executed_utc": datetime.now(timezone.utc).isoformat(),
        "snapshot_manifest_sha256": EXPECTED_MANIFEST,
        "snapshot_files_verified": 4379,
        "source_reader_evidence": ["feature015_j7_j8_reader_results.md",
                                   "j7_j8_addendum/reader_resume_answer.md",
                                   "j7_j8_addendum/formal_run_output.json"],
        "topic_docs": docs,
        "cases": rows,
        "live_tenant_tested": False,
    }
    (HERE / "formal_case_results.json").write_bytes((json.dumps(evidence, indent=2) + "\n").encode())
    print(json.dumps({"cases": len(rows), "passed": len(rows), "topics": len(docs)}))


if __name__ == "__main__":
    main()
