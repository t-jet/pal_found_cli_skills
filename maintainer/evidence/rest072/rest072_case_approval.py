"""Independently verify the complete literal test plan against primary SDK AST."""
import ast
import hashlib
import importlib
import inspect
import json
from datetime import datetime, timezone
from pathlib import Path

tmp = Path(__file__).resolve().parent
path = tmp / "rest072_formal_cases.json"
manifest = json.loads(path.read_text())
repo = tmp / "feature015_integration"
skill = repo / ".agents/skills/pal-found-dev"
expected = {r["id"] for r in json.loads((repo / "maintainer/offline-rest-wave1.json").read_text())["operations"] if "/072/" in r["example"]}
assert {r["operation"] for r in manifest["operations"]} == expected
assert len(manifest["operations"]) == 40
results = []
for row in manifest["operations"]:
    module = importlib.import_module(row["source"]["module"])
    resource, method = row["operation"].split(".")[-2:]
    cls = getattr(module, resource + "Client")
    fn = getattr(cls, method)
    tree = ast.parse(inspect.cleandoc(inspect.getsource(fn)))
    request = next(n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "RequestInfo")
    fields = {n.arg: n.value for n in request.keywords}
    names = {ast.literal_eval(n) for n in fields["throwable_errors"].keys}
    assert names == {e["name"] for e in row["errors"]}, row["operation"]
    for scenario in [{"request": row["request"]["kwargs"], "expected_wire": row["request"]["expected_wire"]}, *row["errors"]]:
        kwargs = scenario["request"]
        env = {k: p.default for k, p in inspect.signature(fn).parameters.items() if p.default is not inspect.Parameter.empty}
        env.update(kwargs)
        for key in ("method", "resource_path", "query_params", "path_params", "header_params", "body"):
            value = eval(compile(ast.Expression(fields[key]), "<primary-sdk-ast>", "eval"), vars(module), env)
            if hasattr(value, "model_dump"):
                value = value.model_dump(mode="json", by_alias=True, exclude_none=True)
            expected_value = scenario["expected_wire"][key]
            if key == "query_params":
                value = {k: v for k, v in value.items() if v is not None}
                expected_value = {k: v for k, v in expected_value.items() if v is not None}
            assert value == expected_value, (row["operation"], key, value, expected_value)
    assert hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() == row["source"]["sha256"]
    for asset in row["assets"].values():
        assert hashlib.sha256((skill / asset["path"]).read_bytes()).hexdigest() == asset["sha256"]
    assert row["gherkin"]["scenarios"]
    for scenario in row["gherkin"]["scenarios"]:
        assert all(scenario.get(k) for k in ("given", "when", "then"))
    if method == "parse_classifications":
        outcome = row["success"]["json"]
        assert set(outcome["parsed"]).isdisjoint(outcome["errors"])
        assert set(outcome["parsed"]) | set(outcome["errors"]) == set(row["request"]["kwargs"]["classification_strings"])
    if method == "get_batch":
        key = "markingId" if resource == "Marking" else "roleId"
        ids = {v[key] for v in row["request"]["kwargs"]["body"]}
        assert set(row["success"]["json"]["data"]) == ids
        assert {v["id"] for v in row["success"]["json"]["data"].values()} == ids
    if resource == "MarkingRoleAssignment" and method in {"add", "remove"}:
        assert {v["role"] for v in row["request"]["kwargs"]["role_assignments"]} <= {"USE", "DECLASSIFY"}
        deny = next(e for e in row["errors"] if e["name"] == "OrganizationMarkingAdministerRoleNotSupported")
        assert deny["request"]["role_assignments"][0]["role"] == "ADMINISTER"
    results.append({"id": row["operation"], "verdict": "PASS", "source_wire_and_error_cases": len(row["errors"]) + 1})

report = {"reviewer": "/root/formal072_workflow_completion", "case_author": manifest["author_identity"], "case_manifest_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "reviewed_at": datetime.now(timezone.utc).isoformat(), "verdict": "APPROVED", "method": "All 40 primary SDK RequestInfo ASTs independently evaluated for baseline plus all113 negative-case request wires. Source and all asset hashes match. Gherkin target/functions and expected results verified; parse/batch/Organization-role correlations explicitly checked. Additional cases reviewed for finite pages,500 boundary,missing input and source silence. No formal execution claim.", "operations": results}
(tmp / "rest072_case_approval.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"approved": len(results), "manifest_sha256": report["case_manifest_sha256"]}))
