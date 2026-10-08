"""Render SDK structural contracts while preserving domain-authored guidance.

Inputs are immutable git archives. Runtime validation and semantic acceptance
use independent tests; this renderer cannot approve its own output.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import re
import subprocess
import tarfile
from pathlib import Path

RELEASE = "1.101.0"
COMMIT = "168d51910570b6966afa2320333ab36f6a3f7ccf"
EXPECTED_ID_HASH = "a6542de72e2fd73a6197ddb6063cf76617b1c8c1bad95f53547dbbce87760bcd"


def digest(value: str | bytes) -> str:
    return hashlib.sha256(value.encode() if isinstance(value, str) else value).hexdigest()


def definition_source(source: str, node: ast.AST) -> str:
    """Class decorators affect constructors and belong to the definition."""
    if isinstance(node, ast.ClassDef) and node.decorator_list:
        first = min(item.lineno for item in node.decorator_list)
        return "\n".join(source.splitlines()[first - 1:node.end_lineno])
    return ast.get_source_segment(source, node)


def archive(repository: Path) -> dict[str, str]:
    actual = subprocess.check_output(
        ["git", "-C", str(repository), "rev-parse", f"{RELEASE}^{{commit}}"], text=True
    ).strip()
    if actual != COMMIT:
        raise ValueError(f"Source release commit differs: {actual}")
    data = subprocess.check_output(["git", "-C", str(repository), "archive", COMMIT])
    with tarfile.open(fileobj=io.BytesIO(data)) as bundle:
        return {
            entry.name: bundle.extractfile(entry).read().decode("utf-8")
            for entry in bundle.getmembers()
            if entry.isfile() and entry.name.endswith((".py", ".md", "LICENSE", "NOTICE"))
        }


def imports(tree: ast.Module) -> dict[str, str]:
    return {
        item.asname or item.name: f"{node.module}.{item.name}"
        for node in tree.body
        if isinstance(node, ast.ImportFrom)
        for item in node.names
    }


def declarations(tree: ast.Module):
    for index, node in enumerate(tree.body):
        if isinstance(node, ast.ClassDef):
            names = [node.name]
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names = [node.target.id]
        elif isinstance(node, ast.Assign):
            names = [target.id for target in node.targets if isinstance(target, ast.Name)]
        else:
            continue
        following = tree.body[index + 1] if index + 1 < len(tree.body) else None
        description = ast.get_docstring(node) if isinstance(node, ast.ClassDef) else None
        if isinstance(following, ast.Expr) and isinstance(following.value, ast.Constant):
            if isinstance(following.value.value, str):
                description = following.value.value
        for name in names:
            if not name.startswith("_"):
                yield name, node, description or ""


def references(node, module: str, aliases: dict[str, str], symbols: dict) -> set[str]:
    result = set()

    def inspect(candidate):
        for item in ast.walk(candidate):
            qualified = None
            if isinstance(item, ast.Attribute) and isinstance(item.value, ast.Name):
                qualified = f"{aliases.get(item.value.id, '')}.{item.attr}"
            elif isinstance(item, ast.Name):
                qualified = aliases.get(item.id, f"{module}.{item.id}")
            if qualified and qualified.startswith("foundry_sdk._core.") and qualified not in symbols:
                exported = qualified.rsplit(".", 1)[1]
                matches = [identity for identity in symbols
                           if identity.startswith("foundry_sdk._core.") and identity.rsplit(".", 1)[1] == exported]
                if len(matches) == 1:
                    qualified = matches[0]
            if qualified in symbols:
                result.add(qualified)

    inspect(node)
    for item in ast.walk(node):
        if isinstance(item, ast.Constant) and isinstance(item.value, str):
            # Forward references may be compound expressions, not single names.
            try:
                inspect(ast.parse(item.value, mode="eval"))
            except (SyntaxError, ValueError):
                pass
    return result


def build_inventory(files: dict[str, str]):
    trees = {
        name: ast.parse(source)
        for name, source in files.items()
        if name.startswith("foundry_sdk/v") and name.endswith(".py")
    }
    trees['foundry_sdk/_core/api_client.py'] = ast.parse(files['foundry_sdk/_core/api_client.py'])
    symbols = {}
    for name, tree in trees.items():
        if not name.endswith(("/models.py", "/errors.py")):
            continue
        module = name[:-3].replace("/", ".")
        for short, node, description in declarations(tree):
            symbols[f"{module}.{short}"] = {
                "node": node, "module": module, "source": name,
                "description": description, "imports": imports(tree),
            }
    primitives = {"utils.py": {"RID", "UUID", "Long", "AwareDatetime", "Timeout"},
                  "model_base.py": {"ModelBase"}, "config.py": {"Config"},
                  "api_client.py": {"SdkInternal", "ResponseMode"}}
    for filename, exported in primitives.items():
        name = f"foundry_sdk/_core/{filename}"
        tree = ast.parse(files[name])
        for short, node, description in declarations(tree):
            if short in exported:
                module = name[:-3].replace("/", ".")
                symbols[f"{module}.{short}"] = {
                    "node": node, "module": module, "source": name,
                    "description": description, "imports": imports(tree),
                }
    for identity, record in symbols.items():
        record["dependencies"] = sorted(
            references(record["node"], record["module"], record["imports"], symbols) - {identity}
        )
    operations = []
    for name, tree in trees.items():
        parts = name.split("/")
        if len(parts) != 4 or parts[-1].startswith("_"):
            continue
        version, service = parts[1:3]
        module = name[:-3].replace("/", ".")
        for client in tree.body:
            if not isinstance(client, ast.ClassDef) or not client.name.endswith("Client"):
                continue
            if client.name.startswith(("Async", "_")):
                continue
            resource = client.name.removesuffix("Client")
            docs = next((path for path in files if path.startswith(f"docs/{version}/")
                         and path.endswith(f"/{resource}.md")
                         and f"/{service.replace('_', '')}/" in path.lower().replace("_", "")), None)
            for method in client.body:
                if not isinstance(method, ast.FunctionDef) or method.name.startswith("_"):
                    continue
                request = next((node for node in ast.walk(method) if isinstance(node, ast.Call)
                                and isinstance(node.func, ast.Attribute)
                                and node.func.attr == "RequestInfo"), None)
                if request is None:
                    continue
                wire = {item.arg: ast.unparse(item.value) for item in request.keywords}
                stage_match = re.search(
                    r"\[\*\*" + re.escape(method.name) + r"\*\*\][^\r\n]*?\|[^\r\n]*?\|\s*([^|\r\n]+)",
                    files[docs] if docs else "",
                )
                if not stage_match:
                    raise ValueError(f"Missing release stage: {name}:{method.name}")
                related = [node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                           and node.name == method.name]
                seeds = set().union(*(references(node, module, imports(tree), symbols) for node in related))
                closure, pending = set(seeds), list(seeds)
                while pending:
                    for dependency in set(symbols[pending.pop()]["dependencies"]) - closure:
                        closure.add(dependency)
                        pending.append(dependency)
                operations.append({
                    "id": f"{version}.{service}.{resource}.{method.name}",
                    "version": version, "service": service, "resource": resource,
                    "method": method.name, "node": method, "wire": wire,
                    "source": name, "docs": docs, "stage": stage_match.group(1).strip(),
                    "symbols": sorted(closure), "imports": imports(tree),
                    "ordinary_return": ast.unparse(method.returns),
                    "async_return": next((ast.unparse(node.returns) for cls in tree.body
                                           if isinstance(cls, ast.ClassDef) and cls.name == f"Async{resource}Client"
                                           for node in cls.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                                           and node.name == method.name), None),
                    "response_modes": {
                        mode: mode_return(tree, trees, class_name, method.name)
                        for mode, class_name in {
                            "sync_ordinary": f"{resource}Client",
                            "sync_raw": f"_{resource}ClientRaw",
                            "sync_streaming": f"_{resource}ClientStreaming",
                            "async_ordinary": f"Async{resource}Client",
                            "async_raw": f"_Async{resource}ClientRaw",
                            "async_streaming": f"_Async{resource}ClientStreaming",
                        }.items()
                    },
                })
    operations.sort(key=lambda operation: operation["id"])
    identity_hash = digest("\n".join(operation["id"] for operation in operations))
    if identity_hash != EXPECTED_ID_HASH:
        raise ValueError(f"Operation identity mismatch: {identity_hash}")
    return operations, symbols


def mode_return(tree, trees, class_name, method_name):
    client = next((node for node in tree.body if isinstance(node, ast.ClassDef)
                   and node.name == class_name), None)
    if client is None:
        return None
    direct = next((node for node in client.body
                   if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                   and node.name == method_name), None)
    if direct is not None:
        return ast.unparse(direct.returns) if direct.returns is not None else None
    constructor = next((node for node in client.body if isinstance(node, ast.FunctionDef)
                        and node.name == '__init__'), None)
    if constructor is None:
        return None
    assignment = next((node for node in constructor.body if isinstance(node, ast.Assign)
                       and any(isinstance(target, ast.Attribute) and target.attr == method_name
                               for target in node.targets)), None)
    if assignment is None:
        return None
    call = assignment.value
    if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Attribute):
        raise ValueError(f'Unrecognized wrapper assignment: {class_name}.{method_name}')
    stub = next((node for node in constructor.body if isinstance(node, ast.FunctionDef)
                 and isinstance(call.args[0], ast.Name) and node.name == call.args[0].id), None)
    if stub is None or not stub.args.args or stub.args.args[0].annotation is None:
        raise ValueError(f'Missing wrapper response model: {class_name}.{method_name}')
    model = ast.unparse(stub.args.args[0].annotation)
    helper = next((node for path, core_tree in trees.items() if '/_core/' in path
                   for node in core_tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                   and node.name == call.func.attr), None)
    if helper is None or not isinstance(helper.returns, ast.Subscript):
        raise ValueError(f'Missing wrapper helper return: {call.func.attr}')
    callable_return = helper.returns.slice.elts[1]
    annotation = callable_return.value if isinstance(callable_return, ast.Constant) else ast.unparse(callable_return)
    return re.sub(r'\bR\b', model, annotation)


def relative_link(origin: Path, destination: Path) -> str:
    import os
    return Path(os.path.relpath(destination, origin.parent)).as_posix()


def cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


_OFFLINE_SOURCE_CONTEXT = {
    "api/general/overview/paging/": ("references/rest/client-behavior.md",
        "Page size is a request hint. Continue with the returned nextPageToken until absent; bound pages and reject a repeated token."),
    "chatbot-studio/overview/": ("references/rest/v2/aip_agents/Agent.md",
        "An Agent has a RID and published versions. Select an accessible version before opening a conversation session."),
    "ontology-manager/overview/": ("references/ontology/modeling.md",
        "Ontology object types define the records and properties an Agent or application can access; check the caller's visibility."),
    "data-integration/datasets/": ("references/pipelines/transactions.md",
        "A dataset branch selects a lineage. A transaction stages writes on that lineage until it is committed or aborted."),
    "data-integration/datasets#snapshot": ("references/pipelines/transactions.md",
        "A snapshot replaces the selected output state at the next update; check the transaction mode before changing backing datasets."),
    "datasets-resources/branches/create-branch/": ("references/rest/catalog.md",
        "Create a branch on the intended dataset before writing to a non-default branch; use the matching version's Branch.create contract."),
    "datasets-resources/transactions/create-transaction/": ("references/rest/catalog.md",
        "Open a transaction on the intended dataset and branch before staging writes; commit it only after validating the staged changes."),
    "action-types/parameters-default-value/": ("references/ontology/actions.md",
        "Check every required Action input explicitly. This endpoint does not apply Action parameter defaults."),
    "action-types/notifications/": ("references/ontology/actions.md",
        "This endpoint does not trigger Action notifications; design notification behavior separately when required."),
    "data-integration/views": ("references/rest/v2/datasets/index.md",
        "A View is a virtual dataset backed by other datasets. This read endpoint does not support Views; choose a supported backing dataset."),
    "ontology-object-basics#filter-objects": ("references/ontology/queries.md",
        "Use the operation's filter model to combine property predicates, then validate names and types against the object type."),
    "chatbot-studio/application-state/": ("references/rest/v2/aip_agents/Session.md",
        "Application-variable keys and discriminated values must match the Agent version recorded on the session."),
    "chatbot-studio/retrieval-context/": ("references/rest/v2/aip_agents/Session.md",
        "Supplying contexts_override skips the Agent's automatic context retrieval and uses the provided contexts."),
    "chatbot-studio/core-concepts/#retrieval-context": ("references/rest/v2/aip_agents/Session.md",
        "RAG context comes from data sources configured for the session; inspect retrieved context before a continuation override."),
    "data-connection/file-based-syncs/": ("references/rest/v2/connectivity/index.md",
        "File import filters are evaluated in declared order. Review a sample path set before executing a changed import."),
    "data-integration/builds": ("references/pipelines/releases.md",
        "A Build runs asynchronously and has its own identity and status. Submission is not completion; poll with a finite budget."),
    "arrow.apache.org/": ("references/rest/v2/sql_queries/index.md",
        "Arrow is a columnar binary result format. Decode it with an Arrow reader and close the response stream; do not parse it as JSON."),
    "ontology-sdk/deploy-osdk-application-on-foundry/": ("references/applications/osdk.md",
        "The upload body is a ZIP artifact for the selected application version; validate its required manifest and files before deployment."),
    "data-connection/core-concepts/#direct-connection": ("references/rest/v2/connectivity/index.md",
        "A direct connection accesses its source through the configured runtime. Check source reachability and credentials before creating imports."),
    "data-connection/set-up-source/": ("references/rest/v2/connectivity/index.md",
        "A Connection configuration contains source/runtime settings; read it separately from imported datasets."),
    "data-connection/export-overview/": ("references/rest/v2/connectivity/index.md",
        "Export settings control whether this Connection can be an export destination. Verify the selected source and policy before changing them."),
    "data-integration/virtual-tables/": ("references/rest/v2/connectivity/index.md",
        "A Virtual Table represents an upstream table through a Connection. It does not copy every row into a Foundry dataset at creation."),
    "api/datasets/get-dataset-health-checks/": ("references/rest/v2/data_health/index.md",
        "Dataset health checks are separate from dataset content. Resolve the dataset RID, then inspect the linked check report."),
    "data-health-v2-resources/checks/get-latest-check-reports": ("references/rest/v2/data_health/index.md",
        "Latest check reports show recent check outcomes; verify report time and check identity before using a result."),
    "data-integration/media-sets/": ("references/rest/v2/media_sets/MediaSet.md",
        "A media reference identifies an item for use by another capability; it is different from downloading item bytes."),
    "spark.apache.org/docs/latest/sql-ref.html": ("references/pipelines/sql.md",
        "This query uses Spark SQL SELECT syntax. Bind dataset references using the operation's declared form and validate schema before execution."),
    "analytics-connectivity/odbc-jdbc-drivers/": ("references/pipelines/sql.md",
        "Use a supported dataset reference in a SELECT query. The operation contract defines accepted query inputs and result format."),
    "data-integration/streams/": ("references/rest/v2/streams/index.md",
        "A stream dataset accepts records through its configured stream source; creation and ingestion have separate contracts."),
    "github.com/palantir/osdk-ts": ("references/widgets/lifecycle.md",
        "Widget dev settings use a manifest with manifestVersion and devSettings; validate localhost URLs and entrypoint paths."),
}


def offline_source_references(blocks: list[str], path: Path, skill: Path) -> list[str]:
    """Turn source doc links into local routes plus the context needed offline."""
    notes: dict[str, str] = {}

    def target(url: str) -> str:
        match = next(((relative, explanation) for fragment, (relative, explanation)
                      in _OFFLINE_SOURCE_CONTEXT.items() if fragment in url), None)
        if match is None:
            raise ValueError(f"Unmapped source reference in {path}: {url}")
        relative, explanation = match
        destination = skill / relative
        if not destination.exists():
            raise ValueError(f"Missing local source context in {path}: {destination}")
        notes.setdefault(relative, explanation)
        return relative_link(path, destination)

    def substitute(block: str) -> str:
        linked = re.sub(r"\[([^]]+)\]\((https?://[^)]+)\)",
                        lambda m: f"[{m.group(1)}]({target(m.group(2))})", block)
        return re.sub(r"(?<!\()https?://(?:github\.com/palantir/osdk-ts)(?![\w/])",
                      lambda m: f"[local widget development reference]({target(m.group(0))})", linked)

    result = [substitute(block) for block in blocks]
    if notes:
        result.append("## Local background for referenced concepts\n\n" + "\n".join(
            f"- {explanation} [Local procedure]({relative_link(path, skill / relative)})."
            for relative, explanation in notes.items()))
    return result


def field_table(node: ast.AST) -> str:
    if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
        call = node.value
        if ast.unparse(call.func).endswith("TypedDict") and len(call.args) >= 2 and isinstance(call.args[1], ast.Dict):
            total = next((ast.literal_eval(k.value) for k in call.keywords if k.arg == "total"), True)
            rows = ["## TypedDict keys", "", "Nullable values and omitted keys are distinct.", "",
                    "| Key | Type | Presence |", "| --- | --- | --- |"]
            for key, value in zip(call.args[1].keys, call.args[1].values):
                annotation = ast.unparse(value)
                optional = "NotRequired[" in annotation or (not total and "Required[" not in annotation)
                rows.append("| " + " | ".join([str(ast.literal_eval(key)), cell(annotation),
                                                "may be omitted" if optional else "required"]) + " |")
            return "\n".join(rows)
    if not isinstance(node, ast.ClassDef):
        return ""
    typed_dict = any(ast.unparse(base).endswith("TypedDict") for base in node.bases)
    total = next((ast.literal_eval(k.value) for k in node.keywords if k.arg == "total"), True)
    representation = ("TypedDict keys use Required/NotRequired and the declared total setting. "
                      "A nullable value does not by itself permit key omission." if typed_dict else
                      "Model fields use their declared defaults and aliases. Nullable and omittable are separate; "
                      "SDK model serialization uses aliases and excludes None values.")
    rows = ["## Fields and wire names", "", representation, "",
            "| SDK field | Wire name | Type | Omission/default | Meaning |",
            "| --- | --- | --- | --- | --- |"]
    for index, field in enumerate(node.body):
        if not isinstance(field, ast.AnnAssign) or not isinstance(field.target, ast.Name):
            continue
        name = field.target.id
        wire_name = name
        omission = "required; no default"
        if field.value is not None:
            omission = ast.unparse(field.value)
            if isinstance(field.value, ast.Call):
                defaults = {item.arg: item.value for item in field.value.keywords}
                if "alias" in defaults:
                    alias = defaults["alias"]
                    if isinstance(alias, ast.Call) and alias.args:
                        alias = alias.args[0]
                    try:
                        wire_name = str(ast.literal_eval(alias))
                    except (ValueError, TypeError):
                        wire_name = ast.unparse(alias)
                omission = ("default " + ast.unparse(defaults["default"])) if "default" in defaults else "required; no default"
        annotation = ast.unparse(field.annotation)
        if typed_dict:
            optional_key = "NotRequired[" in annotation or (not total and "Required[" not in annotation)
            omission = "TypedDict key may be omitted" if optional_key else "TypedDict key required"
        next_node = node.body[index + 1] if index + 1 < len(node.body) else None
        meaning = "No additional field description in SDK source."
        if isinstance(next_node, ast.Expr) and isinstance(next_node.value, ast.Constant):
            if isinstance(next_node.value.value, str):
                meaning = next_node.value.value.strip()
        rows.append("| " + " | ".join(cell(value) for value in [name, wire_name, annotation, omission, meaning]) + " |")
    return "\n".join(rows) if len(rows) > 6 else ""


def doc_sections(method: ast.FunctionDef):
    text = ast.get_docstring(method) or ""
    summary = text.split(":param", 1)[0].split(":return:", 1)[0].strip()
    meanings = {match.group(1): " ".join(match.group(2).split()) for match in re.finditer(
        r":param ([a-zA-Z_][a-zA-Z0-9_]*):[ \t]*(.*?)(?=\n\s*:[a-z]+|\Z)", text, re.S
    )}
    errors = [(match.group(1), " ".join(match.group(2).split())) for match in re.finditer(
        r":raises ([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*?)(?=\n\s*:[a-z]+|\Z)", text, re.S
    )]
    return summary, meanings, errors


def parameter_table(method: ast.FunctionDef) -> str:
    args = method.args
    positional = args.posonlyargs + args.args
    defaults = [None] * (len(positional) - len(args.defaults)) + args.defaults
    parameters = list(zip(positional, defaults)) + list(zip(args.kwonlyargs, args.kw_defaults))
    _, meanings, _ = doc_sections(method)
    rows = ["## Parameters and defaults", "", "| SDK parameter | Type | Required/default | Meaning |",
            "| --- | --- | --- | --- |"]
    for argument, default in parameters:
        if argument.arg == "self":
            continue
        meaning = meanings.get(argument.arg) or "Value shape and constraints are in its referenced local type definition."
        if argument.arg == "_sdk_internal":
            meaning = "SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input."
        rows.append("| " + " | ".join(cell(value) for value in [
            argument.arg, ast.unparse(argument.annotation) if argument.annotation else "unannotated",
            "required" if default is None else ast.unparse(default),
            meaning,
        ]) + " |")
    return "\n".join(rows)


def write_parts(path: Path, title: str, blocks: list[str]) -> list[Path]:
    """Keep full blocks readable and split large source definitions explicitly."""
    chunks, current = [], [f"# {title}\n"]
    for block in blocks:
        if len(block.splitlines()) > 255:
            lines = block.splitlines()
            is_code = lines[0].startswith("```") and lines[-1] == "```"
            raw = lines[1:-1] if is_code else lines
            pieces = [raw[start:start + 240] for start in range(0, len(raw), 240)]
            expanded = ["\n".join(([lines[0]] + piece + ["```"]) if is_code else piece) for piece in pieces]
        else:
            expanded = [block]
        for piece in expanded:
            if len(("\n\n".join(current) + piece).splitlines()) > 275:
                chunks.append(current)
                current = [f"# {title}: continuation {len(chunks) + 1}\n"]
            current.append(piece)
    chunks.append(current)
    destinations = [path] + [path.with_name(f"{path.stem}-{n}.md") for n in range(2, len(chunks) + 1)]
    for destination, content in zip(destinations, chunks):
        navigation = " | ".join(f"[Part {n + 1}]({relative_link(destination, other)})" for n, other in enumerate(destinations))
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("\n\n".join(content) + "\n\n" + navigation + "\n", encoding="utf-8")
        if len(destination.read_text().splitlines()) > 300:
            raise ValueError(f"Leaf exceeded 300 lines: {destination}")
    return destinations


def render(root: Path, files: dict[str, str], operations, symbols, limit: int | None):
    skill = root / ".agents/skills/pal-found-dev"
    refs = skill / "references/rest"
    selected = operations if limit is None else pilot(operations)[:limit]
    required = sorted(set().union(*(set(row["symbols"]) for row in selected))
                      | {identity for identity in symbols if identity.startswith("foundry_sdk._core.")})
    model_paths = {}
    for identity in required:
        if identity.startswith("foundry_sdk._core."):
            model_paths[identity] = refs / "models" / "_core" / f"{identity.rsplit('.', 1)[1]}.md"
        else:
            _, version, service, kind, short = identity.split(".")
            model_paths[identity] = refs / "models" / version / service / kind / f"{short}.md"
    for identity in required:
        record = symbols[identity]
        path = model_paths[identity]
        source = definition_source(files[record["source"]], record["node"])
        blocks = [record["description"] or "The definition below supplies its fields or permitted values.",
                  "## Exact SDK definition\n\nPython names are SDK attributes; `alias` values are wire names. "
                  "`Optional` permits null; a default controls omission. A nullable field without a default remains required. "
                  "`Literal` lists values; `Annotated` retains constraints and discriminators. "
                  "Request TypedDicts and response Pydantic models are distinct shapes.",
                  "```python\n" + source + "\n```"]
        table = field_table(record["node"])
        if table:
            blocks.insert(2, table)
        dependencies = record["dependencies"]
        if dependencies:
            blocks.append("## Referenced definitions\n\n" + "\n".join(
                f"- [{dependency}]({relative_link(path, model_paths[dependency])})" for dependency in dependencies
            ))
        blocks.append("SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; "
                      "Copyright 2024 Palantir Technologies, Inc. "
                      "[license and notices](" + relative_link(path, skill / "assets/rest/LICENSE") + ").")
        write_parts(path, identity, blocks)
    register = []
    for row in selected:
        path = refs / "contracts" / row["version"] / row["service"] / row["resource"] / f"{row['method']}.md"
        node = row["node"]
        description, _, documented_errors = doc_sections(node)
        behavior = refs / row['version'] / row['service'] / f"{row['resource']}.md"
        blocks = [f"API {row['version']}; release stage: {row['stage']}. "
                  "Check enrollment enablement and resource access before live execution.",
                  "## Purpose and parameter meaning\n\n" + description,
                  "## SDK invocation contract\n\n```python\n"
                  + f"def {row['method']}({ast.unparse(node.args)}) -> {row['ordinary_return']}: ...\n```",
                  parameter_table(node),
                  "## Documented operation errors\n\n" + (
                      "| Error | Meaning |\n| --- | --- |\n" + "\n".join(
                          "| " + cell(name) + " | " + cell(meaning) + " |" for name, meaning in documented_errors
                      ) if documented_errors else "No named operation errors are listed in this method's docstring; transport and generic API failures remain possible."
                  ),
                  "## Wire request\n\n" + "\n\n".join(f"**{key}**\n\n```python\n{value}\n```" for key, value in row["wire"].items()),
                  "## Response modes\n\nOrdinary sync return: `" + row["ordinary_return"]
                  + "`. Ordinary async return: `" + (row["async_return"] or "not exposed")
                  + "`. Wrapper availability and exact returns from the frozen source:\n\n"
                  + "| Client mode | Return annotation |\n| --- | --- |\n"
                  + "\n".join("| " + mode + " | " + cell(value or "Not exposed") + " |"
                              for mode, value in row["response_modes"].items())
                  + "\n\nAn absent wrapper method cannot be selected for this operation. "
                  "Use an exposed mode and its actual lifetime. [Client lifetimes and finite work]("
                  + relative_link(path, refs / "client-behavior.md") + ").",
                  "## Complete referenced models and errors\n\n" + "\n".join(
                      f"- [{identity}]({relative_link(path, model_paths[identity])})" for identity in row["symbols"]
                  ),
                  "## Identity and execution boundary\n\n[Authentication and effective access]("
                  + relative_link(path, refs / "authentication.md")
                  + "). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. "
                  "Use configured application grants and resource permissions; verify tenant-specific prerequisites. "
                  "The domain guide supplies authored workflows, examples and outcome reconciliation."]
        if behavior.exists():
            blocks.append("## Application workflow\n\nRead the [local resource guide]("
                          + relative_link(path, behavior)
                          + ") for its authored operations and runnable examples. "
                          "A guide covering selected methods does not establish coverage of other methods.")
        blocks = offline_source_references(blocks, path, skill)
        destinations = write_parts(path, row["id"], blocks)
        register.append({
            "id": row["id"], "stage": row["stage"], "signature": ast.unparse(node.args),
            "ordinary_return": row["ordinary_return"], "async_return": row["async_return"],
            "response_modes": row["response_modes"],
            "wire": row["wire"], "source_sha256": digest(files[row["source"]]),
            "doc_sha256": digest(files[row["docs"]]), "symbols": row["symbols"],
            "contract": str(path.relative_to(skill)).replace("\\", "/"),
            "parts": [str(part.relative_to(skill)).replace("\\", "/") for part in destinations],
            "behavior": str(behavior.relative_to(skill)).replace("\\", "/") if behavior.exists() else None,
            "author": "python-developer", "reviewer": None, "review_status": "unreviewed",
            "behavior_status": "domain authoring pending", "example_status": "domain authoring pending",
        })
    destination = root / "maintainer/rest-contract-register.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps({
        "sdk_release": RELEASE, "source_commit": COMMIT, "openapi_version": "1.1697.0",
        "operation_ids_sha256": EXPECTED_ID_HASH, "pilot": limit is not None,
        "operation_count": len(register), "corrected_reachable_symbols": len(required),
        "operations": register,
    }, indent=2) + "\n", encoding="utf-8")
    (root / "maintainer/rest-model-register.json").write_text(json.dumps({
        "sdk_release": RELEASE, "source_commit": COMMIT,
        "candidate_symbol_count": len(required), "independent_closure_status": "pending",
        "symbols": [{"id": identity, "source": symbols[identity]["source"],
                     "source_sha256": digest(files[symbols[identity]["source"]]),
                     "definition_sha256": digest(definition_source(
                         files[symbols[identity]["source"]], symbols[identity]["node"])),
                     "dependencies": symbols[identity]["dependencies"],
                     "local_definition": str(model_paths[identity].relative_to(skill)).replace("\\", "/"),
                     "semantic_review_status": "unreviewed"} for identity in required],
    }, indent=2) + "\n", encoding="utf-8")
    notices = skill / "assets/rest"
    notices.mkdir(parents=True, exist_ok=True)
    for name in ("LICENSE", "NOTICE"):
        if name in files:
            (notices / name).write_text(files[name], encoding="utf-8")
    namespaces = sorted({f"{row['version']}.{row['service']}" for row in selected})
    catalog = refs / "catalog.md"
    catalog_blocks = ["Choose the API version and capability, then a resource and method. "
                      "Each method links exact inputs, return modes and complete local model/error definitions. "
                      "v1 and v2 identities are separate contracts; a release stage is an availability decision, not permission.",
                      "## Services\n\n" + "\n".join(
                          f"- [{namespace}]({namespace.replace('.', '/')}/index.md)" for namespace in namespaces
                      ),
                      "## Task selection\n\nGovernance applications start with Filesystem projects, folders and resources, "
                      "then Admin identity/role/marking contracts where the task requires them. "
                      "AIP applications select Agents/session or Models/language-model contracts; "
                      "dataset pipelines select Datasets, Orchestration, health and checkpoint resources. "
                      "Ontology applications choose the matching version's schema, objects, Actions and Queries. "
                      "Connectivity, streams, SQL, Media Sets, Widgets, audit and application registration have their own services.",
                      "[Authentication](authentication.md) | [Response modes and finite work](client-behavior.md) "
                      "| [REST authoring procedure](../rest-api.md)"]
    write_parts(catalog, "Foundry Platform REST operation catalog", catalog_blocks)
    for namespace in namespaces:
        version, service = namespace.split(".")
        index = refs / version / service / "index.md"
        rows = [row for row in register if row["id"].startswith(namespace + ".")]
        write_parts(index, namespace + " resources and operations", [
            "Select the resource matching the task and read its operation contract before preparing an invocation. "
            "Stage, API version and actual result lifetimes remain operation-specific.",
            "| Operation | Stage |\n| --- | --- |\n" + "\n".join(
                f"| [{row['id']}]({relative_link(index, skill / row['contract'])}) | {row['stage']} |" for row in rows
            ),
            "[All services](../../catalog.md) | [SDK handling](../../client-behavior.md)",
        ])
    return {"operations": len(register), "symbols": len(required), "pilot": limit is not None}


def pilot(operations):
    """Select diverse contracts; these samples cannot establish acceptance."""
    wanted = ["v2.filesystem.Folder.children", "v2.filesystem.Folder.create", "v2.filesystem.Project.create",
              "v2.datasets.File.read", "v2.datasets.Transaction.create", "v1.ontologies.OntologyObject.list",
              "v2.functions.Query.execute", "v2.aip_agents.Session.create", "v2.models.Model.create",
              "v2.ontologies.OntologyObjectSet.aggregate"]
    chosen = [row for identity in wanted for row in operations if row["id"] == identity]
    present = {row["id"] for row in chosen}
    return chosen + [row for row in operations if row["id"] not in present]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-repository", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--pilot", type=int)
    args = parser.parse_args()
    files = archive(args.source_repository)
    operations, symbols = build_inventory(files)
    print(json.dumps(render(args.output_root, files, operations, symbols, args.pilot), sort_keys=True))


if __name__ == "__main__":
    main()
