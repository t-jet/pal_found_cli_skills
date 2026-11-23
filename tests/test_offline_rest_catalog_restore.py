"""Restore's conflicting SDK declarations must stay visible after generation."""

import ast
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import re
import socket
import tempfile

import foundry_sdk.v2.filesystem.resource as resource_module


ROOT = Path(__file__).resolve().parents[1]
SKILL = Path(".agents/skills/pal-found-dev")
CONTRACT = SKILL / "references/rest/contracts/v2/filesystem/Resource/restore.md"
BEHAVIOR = SKILL / "references/rest/v2/filesystem/Resource.md"


def test_restore_render_preserves_source_and_qualifies_conflicting_purpose(monkeypatch):
    def deny_network(*args, **kwargs):
        raise AssertionError("Operation rendering must remain offline")

    monkeypatch.setattr(socket, "getaddrinfo", deny_network)
    monkeypatch.setattr(socket.socket, "connect", deny_network)
    monkeypatch.setattr(socket.socket, "connect_ex", deny_network)
    spec = importlib.util.spec_from_file_location(
        "restore_catalog", ROOT / "scripts/offline_rest_catalog.py"
    )
    catalog = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(catalog)
    source_bytes = Path(resource_module.__file__).read_bytes()
    source = source_bytes.decode("utf-8")
    tree = ast.parse(source)
    client = next(node for node in tree.body
                  if isinstance(node, ast.ClassDef) and node.name == "ResourceClient")
    register = json.loads((ROOT / "maintainer/rest-contract-register.json").read_text())
    rows = []
    for method_name in ("restore", "delete"):
        identity = f"v2.filesystem.Resource.{method_name}"
        row = dict(next(row for row in register["operations"] if row["id"] == identity))
        assert hashlib.sha256(source_bytes).hexdigest() == row["source_sha256"]
        node = next(node for node in client.body
                    if isinstance(node, ast.FunctionDef) and node.name == method_name)
        request = next(node for node in ast.walk(node)
                       if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                       and node.func.attr == "RequestInfo")
        row.update(version="v2", service="filesystem", resource="Resource", method=method_name,
                   node=node, source="foundry_sdk/v2/filesystem/resource.py",
                   docs="docs/v2/Filesystem/Resource.md", symbols=[],
                   wire={item.arg: ast.unparse(item.value) for item in request.keywords},
                   ordinary_return=ast.unparse(node.returns))
        rows.append(row)
    files = {rows[0]["source"]: source, rows[0]["docs"]: ""}
    temporary_root = ROOT / ".ept/tmp"
    temporary_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=temporary_root) as temporary:
        output = Path(temporary)
        (output / "maintainer").mkdir()
        behavior = output / BEHAVIOR
        behavior.parent.mkdir(parents=True)
        behavior.write_bytes((ROOT / BEHAVIOR).read_bytes())
        catalog.render(output, files, rows, {}, None)
        generated = (output / CONTRACT).read_text(encoding="utf-8")
        restore = rows[0]["node"]
        purpose = inspect.getdoc(resource_module.ResourceClient.restore).split(":param", 1)[0].strip()
        assert "## Purpose and parameter meaning\n\n" + purpose + "\n\n" in generated
        assert f"def restore({ast.unparse(restore.args)}) -> None: ..." in generated
        assert "| ResourceNotDirectlyTrashed | The resource is not directly trashed. |" in generated
        assert "| ResourceNotFound | The given Resource could not be found. |" in generated
        assert "| RestoreResourcePermissionDenied | Could not restore the Resource. |" in generated
        for key, value in rows[0]["wire"].items():
            assert f"**{key}**\n\n```python\n{value}\n```" in generated
        qualifier = generated.split("## SDK source disagreement\n\n", 1)[1].split("\n\n##", 1)[0]
        assert "SDK 1.101.0" in qualifier and "`ResourceNotDirectlyTrashed`" in qualifier
        assert "Live server policy is unverified." in qualifier
        assert "do not establish an active-resource no-op, idempotency" in qualifier
        link = re.search(r"\[restore prerequisites, state checks and bounded reconciliation\]\(([^)]+)\)", qualifier)
        assert link is not None
        target, anchor = link.group(1).split("#")
        assert anchor == "restore"
        linked = (output / CONTRACT).parent / target
        assert linked.resolve() == behavior.resolve()
        assert re.search(r"(?m)^### restore\s*$", linked.read_text(encoding="utf-8"))
        assert "## SDK source disagreement" not in (output / CONTRACT.with_name("delete.md")).read_text()
        published = (ROOT / CONTRACT).read_text(encoding="utf-8")
        model_section = r"## Complete referenced models and errors\n.*?(?=## Identity and execution boundary)"
        assert re.sub(model_section, "", generated, flags=re.S) == re.sub(
            model_section, "", published, flags=re.S
        )
        first = {path.relative_to(output): path.read_bytes()
                 for path in output.rglob("*") if path.is_file()}
        catalog.render(output, files, rows, {}, None)
        assert first == {path.relative_to(output): path.read_bytes()
                         for path in output.rglob("*") if path.is_file()}
