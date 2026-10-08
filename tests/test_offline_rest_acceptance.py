"""Independent REST source checks and bounded, network-denied fixture execution."""

import ast
from datetime import datetime, timezone
import hashlib
from contextlib import contextmanager
import importlib
import importlib.metadata
import inspect
import json
from pathlib import Path
import re
import runpy
import socket
import subprocess
import typing_extensions
import httpx
import urllib.request
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent
SOURCE_ORACLE = ROOT / "tests/fixtures/offline/rest-acceptance/source-oracle.json"
EXPECTED_RELEASE = "1.101.0"
EXPECTED_COMMIT = "168d51910570b6966afa2320333ab36f6a3f7ccf"


def verify_domain_acceptance(oracle: dict, register: dict, owner: Path,
                             candidate_sha: str) -> None:
    """Reject incomplete, self-reviewed or stale behavioral acceptance evidence."""
    assert re.fullmatch(r"[0-9a-f]{40}", candidate_sha), "Invalid candidate SHA"
    if "candidate_sha" in register:
        assert register["candidate_sha"] == candidate_sha, "Stale domain acceptance candidate"
    assert register.get("input_bundle_sha256") == rest_input_bundle_sha256(owner), "Changed domain acceptance input bundle"
    records = register["operations"]
    by_id = {row["id"]: row for row in records}
    assert len(records) == len(by_id), "Duplicate domain operation evidence"
    assert by_id.keys() == oracle["operations"].keys(), "Incomplete behavioral operation closure"
    for identity, row in by_id.items():
        assert row["source_sdk"] == EXPECTED_RELEASE and row["source_commit"] == EXPECTED_COMMIT, identity
        assert row.get("independent_reviewer") and row["independent_reviewer"] != row["author"], f"{identity}: self-review"
        assert row.get("author_agent") and row.get("reviewer_agent") != row["author_agent"], f"{identity}: missing or same-agent review"
        assert row.get("independent_qa_agent") and row["independent_qa_agent"] != row["author_agent"], f"{identity}: missing or same-agent QA"
        assert row.get("semantic_review_status") == "accepted", f"{identity}: semantic review pending"
        assert row.get("independent_qa_status") == "accepted", f"{identity}: independent QA pending"
        assert row.get("fixture_status") == "passed", f"{identity}: fixture execution pending"
        source = oracle["operations"][identity]
        assert row.get("source_sha256") == source["source_sha256"], f"{identity}: changed source"
        assert row.get("doc_sha256") == source["documentation"]["doc_sha256"], f"{identity}: changed source documentation"
        assert row.get("fixture_entrypoint"), f"{identity}: missing runnable entrypoint"
        for field in ("behavior", "example"):
            path = (owner / row[field]).resolve()
            assert path.is_relative_to(owner.resolve()) and path.is_file(), f"{identity}: missing/escaped {field}"
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            assert digest == row[field + "_sha256"], f"{identity}: changed accepted {field}"


def rest_input_bundle_sha256(owner: Path) -> str:
    """Hash distributed REST knowledge and assets, excluding review bookkeeping."""
    files = [owner / "references/rest-api.md"]
    for directory in ["references/rest", "examples/rest", "assets/rest"]:
        files.extend(p for p in (owner / directory).rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    entries = [
        f"{p.relative_to(owner).as_posix()}:{hashlib.sha256(p.read_bytes()).hexdigest()}"
        for p in sorted(set(files)) if p.is_file()
    ]
    return hashlib.sha256(("\n".join(entries) + "\n").encode()).hexdigest()


def documented_operation_ids(files: dict[str, bytes]) -> dict[str, dict]:
    """Use resource documentation tables as the independent identity oracle."""
    import foundry_sdk
    namespaces = {
        "".join(service.name.split("_")).lower(): service.name
        for version in ("v1", "v2")
        for service in (Path(foundry_sdk.__file__).parent / version).iterdir()
        if service.is_dir()
    }
    records = {}
    for name, content in files.items():
        parts = Path(name).parts
        if len(parts) != 4 or parts[0] != "docs" or parts[1] not in {"v1", "v2"}:
            continue
        service = namespaces.get(parts[2].lower())
        if service is None or not name.endswith(".md"):
            continue
        resource = Path(name).stem
        for line in content.decode().splitlines():
            match = re.match(r"\[\*\*(\w+)\*\*\]\([^)]*\)\s*\|\s*\*\*(\w+)\*\*\s+(\S+)\s*\|\s*([^|]+)", line)
            if not match:
                continue
            operation, verb, path, stage = match.groups()
            key = f"{parts[1]}.{service}.{resource}.{operation}"
            assert key not in records, f"Duplicate source documentation identity: {key}"
            records[key] = {"method": verb, "resource_path": path, "stage": stage.strip(), "doc_sha256": hashlib.sha256(content).hexdigest()}
    return records


def source_method_contracts(source: str, resource: str) -> dict[str, dict]:
    """Capture every actual SDK form, including direct async iterator returns."""
    tree = ast.parse(source)
    result: dict[str, dict] = {}
    for cls in tree.body:
        if not isinstance(cls, ast.ClassDef):
            continue
        if resource not in cls.name:
            continue
        if cls.name == resource + "Client":
            mode = "ordinary"
        elif cls.name == "Async" + resource + "Client":
            mode = "async"
        elif "Streaming" in cls.name:
            mode = "async_stream" if "Async" in cls.name else "stream"
        elif "Raw" in cls.name:
            mode = "async_raw" if "Async" in cls.name else "raw"
        else:
            continue
        for method in cls.body:
            if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) or method.name.startswith("_"):
                continue
            row = result.setdefault(method.name, {})
            row[mode] = {
                "signature": ast.unparse(method.args),
                "return": ast.unparse(method.returns) if method.returns else "None",
                "coroutine_definition": isinstance(method, ast.AsyncFunctionDef),
            }
            if mode == "ordinary":
                request = next((
                    n for n in ast.walk(method)
                    if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                    and n.func.attr == "RequestInfo"
                ), None)
                if request:
                    row["wire"] = {k.arg: ast.unparse(k.value) for k in request.keywords}
    wrappers = source_wrapper_contracts(source, resource)
    for operation, row in result.items():
        if "ordinary" in row:
            row["wrappers"] = wrappers.get(operation, {})
    return result


def source_wrapper_contracts(source: str, resource: str) -> dict[str, dict]:
    """Read actual constructor assignments; nested stubs carry payload types."""
    modes = {
        "_" + resource + "ClientRaw": "raw",
        "_" + resource + "ClientStreaming": "stream",
        "_Async" + resource + "ClientRaw": "async_raw",
        "_Async" + resource + "ClientStreaming": "async_stream",
    }
    result = {}
    for cls in ast.parse(source).body:
        if not isinstance(cls, ast.ClassDef) or cls.name not in modes:
            continue
        constructor = next(node for node in cls.body
                           if isinstance(node, ast.FunctionDef) and node.name == "__init__")
        stubs = {node.name: node for node in constructor.body if isinstance(node, ast.FunctionDef)}
        for node in constructor.body:
            if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Call):
                continue
            target = node.targets[0]
            if not isinstance(target, ast.Attribute) or not isinstance(target.value, ast.Name) or target.value.id != "self":
                continue
            call = node.value
            assert isinstance(call.func, ast.Attribute) and isinstance(call.args[0], ast.Name)
            stub = stubs[call.args[0].id]
            assert len(stub.args.args) == 1 and stub.args.args[0].annotation is not None
            result.setdefault(target.attr, {})[modes[cls.name]] = {
                "class": cls.name, "helper": call.func.attr,
                "payload": ast.unparse(stub.args.args[0].annotation),
            }
    return result


def verify_operation_register(oracle: dict, register: dict) -> None:
    assert register["sdk_release"] == EXPECTED_RELEASE
    assert register["source_commit"] == EXPECTED_COMMIT
    expected = oracle["operations"]
    actual = {row["id"]: row for row in register["operations"]}
    assert len(actual) == len(register["operations"]), "Duplicate operation ownership"
    assert actual.keys() == expected.keys(), (
        f"Identity mismatch: missing={expected.keys() - actual.keys()}, extra={actual.keys() - expected.keys()}"
    )
    for key, source in expected.items():
        row = actual[key]
        assert row["stage"] == source["documentation"]["stage"], key
        assert row["signature"] == source["ordinary"]["signature"], f"{key}: signature mismatch"
        assert row["ordinary_return"] == source["ordinary"]["return"], f"{key}: ordinary return mismatch"
        assert row["async_return"] == source["async"]["return"], f"{key}: async return mismatch"
        assert row["wire"] == source["wire"], f"{key}: serialized request contract mismatch"


def verified_runtime_method(operation_id: str, source_module: str):
    """Resolve a concrete resource module, not an invented client.v1 property."""
    version, service, resource, method = operation_id.split(".")
    assert source_module.startswith(f"foundry_sdk.{version}.{service}.")
    module = importlib.import_module(source_module)
    client = getattr(module, resource + "Client")
    return getattr(client, method), module


def assert_runtime_signature(operation_id: str, expected: dict) -> None:
    method, module = verified_runtime_method(operation_id, expected["module"])
    assert_signature_contract(operation_id, method, expected["ordinary"], vars(module))
    resource = operation_id.split(".")[2]
    operation = operation_id.split(".")[3]
    for name, cls in vars(module).items():
        if not inspect.isclass(cls) or resource not in name or not hasattr(cls, operation):
            continue
        mode = (
            "async" if name == "Async" + resource + "Client"
            else "async_stream" if "Async" in name and "Streaming" in name
            else "stream" if "Streaming" in name
            else "async_raw" if "Async" in name and "Raw" in name
            else "raw" if "Raw" in name else None
        )
        if mode and mode in expected:
            assert_signature_contract(operation_id + "/" + mode, getattr(cls, operation), expected[mode], vars(module))
    # Constructor-built partials have no public methods on their class itself.
    # Build wrappers around an uninitialized real resource; no HTTP client needed.
    for mode, prefix, suffix in [("raw", "_", "Raw"), ("stream", "_", "Streaming"),
                                  ("async_raw", "_Async", "Raw"), ("async_stream", "_Async", "Streaming")]:
        cls = getattr(module, prefix + resource + "Client" + suffix)
        ordinary_cls = getattr(module, ("Async" if mode.startswith("async") else "") + resource + "Client")
        wrapper = cls(ordinary_cls.__new__(ordinary_cls))
        binding = expected["wrappers"].get(mode)
        assert hasattr(wrapper, operation) == (binding is not None), f"{operation_id}/{mode}: availability differs"
        if binding is not None:
            partial = getattr(wrapper, operation)
            assert partial.func.__func__ is getattr(ordinary_cls, operation), operation_id
            configured = partial.keywords["_sdk_internal"]["response_mode"]
            helper = binding["helper"]
            assert configured == ("SSE" if "sse" in helper else "STREAMING" if "streaming" in helper else "RAW"), operation_id


def verify_prepared_source_files(records: list[dict]) -> int:
    """Check complete prepared module bytes against the frozen source snapshot."""
    checked = set()
    for record in records:
        module = record["module"]
        if module in checked:
            continue
        path = Path(importlib.import_module(module).__file__)
        content = path.read_bytes().replace(b"\r\n", b"\n")
        assert hashlib.sha256(content).hexdigest() == record["source_sha256"], f"{module}: prepared source differs from frozen commit"
        checked.add(module)
    return len(checked)


def assert_signature_contract(label: str, method, expected: dict, namespace: dict) -> None:
    """Check requiredness, defaults and every actual runtime mode independently."""
    signature = inspect.signature(method)
    source = ast.parse("def call(" + expected["signature"] + "): pass").body[0]
    names = [arg.arg for arg in source.args.posonlyargs + source.args.args + source.args.kwonlyargs]
    assert list(signature.parameters) == names, f"{label}: runtime parameter mismatch"
    assert inspect.iscoroutinefunction(method) == expected["coroutine_definition"], label
    source_return = eval(expected["return"], namespace)
    assert str(signature.return_annotation) == str(source_return), (
        f"{label}: runtime return annotation mismatch"
    )
    positional = source.args.posonlyargs + source.args.args
    defaults = dict(zip([a.arg for a in positional][-len(source.args.defaults):], source.args.defaults)) if source.args.defaults else {}
    defaults.update({arg.arg: value for arg, value in zip(source.args.kwonlyargs, source.args.kw_defaults) if value is not None})
    for arg in source.args.posonlyargs + source.args.args + source.args.kwonlyargs:
        parameter = signature.parameters[arg.arg]
        kind = (
            inspect.Parameter.POSITIONAL_ONLY if arg in source.args.posonlyargs
            else inspect.Parameter.KEYWORD_ONLY if arg in source.args.kwonlyargs
            else inspect.Parameter.POSITIONAL_OR_KEYWORD
        )
        assert parameter.kind == kind, f"{label}/{arg.arg}: parameter kind mismatch"
        default = eval(ast.unparse(defaults[arg.arg]), namespace) if arg.arg in defaults else inspect.Parameter.empty
        assert parameter.default == default, f"{label}/{arg.arg}: default/requiredness mismatch"
        if arg.annotation is not None:
            source_type = eval(ast.unparse(arg.annotation), namespace)
            assert str(parameter.annotation) == str(source_type), (
                f"{label}/{arg.arg}: runtime type mismatch"
            )


@contextmanager
def denied_public_network():
    """Deny public sockets in this Python process and reject child-process escape."""
    def deny(*args, **kwargs):
        raise RuntimeError("Public network unavailable in isolated fixture process")

    with (
        patch.object(socket, "getaddrinfo", deny),
        patch.object(socket, "create_connection", deny),
        patch.object(socket.socket, "connect", deny),
        patch.object(socket.socket, "connect_ex", deny),
        patch.object(httpx.HTTPTransport, "handle_request", deny),
        patch.object(httpx.AsyncHTTPTransport, "handle_async_request", deny),
        patch.object(urllib.request, "urlopen", deny),
        patch.object(subprocess, "Popen", deny),
    ):
        yield


def no_public_network_probe() -> None:
    with denied_public_network():
        try:
            socket.create_connection(("www.palantir.com", 443), timeout=1)
        except RuntimeError as error:
            assert "Public network unavailable" in str(error)
        else:
            raise AssertionError("External socket was not denied")
        try:
            with httpx.Client(timeout=1, trust_env=False) as client:
                client.get("https://www.palantir.com/")
        except RuntimeError as error:
            assert "Public network unavailable" in str(error)
        else:
            raise AssertionError("Real HTTP dispatch was not denied")


def reconcile_symbol_definitions(expected: dict, actual: dict) -> None:
    """Require the corrected closure and exact field/schema evidence, not a cap."""
    assert expected.keys() == actual.keys(), (
        f"Unresolved symbol closure: missing={expected.keys() - actual.keys()}, extra={actual.keys() - expected.keys()}"
    )
    for symbol, definition in expected.items():
        assert actual[symbol] == definition, f"{symbol}: field/default/constraint/source mismatch"


def reader_symbol_definitions(folder: Path) -> dict[str, str]:
    """Reassemble reader code blocks, then compare syntax trees with source."""
    result = {}
    for path in folder.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        title = text.splitlines()[0].removeprefix("# ")
        if not title.startswith("foundry_sdk.") or " part " in title.lower():
            continue
        if title.startswith("foundry_sdk._core.") and title.count(".") == 2:
            name = title.rpartition(".")[2]
            module = (
                "api_client" if name in {"SdkInternal", "ResponseMode"}
                else "model_base" if name == "ModelBase"
                else "config" if name == "Config" else "utils"
            )
            title = f"foundry_sdk._core.{module}.{name}"
        parts = [path]
        for relative in re.findall(r"\[Part \d+\]\(([^)]+)\)", text):
            candidate = path.parent / relative
            if candidate not in parts:
                parts.append(candidate)
        code = "\n".join(
            block
            for part in parts
            for block in re.findall(r"```python\s*\n(.*?)\n```", part.read_text(encoding="utf-8"), re.S)
        )
        assert code, f"{title}: missing source definition"
        tree = ast.parse(code)
        assert title not in result, f"Duplicate reader symbol {title}"
        result[title] = ast.dump(tree, include_attributes=False)
    return result


def verify_reader_definitions(oracle: dict, actual: dict[str, str]) -> None:
    expected = {
        symbol: ast.dump(ast.parse(record["definition"]), include_attributes=False)
        for symbol, record in oracle["symbols"].items()
    }
    reconcile_symbol_definitions(expected, actual)


def verify_reader_field_tables(oracle: dict, folder: Path) -> tuple[int, int]:
    """Check prose tables against runtime omission/aliases and source annotations."""
    models, fields = 0, 0
    for symbol, record in oracle["symbols"].items():
        node = ast.parse(record["definition"]).body[0]
        if not isinstance(node, ast.ClassDef):
            continue
        members = [n for n in node.body if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name)]
        if not members:
            continue
        relative = (
            Path("_core") / (node.name + ".md") if symbol.startswith("foundry_sdk._core.")
            else Path(*symbol.split(".")[1:-1]) / (node.name + ".md")
        )
        text = (folder / relative).read_text(encoding="utf-8")
        parts = [folder / relative]
        for link in re.findall(r"\[Part \d+\]\(([^)]+)\)", text):
            path = parts[0].parent / link
            if path not in parts:
                parts.append(path)
        rows = {}
        for part in parts:
            for line in part.read_text(encoding="utf-8").splitlines():
                cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line)]
                if len(cells) == 7 and cells[1] in {n.target.id for n in members}:
                    assert cells[1] not in rows, f"{symbol}: duplicate table field"
                    rows[cells[1]] = cells[2:6]
        assert rows.keys() == {n.target.id for n in members}, f"{symbol}: table fields missing or extra"
        runtime = getattr(importlib.import_module(record["module"]), node.name)
        for index, member in enumerate(members):
            name = member.target.id
            alias, annotation, omission, meaning = rows[name]
            assert annotation == ast.unparse(member.annotation), f"{symbol}/{name}: prose type mismatch"
            if hasattr(runtime, "model_fields"):
                field = runtime.model_fields[name]
                assert alias == (field.alias or name), f"{symbol}/{name}: wire alias mismatch"
                assert (omission == "required; no default") == field.is_required(), f"{symbol}/{name}: Pydantic omission mismatch"
            elif typing_extensions.is_typeddict(runtime):
                assert alias == name, f"{symbol}/{name}: TypedDict alias invented"
                assert (omission == "TypedDict key required") == (name in runtime.__required_keys__), f"{symbol}/{name}: TypedDict omission mismatch"
            following = node.body[node.body.index(member) + 1:][:1]
            if following and isinstance(following[0], ast.Expr) and isinstance(following[0].value, ast.Constant) and isinstance(following[0].value.value, str):
                source_description = following[0].value.value
                normalize = lambda value: " ".join(value.replace("<br>", " ").split())
                assert normalize(meaning) == normalize(source_description), f"{symbol}/{name}: field meaning omitted or changed"
            fields += 1
        models += 1
    return models, fields


def source_symbol_closure(files: dict[str, bytes]) -> tuple[dict, set[str]]:
    """Resolve module re-exports and parsed forward expressions independently."""
    definitions, imports, trees = {}, {}, {}
    core_types = {
        "foundry_sdk._core.utils": {"RID", "UUID", "Long", "AwareDatetime", "Timeout"},
        "foundry_sdk._core.model_base": {"ModelBase"},
        "foundry_sdk._core.api_client": {"SdkInternal", "ResponseMode"},
        "foundry_sdk._core.config": {"Config"},
    }
    for path, data in files.items():
        if not path.startswith("foundry_sdk/") or not path.endswith(".py"):
            continue
        module = path[:-3].replace("/", ".").removesuffix(".__init__")
        tree = ast.parse(data)
        trees[module] = tree
        aliases = {}
        for node in tree.body:
            if isinstance(node, ast.ImportFrom):
                package = module if path.endswith("/__init__.py") else module.rsplit(".", 1)[0]
                base = node.module or ""
                if node.level:
                    from importlib.util import resolve_name
                    base = resolve_name("." * node.level + base, package)
                for item in node.names:
                    aliases[item.asname or item.name] = base + "." + item.name
            elif isinstance(node, ast.Import):
                for item in node.names:
                    aliases[item.asname or item.name] = item.name
        imports[module] = aliases
        datatype = ".models" in module or ".errors" in module
        for node in tree.body:
            names = (
                [node.name] if isinstance(node, ast.ClassDef)
                else [n.id for n in node.targets if isinstance(n, ast.Name)] if isinstance(node, ast.Assign)
                else [node.target.id] if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name)
                else []
            )
            for name in names:
                if datatype or name in core_types.get(module, set()):
                    definitions[module + "." + name] = (module, node, path)

    def resolve(name: str, visited=frozenset()) -> str:
        if name in visited or name in definitions:
            return name
        parent, _, symbol = name.rpartition(".")
        target = imports.get(parent, {}).get(symbol)
        return resolve(target, visited | {name}) if target else name

    runtime_types: set[str] = set()
    def references(node: ast.AST, module: str, parse_strings=True) -> set[str]:
        result = set()
        for part in ast.walk(node):
            dotted = None
            if isinstance(part, (ast.Name, ast.Attribute)):
                expression = ast.unparse(part)
                first, _, rest = expression.partition(".")
                base = imports.get(module, {}).get(first, module + "." + first)
                dotted = base + ("." + rest if rest else "")
            elif parse_strings and isinstance(part, ast.Constant) and isinstance(part.value, str):
                try:
                    expression = ast.parse(part.value, mode="eval")
                except (SyntaxError, ValueError):
                    continue
                result |= references(expression, module, parse_strings=False)
            if dotted is not None:
                candidate = resolve(dotted)
                if candidate in definitions:
                    result.add(candidate)
                elif candidate.startswith("foundry_sdk._core.") and (
                    candidate.rpartition(".")[2] in imports.get(candidate.rpartition(".")[0], {})
                    or any(
                        isinstance(top, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
                        and top.name == candidate.rpartition(".")[2]
                        for top in trees.get(candidate.rpartition(".")[0], ast.Module(body=[])).body
                    )
                ):
                    runtime_types.add(candidate)
        return result

    # Config is a constructor prerequisite, independently rooted in the SDK's
    # public client signature rather than an operation response model.
    roots = {"foundry_sdk._core.config.Config"}
    for module, tree in trees.items():
        bits = module.split(".")
        if len(bits) != 4 or bits[1] not in {"v1", "v2"}:
            continue
        for cls in tree.body:
            if not isinstance(cls, ast.ClassDef) or not cls.name.endswith("Client") or cls.name.startswith(("_", "Async")):
                continue
            for method in cls.body:
                if not isinstance(method, ast.FunctionDef) or method.name.startswith("_"):
                    continue
                request = next((
                    n for n in ast.walk(method) if isinstance(n, ast.Call)
                    and isinstance(n.func, ast.Attribute) and n.func.attr == "RequestInfo"
                ), None)
                if request is None:
                    continue
                roots |= references(method.args, module)
                if method.returns:
                    roots |= references(method.returns, module)
                for keyword in request.keywords:
                    if keyword.arg in {"body", "response_type", "throwable_errors"}:
                        roots |= references(keyword.value, module)
    closure, pending = {}, list(roots)
    while pending:
        symbol = pending.pop()
        if symbol in closure:
            continue
        module, definition, path = definitions[symbol]
        dependencies = references(definition, module) - {symbol}
        closure[symbol] = {
            "module": module, "path": path,
            "definition": ast.unparse(definition),
            "dependencies": sorted(dependencies),
        }
        pending.extend(dependencies - closure.keys())
    return dict(sorted(closure.items())), runtime_types


def test_prepared_sdk_matches_frozen_release() -> None:
    assert importlib.metadata.version("foundry-platform-sdk") == EXPECTED_RELEASE


def test_paged_and_nonpaged_reader_contracts_match_sdk_responses() -> None:
    fixture = ROOT / "tests/fixtures/feature015_qa/paging_modes.py"
    runpy.run_path(str(fixture))["run"]()


def test_public_connection_probe_is_denied() -> None:
    no_public_network_probe()


def test_all_operation_contracts_match_independent_source_oracle() -> None:
    oracle = json.loads(SOURCE_ORACLE.read_text(encoding="utf-8"))
    register = json.loads((ROOT / "maintainer/rest-contract-register.json").read_text(encoding="utf-8"))
    verify_operation_register(oracle, register)
    verify_prepared_source_files(list(oracle["operations"].values()))
    for key, source in oracle["operations"].items():
        assert_runtime_signature(key, source)


def test_all_reader_models_match_independent_source_oracle() -> None:
    oracle = json.loads((SOURCE_ORACLE.parent / "model-source-oracle.json").read_text(encoding="utf-8"))
    folder = ROOT / ".agents/skills/pal-found-dev/references/rest/models"
    verify_reader_definitions(oracle, reader_symbol_definitions(folder))
    verify_reader_field_tables(oracle, folder)
    verify_prepared_source_files(list(oracle["symbols"].values()))


def test_prepared_core_constraints_and_json_serialization() -> None:
    """Exercise validators/serialization that syntax preservation alone cannot prove."""
    from foundry_sdk._core import AwareDatetime, Long, ModelBase, RID, Timeout, UUID
    from pydantic import Field, TypeAdapter, ValidationError

    for annotation, invalid in [(RID, "not-a-rid"), (UUID, "not-a-uuid"), (Timeout, 0), (AwareDatetime, datetime(2026, 1, 1))]:
        try:
            TypeAdapter(annotation).validate_python(invalid)
        except ValidationError:
            pass
        else:
            raise AssertionError(f"Missing SDK constraint on {annotation}")
    assert TypeAdapter(Long).dump_json(42) == b'"42"'
    assert TypeAdapter(AwareDatetime).dump_json(datetime(2026, 1, 1, tzinfo=timezone.utc)) == b'"2026-01-01T00:00:00+00:00"'

    class Example(ModelBase):
        nullable_required: str | None = Field(alias="nullableRequired")
        omitted: str | None = None

    try:
        Example()
    except ValidationError:
        pass
    else:
        raise AssertionError("Nullable field without default incorrectly became omittable")
    example = Example(nullableRequired=None, additional="preserved")
    assert example.to_dict() == {"additional": "preserved"}
    populated_by_name = Example(nullable_required="value")
    assert populated_by_name.to_dict() == {"nullableRequired": "value"}
