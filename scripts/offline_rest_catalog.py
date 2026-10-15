"""Render SDK structural contracts while preserving domain-authored guidance.

Inputs are immutable git archives. Runtime validation and semantic acceptance
use independent tests; this renderer cannot approve its own output.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib
import io
import json
import re
import subprocess
import tarfile
from collections import defaultdict, deque
from pathlib import Path

RELEASE = "1.101.0"
COMMIT = "168d51910570b6966afa2320333ab36f6a3f7ccf"
EXPECTED_ID_HASH = "a6542de72e2fd73a6197ddb6063cf76617b1c8c1bad95f53547dbbce87760bcd"

_SERVICE_CONTEXT = {
    "v1.datasets": "Use these v1 dataset, branch, file and transaction resources when the selected application depends on a v1 contract. A file upload into a transaction is staged until commit; inspect the known transaction and resulting branch before treating data as published. Check the operation stage and do not substitute a v2 signature.",
    "v1.ontologies": "Use v1 Ontology metadata, objects, linked objects, Actions, Queries and attachments for a client pinned to v1. Read the target Ontology and type metadata before constructing object or Action inputs; result visibility and write authorization remain tenant specific.",
    "v2.admin": "Use Admin resources to read enrollment identity, users, groups, Organizations, role assignments and Markings before changing access. A role or membership change affects the named security boundary; identify the exact principal and resource, then read back assignments rather than assuming effective access from a write response.",
    "v2.aip_agents": "Use Agent and version metadata to select an enabled Agent before creating a session. Continue, stream or cancel a known session according to the interaction; inspect context and trace operations separately. Agent parameters and available Ontology context come from the permitted enrollment metadata.",
    "v2.audit": "Use Organization audit log files for a bounded, time-filtered evidence retrieval. Supply the documented date range and follow every page token, including after an empty page; retain partial results if a finite page budget or repeated token stops the traversal.",
    "v2.checkpoints": "Use checkpoint resources to search and inspect recorded pipeline checkpoints. Select the relevant checkpoint type, operation and time window, then distinguish an existing checkpoint from evidence that a later production build succeeded.",
    "v2.connectivity": "Use Connections to configure an authorized external source and its worker, authentication and network route. File and table imports refer to that Connection; inspect a configured import before replacement or execution. External credentials, permissions and reachable endpoints are prerequisites supplied by the enrollment and source system.",
    "v2.data_health": "Use checks and reports to inspect data quality or freshness results. A check definition, its latest report and an upstream build are different records; correlate their timestamps and target resources before diagnosing a stale output.",
    "v2.datasets": "Use v2 datasets, branches, files, transactions and views for data reads and writes. Select the intended branch or known transaction, bound file/page reads, and verify transaction commit plus resulting branch state before treating staged content as visible.",
    "v2.filesystem": "Start governance navigation with a permitted Project or Folder, then traverse children and inspect resources. Create or modify a folder/project only after identifying its parent, applicable access context and exact RID; verify the resulting resource and permissions through supported read operations.",
    "v2.functions": "Use Function and Query metadata to choose a published callable version and its input/output types. Execute or stream only with arguments matching the selected version; validation or permission failures require correcting the input or access before retrying.",
    "v2.language_models": "Select a model exposed by the permitted enrollment and use its operation-specific request and response format. Model availability, token limits and streaming behavior are operation dependent; test with a bounded prompt and handle rejected or partial responses explicitly.",
    "v2.media_sets": "Use Media Set metadata to identify an authorized collection, then select its items, views or retrieval operations. Binary/media outputs require the declared content format and a byte budget; a missing item or denied view should not be treated as an empty successful payload.",
    "v2.models": "Use Model metadata and version resources to choose a deployed or published artifact before invoking an inference operation. Experiment and live deployment results have distinct formats and lifecycle states; inspect the requested format and model availability before decoding the payload.",
    "v2.ontologies": "Read Ontology, object type and interface metadata before querying objects, Object Sets or links. Actions and Queries use their own declared parameters and authorization; check the result or validation outcome, and reconcile an uncertain write before replaying it.",
    "v2.orchestration": "Use schedules, builds and jobs to observe pipeline execution. Creating or requesting a build is not completion: poll a known build with a finite budget and inspect its terminal status, output and failing jobs before declaring data ready.",
    "v2.sql_queries": "Use SQL query resources for permitted Foundry dataset reads. Author the documented SELECT dialect, select branch and result format, then decode the returned Arrow or other declared payload and verify row/schema expectations within a byte budget.",
    "v2.streams": "Use stream metadata to select an existing stream or define a schema, partition keys and optional change-data-capture behavior. Publish or subscribe with finite batches and cursor handling; a key groups records but does not by itself deduplicate them.",
    "v2.third_party_applications": "Use application, version and website resources to inspect an application before uploading a version or deploying a website. Treat archive bytes, version identity and deployment state separately; verify the selected live version after a write or uncertain reply.",
    "v2.widgets": "Use Widget Set and Repository resources for authored widget bundles, then inspect Release and development-mode settings. A repository publish, first release and host-selected version are separate steps; confirm the host can use the intended release before treating the widget as deployed.",
}

# The frozen SDK leaves these three error docstrings as `todo`. Keep their
# source identity while giving readers the bounded meaning known from the
# error class and operation. No tenant role or grant name is inferred.
_ERROR_TODO_NOTES = {
    ("v1.datasets.Dataset.delete_schema", "DeleteSchemaPermissionDenied"):
        "Permission denied while deleting this dataset schema. Check caller access to the exact dataset; the SDK does not name a specific missing grant.",
    ("v1.datasets.Dataset.replace_schema", "PutSchemaPermissionDenied"):
        "Permission denied while replacing this dataset schema. Check caller access to the exact dataset; the SDK does not name a specific missing grant.",
    ("v1.datasets.File.delete", "PutSchemaPermissionDenied"):
        "Permission denied in a schema-related step of file deletion. Check caller access to the exact dataset and retain the error envelope; the SDK leaves the reason unspecified.",
}


def public_client_paths(operations) -> dict[str, str]:
    """Resolve methods through pinned public client objects, including nested resources."""
    sdk = importlib.import_module("foundry_sdk")
    if sdk.__version__ != RELEASE:
        raise ValueError(f"Installed SDK release differs: {sdk.__version__}")
    resolved = {}
    for version in ("v1", "v2"):
        client_type = importlib.import_module(f"foundry_sdk.{version}").FoundryClient
        client = client_type(auth=sdk.UserTokenAuth("offline-route-check"),
                             hostname="https://example.invalid")
        queue = deque([(client, "client", 0)])
        seen = set()
        methods = defaultdict(list)
        while queue:
            resource, prefix, depth = queue.popleft()
            if id(resource) in seen or depth > 5:
                continue
            seen.add(id(resource))
            for name in dir(resource):
                if name.startswith("_") or name in {"with_raw_response", "with_streaming_response"}:
                    continue
                try:
                    child = getattr(resource, name)
                except (AttributeError, RuntimeError):
                    continue
                path = f"{prefix}.{name}"
                if callable(child) and hasattr(child, "__func__"):
                    methods[(child.__func__.__module__, name)].append(path)
                elif depth < 5 and type(child).__name__.endswith("Client"):
                    queue.append((child, path, depth + 1))
        for row in operations:
            if row["version"] != version:
                continue
            module = row["source"][:-3].replace("/", ".")
            paths = methods.get((module, row["method"]), [])
            if len(paths) != 1:
                raise ValueError(f"Expected one public client path for {row['id']}: {paths}")
            resolved[row["id"]] = paths[0]
    if len(resolved) != len(operations):
        raise ValueError(f"Public client path count differs: {len(resolved)}")
    return resolved


def behavior_leaf(base: Path, method: str) -> Path:
    """Link a split guide to the page with this operation, when identifiable."""
    if not base.is_file():
        return base
    heading = re.compile(rf"(?m)^#{{2,3}} {re.escape(method)}\s*$")
    candidates = [base] + [base.with_name(f"{base.stem}-{number}.md")
                           for number in range(2, 12)]
    matches = [path for path in candidates if path.is_file()
               and heading.search(path.read_text(encoding="utf-8"))]
    if len(matches) > 1:
        raise ValueError(f"Duplicate operation heading for {base}: {method}")
    return matches[0] if matches else base


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


_MODEL_OFFLINE_NOTES = {
    "foundry_sdk.v2.connectivity.models.SnowflakeExternalOauth": (
        "External OAuth uses an authorization server trusted by Snowflake. Configure a Snowflake External OAuth "
        "security integration before using this connection. Its issuer and audience must match the token's `iss` "
        "and `aud` claims; `subject` is the Foundry Connection RID. The authorization server and Snowflake "
        "integration must agree on token signature validation, user mapping and authorized scopes. A malformed "
        "or unmatched token cannot be repaired by changing the Connection RID. The SDK model stores identifiers, "
        "not an access token or the Snowflake integration itself."
    ),
    "foundry_sdk.v2.connectivity.models.SnowflakeKeyPairAuthentication": (
        "Key-pair authentication uses the Snowflake user in `user` and its matching private key in "
        "`private_key`. Register the corresponding public key on that Snowflake user first. Supply the "
        "private key through the `EncryptedProperty` variant chosen for a write: plaintext is encrypted and "
        "stored by Foundry, while an existing secret name retains its encrypted value. Never substitute the "
        "public key for this private-key field. If authentication fails, compare user identity and public-key "
        "fingerprint with the intended key before rotating or resubmitting a secret."
    ),
    "foundry_sdk.v2.connectivity.models.StsRoleConfiguration": (
        "`role_arn` names the AWS IAM role to assume, for example `arn:aws:iam::123456789012:role/"
        "example-role`; it is not a user or account-root ARN. `role_session_name` identifies this assumed "
        "session and should be unique enough for audit. If supplied, `role_session_duration` is at least "
        "900 seconds and no greater than the role's configured maximum (which can be 1–12 hours); AWS role "
        "chaining imposes a one-hour maximum. `external_id` must match the role trust arrangement when one "
        "is required. `sts_endpoint` selects the STS endpoint; use the tenant's approved region/endpoint. "
        "A valid ARN alone does not grant AssumeRole permission or satisfy the trust policy."
    ),
}

_TRANSACTION_NOT_OPEN_NOTE = (
    "The requested dataset transaction is not `OPEN`. The typed error parameters identify "
    "`datasetRid`, `transactionRid` and the reported `transactionStatus`; the SDK status "
    "values are `OPEN`, `COMMITTED` and `ABORTED`. Read that known transaction and the "
    "intended branch separately under the authorized identity before choosing a next operation. "
    "Do not replay an upload, schema change, commit or abort against a closed transaction. "
    "If its state or access cannot be verified, retain `error_instance_id` for investigation."
)

_MODEL_OFFLINE_NOTES.update({
    "foundry_sdk.v1.datasets.errors.TransactionNotOpen": _TRANSACTION_NOT_OPEN_NOTE,
    "foundry_sdk.v2.datasets.errors.TransactionNotOpen": _TRANSACTION_NOT_OPEN_NOTE,
    "foundry_sdk._core.api_client.ResponseMode": (
        "An SDK transport response mode. `DECODED` returns the operation's ordinary typed result; "
        "`ITERATOR` traverses paged results; `RAW` exposes status and explicit decoding; "
        "`STREAMING` keeps the response open in a context manager. The table and SSE values are "
        "specialized operation formats. Choose through the public response wrapper supported by "
        "the operation, rather than passing `_sdk_internal` as application input."
    ),
    "foundry_sdk._core.api_client.SdkInternal": (
        "The SDK uses this internal TypedDict to carry an optional response mode into transport code. "
        "Application code selects ordinary, raw or streaming behavior through the public client "
        "wrappers described in the local client-behavior guide. This key is not a Foundry API field."
    ),
    "foundry_sdk._core.utils.Timeout": (
        "A positive integer request timeout in seconds. Supply it as `request_timeout` where the "
        "operation signature permits it. Reaching this bound does not prove whether a write "
        "succeeded; reconcile the known resource or transaction before replaying a mutation."
    ),
    "foundry_sdk._core.utils.RID": (
        "A Foundry resource identifier string beginning `ri.` and matching the SDK constraint below. "
        "Read the specific resource RID from permitted metadata or a prior response; a valid "
        "pattern alone does not establish that the resource exists or the caller can access it."
    ),
    "foundry_sdk._core.utils.UUID": (
        "A hyphenated UUID string matching the SDK hexadecimal pattern below. Preserve the "
        "returned identifier for later requests; this shape alone does not imply a Foundry RID "
        "or validate a resource's existence."
    ),
    "foundry_sdk.v2.connectivity.models.CreateConnectionRequestS3ConnectionConfiguration": (
        "Create an S3 Connection with a bucket URL ending in `/`, the bucket's region and a supported "
        "authentication variant. Public buckets may omit authentication. The field table gives the "
        "source-declared timeouts, retries and connection limits when omitted; those are connector "
        "behavior, not SDK model defaults. A custom endpoint may need an explicit signing region. "
        "Check source access and reachability before running an import."
    ),
    "foundry_sdk.v2.connectivity.models.CreateConnectionRequestSnowflakeConnectionConfiguration": (
        "Create a Snowflake Connection for the named account with an existing authentication identity. "
        "Optional database, schema, role and warehouse choose session defaults; each named resource "
        "must exist and be accessible to that identity. The account identifier selects the account, "
        "while `jdbc_properties` carries only approved, nonsecret driver options."
    ),
    "foundry_sdk.v2.connectivity.models.SnowflakeConnectionConfiguration": (
        "A stored Snowflake Connection identifies an account and its authentication mode. The optional "
        "database, schema, role and warehouse are session defaults and require the chosen identity's "
        "access. Inspect these fields and `jdbc_properties` before replacing the Connection; keep "
        "passwords and tokens in the authentication variant's encrypted fields."
    ),
    "foundry_sdk.v1.core.models.MediaType": (
        "The MIME media type of a file or attachment, such as `application/pdf`. Use the "
        "actual content type of the bytes; this SDK alias is a string and does not validate it."
    ),
    "foundry_sdk.v2.core.models.MediaType": (
        "The MIME media type of a file or attachment, such as `application/pdf`. Use the "
        "actual content type of the bytes; this SDK alias is a string and does not validate it."
    ),
    "foundry_sdk.v1.ontologies.models.PropertyValue": (
        "An Ontology property value uses the JSON encoding for its declared property type. "
        "The local type table below gives the SDK's supported encodings, including arrays, "
        "primitives, date/time, GeoJSON, Cipher, attachment, media and time-series values. "
        "Use the target property's permitted Ontology metadata to select the type."
    ),
    "foundry_sdk.v2.aip_agents.errors.ObjectTypeIdsNotFoundParameters": (
        "The error names object type IDs unavailable to this Agent request. Compare each ID "
        "with the object types returned by the permitted Ontology metadata API."
    ),
    "foundry_sdk.v2.aip_agents.errors.ObjectTypeRidsNotFoundParameters": (
        "The error names object type RIDs unavailable to this Agent request. Compare each RID "
        "with the object types returned by the permitted Ontology metadata API."
    ),
    "foundry_sdk.v2.aip_agents.errors.OntologyEntitiesNotFoundParameters": (
        "The error names unavailable Ontology object or link types. Compare each identity "
        "with the permitted Ontology metadata before changing the Agent request."
    ),
    "foundry_sdk.v2.aip_agents.models.AgentRid": (
        "An RID identifying an Agent created in AIP Chatbot Studio. Obtain an existing "
        "Agent RID from the authorized Studio or application configuration, or use a "
        "supplied synthetic RID in an offline fixture. The frozen SDK Agent client has "
        "`get` and session methods but no Agent list operation; `get` already requires the RID."
    ),
    "foundry_sdk.v2.aip_agents.models.InputContext": (
        "Custom retrieved context supplied to an Agent when continuing a session. Use the "
        "typed fields below and only content the caller is allowed to provide."
    ),
    "foundry_sdk.v2.aip_agents.models.Parameter": (
        "An Agent application-state variable with the name and type configured for that "
        "Agent. Read the Agent metadata before supplying a value."
    ),
    "foundry_sdk.v2.aip_agents.models.ParameterId": (
        "The identifier of an Agent application-state variable. Use the exact ID returned "
        "by the target Agent's parameter metadata."
    ),
    "foundry_sdk.v2.aip_agents.models.ParameterValue": (
        "A value for an Agent application-state variable. Match the value shape to the "
        "parameter type returned by the target Agent's metadata."
    ),
    "foundry_sdk.v2.aip_agents.models.ParameterValueUpdate": (
        "An update to an Agent application-state variable generated by the Agent. "
        "Check its parameter ID and typed value before applying it to local state."
    ),
    "foundry_sdk.v2.connectivity.models.CreateTableImportRequestTableImportConfig": (
        "Choose the table import configuration variant that matches the existing "
        "Connection's connector type. The union alternatives and type discriminator below "
        "give the wire shape; source query syntax depends on the selected connector."
    ),
    "foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestTableImportConfig": (
        "Choose the replacement table import configuration variant that matches the "
        "Connection's connector type. Preserve the chosen union discriminator and validate "
        "the source query before replacing the import."
    ),
    "foundry_sdk.v2.connectivity.models.TableImportConfig": (
        "The stored table import configuration has a variant for each supported connector "
        "type. Read its discriminator and variant fields below before interpreting the query "
        "or constructing an update."
    ),
    "foundry_sdk.v1.core.models.TraceParent": (
        "W3C `traceparent` is a string header for correlating Foundry telemetry across requests. "
        "Its trace ID is 16 bytes encoded as 32 hexadecimal characters and, for Foundry, must come "
        "from a time-based UUID. Preserve the same trace ID across related requests."
    ),
    "foundry_sdk.v1.core.models.TraceState": (
        "W3C `tracestate` is a string header carrying vendor-specific tracing state alongside "
        "`traceparent`. Pass through the state supplied by the active tracing context; this SDK "
        "alias does not construct or validate vendor entries."
    ),
    "foundry_sdk.v2.core.models.TraceParent": (
        "W3C `traceparent` is a string header for correlating Foundry telemetry across requests. "
        "Its trace ID is 16 bytes encoded as 32 hexadecimal characters and, for Foundry, must come "
        "from a time-based UUID. Preserve the same trace ID across related requests."
    ),
    "foundry_sdk.v2.core.models.TraceState": (
        "W3C `tracestate` is a string header carrying vendor-specific tracing state alongside "
        "`traceparent`. Pass through the state supplied by the active tracing context; this SDK "
        "alias does not construct or validate vendor entries."
    ),
    "foundry_sdk.v2.checkpoints.models.CheckpointType": (
        "A checkpoint type identifies the operation that produced a checkpoint record. Select an "
        "exact literal from the SDK definition below when filtering or interpreting records; the "
        "type alone does not say whether the operation succeeded. Read the record status and time."
    ),
    "foundry_sdk.v2.core.models.ChangeDataCaptureConfiguration": (
        "Change data capture uses the stream as a keyed update feed. Supply at least one key field "
        "in its stream schema, then choose the CDC configuration that matches the incoming change "
        "records. A key groups updates to the same entity; a key alone does not deduplicate records."
    ),
    "foundry_sdk.v2.core.models.ComputeSeconds": (
        "Compute seconds measure consumed compute time for resource usage accounting. This SDK "
        "alias gives a numeric quantity, not a charge or a per-operation quota. Interpret it with "
        "the usage record's resource and time window."
    ),
    "foundry_sdk.v2.core.models.Field": (
        "A Foundry schema field pairs `name` with a `FieldSchema` under wire key `schema`. "
        "Use the referenced FieldSchema definition for its supported type and nullability. "
        "A field name must match the columns or stream records it describes."
    ),
    "foundry_sdk.v2.core.models.RoleId": (
        "A Role ID identifies a permission set on a resource. Common roles are Owner, Editor, "
        "Viewer and Discoverer, but use the ID returned for the target resource and enrollment "
        "when assigning a role. A display name alone does not establish its ID or effective access."
    ),
    "foundry_sdk.v2.filesystem.models.FolderType": (
        "The folder type distinguishes an ordinary folder, Project and Space. Read the literal "
        "values below and use the matching resource operation when traversing the hierarchy. "
        "Project and Space also carry access context that an ordinary folder path does not convey."
    ),
    "foundry_sdk.v2.filesystem.models.Marking": (
        "A Marking restricts access to a file, folder or Project. `marking_id` identifies it; "
        "`is_directly_applied` distinguishes a direct marking from an inherited one. A user "
        "must satisfy every marking on the resource to access it."
    ),
    "foundry_sdk.v2.filesystem.models.Organization": (
        "An Organization is an access requirement on a Project. `organization_rid` identifies "
        "it; `is_directly_applied` distinguishes direct from inherited application. A user needs "
        "membership or guest membership in at least one Organization applied to the Project."
    ),
    "foundry_sdk.v2.filesystem.models.ProjectResourceReferenceUnion": (
        "A project resource reference represents a resource imported from another Project. "
        "Select the union alternative and discriminator shown below. The reference does not "
        "change ownership of the source resource; check its access separately."
    ),
    "foundry_sdk.v2.language_models.models.AnthropicEffort": (
        "`effort` controls the response token effort for supported Claude models beginning with "
        "Opus 4.5. Use one literal below only when the selected model accepts it. `HIGH` has "
        "the same behavior as omitting the parameter according to the frozen SDK."
    ),
    "foundry_sdk.v2.media_sets.models.Modality": (
        "A DICOM modality code identifies the imaging device or method associated with an item. "
        "Use the code recorded in the source DICOM metadata; the SDK type does not enumerate "
        "or validate the complete modality code set."
    ),
    "foundry_sdk.v2.ontologies.models.BlueprintIcon": (
        "This icon descriptor uses `type='blueprint'`, a hexadecimal `color`, and the `name` "
        "of a Blueprint icon available to the application's icon library. Check the chosen "
        "name against the locally available library assets before displaying the object type."
    ),
    "foundry_sdk.v2.ontologies.models.CipherText": (
        "An encrypted Cipher value is a string envelope in the form "
        "`CIPHER::{cipherChannelRid}::<ciphertext>::CIPHER`. Preserve the whole envelope and "
        "its channel RID; do not treat the ciphertext segment as a plaintext property value."
    ),
    "foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName": (
        "The API name of an Ontology interface link type. Obtain it from the permitted "
        "Ontology interface metadata for the target enrollment, and use that exact API name "
        "in link requests. A display label is not a reliable substitute."
    ),
    "foundry_sdk.v2.ontologies.models.ObjectTypeId": (
        "The unique object-type ID in Ontology metadata. Read the permitted target Ontology "
        "metadata and use its returned ID; an object type API name or display title may differ."
    ),
    "foundry_sdk.v2.ontologies.models.PropertyValue": (
        "An Ontology property value uses the JSON encoding for its declared property type. "
        "The local type table below lists arrays, primitives, date/time, GeoJSON, Cipher, "
        "attachment, media and time-series encodings. Match the target property metadata; "
        "an attachment or media reference needs its documented object shape, not a display string."
    ),
    "foundry_sdk.v2.ontologies.models.RelativeDateRangeQuery": (
        "This query filters a date or timestamp property against a range evaluated at query "
        "time. Supply either `field` or `property_identifier`, inclusive start and exclusive "
        "end bounds as needed, and a valid IANA time-zone ID such as `Etc/UTC`. Bounds are "
        "rounded to midnight in that zone, so the zone can change which records match."
    ),
    "foundry_sdk.v2.sql_queries.models.ExecuteSqlQueryRequest": (
        "`query` is a Spark SQL SELECT against Foundry datasets identified by path or RID. "
        "`fallback_branch_ids` supplies ordered branch fallbacks when the primary branch "
        "cannot be used; validate each intended branch before relying on it. The omitted "
        "serialization format is ARROW, so decode the returned bytes as Arrow."
    ),
    "foundry_sdk.v2.streams.models.CreateStreamRequestStreamSchema": (
        "`fields` declares the stream schema. Optional `key_field_names` group records with "
        "the same key into one partition and preserve their processing order; keys alone do "
        "not deduplicate. Key fields must use one of Boolean, Byte, Date, Decimal, Integer, "
        "Long, Short, String or Timestamp. Optional `change_data_capture` adds CDC behavior."
    ),
    "foundry_sdk.v2.streams.models.StreamType": (
        "`LOW_LATENCY` is the default stream type. `HIGH_THROUGHPUT` favors larger batches "
        "with some added latency. Select it after checking stream metrics for batches near "
        "their maximum or producer batch expiry in downstream jobs."
    ),
    "foundry_sdk.v1.datasets.errors.DeleteSchemaPermissionDeniedParameters": (
        "The frozen SDK leaves this error-parameter description unspecified. "
        "`Dataset.delete_schema` can return the named permission-denied error. "
        "Check access to the exact dataset and preserve the server error envelope; "
        "this type does not identify a particular missing grant."
    ),
    "foundry_sdk.v1.datasets.errors.PutSchemaPermissionDeniedParameters": (
        "The frozen SDK leaves this error-parameter description unspecified. "
        "The named permission-denied error appears in `Dataset.replace_schema` and in a "
        "schema-related step of `File.delete`. Check the exact dataset, operation and caller "
        "access; this shared type does not establish a single missing grant."
    ),
    "foundry_sdk.v2.connectivity.models.AwsAccessKey": (
        "AWS access-key authentication requires both the IAM access key ID and matching secret access key. "
        "Provide the secret as an `EncryptedProperty`; do not put it in JDBC properties or logs. "
        "The external IAM principal and its permissions must already exist."
    ),
    "foundry_sdk.v2.connectivity.models.AwsOidcAuthentication": (
        "Foundry issues an OIDC token when this Connection runs. The external trust policy must accept the "
        "configured issuer (`iss`), audience (`aud`) and this Connection RID as subject (`sub`). "
        "A token from another Connection does not satisfy that subject check; token issuance does not "
        "create the external trust policy."
    ),
    "foundry_sdk.v2.connectivity.models.CloudIdentity": (
        "Select a cloud identity already configured for this enrollment by its `cloud_identity_rid`. "
        "The identity replaces static credentials for the supported cloud resource, but its external "
        "trust and resource permissions still need to be configured and checked separately."
    ),
    "foundry_sdk.v2.connectivity.models.ConnectionExportSettings": (
        "`exports_enabled` allows this Connection to receive dataset exports. Set "
        "`export_enabled_without_markings_validation` only when the application has independently "
        "checked security markings for the data to export; some interactive flows cannot do so. "
        "Read back the Connection export flags after an update."
    ),
    "foundry_sdk.v2.connectivity.models.ConnectionWorker": (
        "This read model distinguishes a configured `FoundryWorker` from `UnknownWorker`. "
        "A Foundry worker executes source capability compute in Foundry and uses approved "
        "network egress policies for direct or agent-proxy reachability. `UnknownWorker` "
        "represents a worker configuration this SDK cannot describe; it is not an agent-host "
        "configuration to copy into a new Connection."
    ),
    "foundry_sdk.v2.connectivity.models.CreateConnectionRequestConnectionWorker": (
        "For a new supported Connection worker, select `CreateConnectionRequestFoundryWorker` "
        "(`type='foundryWorker'`) with approved `network_egress_policy_rids`. The other union "
        "arm is `CreateConnectionRequestUnknownWorker` (`type='unknownWorker'`), which has no "
        "agent-host configuration fields. This SDK exposes no selectable legacy agent-worker "
        "creation variant; agent-proxy reachability belongs to the Foundry worker's egress "
        "policy. Confirm the connector and external host are reachable before creating imports."
    ),
    "foundry_sdk.v2.connectivity.models.CreateConnectionRequestUnknownWorker": (
        "This create-union arm contains only `type='unknownWorker'`. It supplies no host, "
        "credential or egress configuration and cannot describe a legacy agent worker. "
        "The frozen SDK does not specify server acceptance or behavior for authoring an "
        "unknown worker. Use the supported Foundry-worker arm for a new configured worker."
    ),
    "foundry_sdk.v2.connectivity.models.FoundryWorker": (
        "This worker runs source capabilities in Foundry. `network_egress_policy_rids` identifies "
        "preconfigured direct or agent-proxy egress rules that permit the intended host and port. "
        "A worker selection alone does not make a private source reachable."
    ),
    "foundry_sdk.v2.connectivity.models.UnknownWorker": (
        "The API cannot represent this stored worker configuration, possibly because it is malformed "
        "or legacy. Do not write it back as a new worker. Inspect the Connection and plan a supported "
        "Foundry-worker configuration with approved direct or agent-proxy egress policies."
    ),
    "foundry_sdk.v2.connectivity.models.CreateConnectionRequestRestConnectionConfiguration": (
        "Supply at least one allowed domain. `oauth2_client_rid` refers to an outbound application "
        "already configured by an organization administrator for OAuth 2.0 authorization-code flow; "
        "the Connection can select only one such application. `additional_secrets` are optional named "
        "secrets for code and webhooks, separate from allowed domains."
    ),
    "foundry_sdk.v2.connectivity.models.RestConnectionConfiguration": (
        "The REST Connection limits requests to its configured domains. An optional "
        "`oauth2_client_rid` selects one preconfigured outbound application for OAuth 2.0; replacing it "
        "changes the OAuth selection for all configured domains. Check approved egress to the domains "
        "and the external server's authorization settings before using the Connection."
    ),
    "foundry_sdk.v2.connectivity.models.RestConnectionOAuth2": (
        "This authorization variant uses the Connection's `oauth2_client_rid`. An organization "
        "administrator must first configure the outbound application and its external OAuth 2.0 "
        "authorization-code client; selecting this variant does not provision that application."
    ),
    "foundry_sdk.v2.connectivity.models.DatabricksConnectionConfiguration": (
        "`host_name` is the Databricks workspace hostname and `http_path` is the SQL compute endpoint "
        "path, such as `/sql/1.0/warehouses/<warehouse-id>` for a SQL warehouse. Choose a supported "
        "authentication variant and only nonsecret JDBC properties. The prepared Foundry worker needs "
        "egress to the workspace host on port 443; Cloud Fetch may need separate storage egress."
    ),
    "foundry_sdk.v2.connectivity.models.OauthMachineToMachineAuth": (
        "Create a Databricks service principal and OAuth client secret in the external account first. "
        "Use its client ID and encrypted client secret here; this mode authenticates the service "
        "principal and does not itself create or authorize it."
    ),
    "foundry_sdk.v2.connectivity.models.PersonalAccessToken": (
        "Supply a Databricks personal access token already issued to the intended user or service "
        "principal as an `EncryptedProperty`. Keep its owner, expiry and workspace permissions aligned "
        "with the Connection. This model cannot generate or renew the external token."
    ),
    "foundry_sdk.v2.connectivity.models.WorkflowIdentityFederation": (
        "Foundry acts as OIDC issuer for this Connection. Match the configured issuer, audience and "
        "Connection RID subject to a precreated Databricks federation policy. If "
        "`service_principal_application_id` is present, the exchange uses that service principal's "
        "policy; otherwise it uses an account federation policy. No Databricks secret is stored here."
    ),
    "foundry_sdk.v2.connectivity.models.CreateConnectionRequestWorkflowIdentityFederation": (
        "The audience identifies the Databricks recipient for a Foundry-issued token. An optional "
        "service-principal application ID chooses a preconfigured service-principal federation policy; "
        "without it the token exchange uses an account federation policy. Configure the external "
        "policy before testing the Connection."
    ),
    "foundry_sdk.v2.connectivity.models.JdbcProperties": (
        "This is a map of JDBC driver property names to unencrypted values. Take supported keys from "
        "the approved driver and connector configuration; this SDK type declares no universal keys "
        "or defaults. Put passwords and tokens in the connector's encrypted authentication fields."
    ),
    "foundry_sdk.v2.connectivity.models.FileImportFilter": (
        "Filters select which source files enter an import. Apply them in the configured order and "
        "test representative paths against the source before executing the import; order can affect "
        "efficiency. A filter changes selection, not the Connection's file access permission."
    ),
    "foundry_sdk.v2.connectivity.models.ReplaceFileImportRequest": (
        "Choose the import mode, display name, source subfolder and ordered file filters for the "
        "replacement. An omitted subfolder means the source root. Preview representative included "
        "and excluded paths, then read back the import configuration before executing it."
    ),
    "foundry_sdk.v2.connectivity.models.S3ConnectionConfiguration": (
        "`bucket_url` needs a trailing slash. Select the bucket region and authentication mode; "
        "a public bucket may omit authentication. A custom S3 endpoint needs its own reachability "
        "and possibly signing region. Omitted timeout, connection and retry fields use the SDK "
        "source defaults shown in the field table; do not infer a tenant-specific bucket or role."
    ),
    "foundry_sdk.v2.connectivity.models.CreateConnectionRequestSmbConnectionConfiguration": (
        "Use a resolvable server hostname without an `smb://` prefix, the server's share name and "
        "an authentication variant. Omitted port uses 445. Optional base directory confines reads "
        "and writes beneath that path; message signing defaults true and fails against a server "
        "that cannot sign. Confirm share name and access on the SMB server."
    ),
    "foundry_sdk.v2.connectivity.models.SmbConnectionConfiguration": (
        "Use a resolvable SMB host, valid server share and supported authentication. Omitted port "
        "uses 445; optional base directory narrows file access. Message signing defaults true and "
        "requires server support. The share and credentials must already exist on the server."
    ),
})

for _connector, _label in (
    ("DatabricksTableImportConfig", "Databricks"),
    ("JdbcTableImportConfig", "custom JDBC"),
    ("MicrosoftAccessTableImportConfig", "Microsoft Access"),
    ("MicrosoftSqlServerTableImportConfig", "Microsoft SQL Server"),
    ("PostgreSqlTableImportConfig", "PostgreSQL"),
    ("SnowflakeTableImportConfig", "Snowflake"),
):
    _MODEL_OFFLINE_NOTES[f"foundry_sdk.v2.connectivity.models.{_connector}"] = (
        f"This config selects a table import on an authorized {_label} Connection. `query` uses the "
        "linked `TableImportQuery` shape and must be valid for that external source and caller. "
        "`initial_incremental_state` is optional; set it only when the import strategy and "
        "source's change position are known. Execute the import, then verify its run and dataset."
    )


def localized_model_prose(prose: str) -> str:
    """Render complete local model prose without public-reading directives."""
    prose = re.sub(r"\[([^]]+)\]\(https?://[^)]+\)", r"\1", prose)
    prose = re.sub(r"(?i)For more (?:information|details),? see the official "
                   r"(?:AWS|Databricks) documentation\.?", "", prose)
    prose = re.sub(r"https://learn\.microsoft\.com/[^\s|<]+",
                   "Confirm the share name on the SMB server.", prose)
    prose = re.sub(r"(?:<br>\s*){1,2}See https://docs\.snowflake\.com/[^\s|<]+",
                   "", prose)
    prose = re.sub(
        r"<br>\s*For additional information on keys for Foundry streams, see the"
        r"<br>\s*streaming keys user documentation\.", "", prose,
    )
    prose = re.sub(
        r"See the\s*<br>\s*documentation<br>\s*for more details\.", "", prose,
    )
    prose = prose.replace(
        "See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for valid values.",
        "Use an IANA time-zone ID such as Etc/UTC, Europe/London or America/New_York.",
    )
    return prose


def property_value_encoding_table(document: str) -> str:
    """Expose the pinned SDK's property encodings outside the `Any` source alias."""
    examples = {
        "Array": ["alpha", "bravo"],
        "Attachment": {"rid": "ri.blobster.main.attachment.synthetic"},
        "Boolean": True,
        "Byte": 31,
        "CipherText": "CIPHER::ri.bellaso.main.cipher-channel.synthetic::opaque::CIPHER",
        "Date": "2021-05-01",
        "Decimal": "2.718281828",
        "Double": 3.14159265,
        "Float": 3.14159265,
        "GeoPoint": {"type": "Point", "coordinates": [102.0, 0.5]},
        "GeoShape": {"type": "LineString", "coordinates": [[102.0, 0.0], [103.0, 1.0]]},
        "Integer": 238940,
        "Long": "58319870951433",
        "MediaReference": {
            "mimeType": "application/pdf",
            "reference": {"type": "mediaSetViewItem", "mediaSetViewItem": {
                "mediaSetRid": "ri.mio.main.media-set.synthetic",
                "mediaSetViewRid": "ri.mio.main.view.synthetic",
                "mediaItemRid": "ri.mio.main.media-item.synthetic",
            }},
        },
        "Secured Property Value": {"value": 10, "propertySecurityIndex": 5},
        "Short": 8739,
        "String": "Call me Ishmael",
        "Struct": {"firstName": "Alex", "lastName": "Karp"},
        "Timestamp": "2021-01-04T05:00:00Z",
        "Timeseries": {"seriesId": "wellPressureSeriesId",
                       "syncRid": "ri.time-series-catalog.main.sync.synthetic"},
        "Vector": [0.1, 0.3, 0.02],
    }
    timeseries_variants = [
        examples["Timeseries"],
        {"templateRid": "ri.codex-emu.main.template.synthetic", "templateVersion": "0.0.0"},
        "wellPressureSeriesId",
    ]

    def example_cell(name: str) -> str:
        values = timeseries_variants if name == "Timeseries" else [examples[name]]
        return "<br>".join(f"`{json.dumps(value, separators=(',', ':'))}`" for value in values)

    rows = []
    for line in document.splitlines():
        if not line.startswith("|"):
            continue
        cells = [part.strip() for part in line.split("|")[1:3]]
        if len(cells) != 2 or cells[0] == "Type" or set(cells[0]) <= {"-"}:
            continue
        property_type = re.sub(r"\[([^]]+)\]\(https?://[^)]+\)", r"\1", cells[0])
        rows.append((property_type, cells[1]))
    if len(rows) != 21 or {name for name, _ in rows} != examples.keys():
        raise ValueError("Pinned SDK PropertyValue documentation changed: review encodings")
    return "\n".join([
        "## JSON encodings by Ontology property type", "",
        "`typing.Any` is the SDK's Python alias, not permission to send an arbitrary JSON "
        "shape. Read the target property's type from permitted Ontology metadata, then use "
        "its encoding below. JSON examples illustrate shape with synthetic values; "
        "substitute authorized tenant identifiers, metadata and real encrypted values.", "",
        "| Property type | JSON encoding | JSON example |", "| --- | --- | --- |",
        *(f"| {name} | {encoding} | {example_cell(name)} |"
          for name, encoding in rows), "",
        "Decimal and Long are JSON strings so their values are not rounded through a JSON "
        "number. Date uses a local ISO 8601 date; Timestamp uses an ISO 8601 UTC offset "
        "date-time. GeoPoint and GeoShape use GeoJSON objects. Struct is an object keyed "
        "by struct field API name. An Attachment is an object with `rid`; a MediaReference "
        "has `mimeType` and a typed `reference`; a secured value has `value` and "
        "`propertySecurityIndex`. Timeseries accepts an object with `seriesId` and "
        "`syncRid`, an object with `templateRid` and `templateVersion`, or a bare "
        "series ID string. For compatibility the source also accepts Boolean, Byte, Double, Float, "
        "Integer and Short as JSON strings; prefer the primary encoding shown above.",
    ])


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
    client_paths = public_client_paths(selected)
    required = sorted(set().union(*(set(row["symbols"]) for row in selected))
                      | {identity for identity in symbols if identity.startswith("foundry_sdk._core.")})
    consumers = defaultdict(list)
    for operation in selected:
        for identity in operation["symbols"]:
            consumers[identity].append(operation["id"])
    model_paths = {}
    for identity in required:
        if identity.startswith("foundry_sdk._core."):
            model_paths[identity] = refs / "models" / "_core" / f"{identity.rsplit('.', 1)[1]}.md"
        else:
            _, version, service, kind, short = identity.split(".")
            model_paths[identity] = refs / "models" / version / service / kind / f"{short}.md"
    model_review_rows = []
    for identity in required:
        record = symbols[identity]
        path = model_paths[identity]
        source = definition_source(files[record["source"]], record["node"])
        property_document = (f"docs/{identity.split('.')[1]}/Ontologies/models/PropertyValue.md"
                             if identity in {"foundry_sdk.v1.ontologies.models.PropertyValue",
                                             "foundry_sdk.v2.ontologies.models.PropertyValue"} else None)
        description = localized_model_prose(
            _MODEL_OFFLINE_NOTES[identity] if identity in _MODEL_OFFLINE_NOTES
            else record["description"] or
            "The definition below supplies its fields or permitted values."
        )
        blocks = [description,
                  "## Exact SDK definition\n\nPython names are SDK attributes; `alias` values are wire names. "
                  "`Optional` permits null; a default controls omission. A nullable field without a default remains required. "
                  "`Literal` lists values; `Annotated` retains constraints and discriminators. "
                  "Request TypedDicts and response Pydantic models are distinct shapes.",
                  "```python\n" + source + "\n```"]
        property_encoding = (property_value_encoding_table(files[property_document])
                             if property_document else "")
        if property_encoding:
            blocks.insert(1, property_encoding)
        table = field_table(record["node"])
        if table:
            table = localized_model_prose(table)
            blocks.insert(2, table)
        dependencies = record["dependencies"]
        if dependencies:
            blocks.append("## Referenced definitions\n\n" + "\n".join(
                f"- [{dependency}]({relative_link(path, model_paths[dependency])})" for dependency in dependencies
            ))
        blocks.append("SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; "
                      "Copyright 2024 Palantir Technologies, Inc. "
                      "[license and notices](" + relative_link(path, skill / "assets/rest/LICENSE") + ").")
        destinations = write_parts(path, identity, blocks)
        reader_prose = "\n\n".join(part for part in (description, property_encoding, table) if part)
        model_review_rows.append({
            "id": identity,
            "source": record["source"],
            "source_file_sha256": digest(files[record["source"]]),
            "source_definition_sha256": digest(source),
            "source_description_sha256": digest(record["description"] or ""),
            "semantic_documentation": property_document,
            "semantic_documentation_sha256": digest(files[property_document]) if property_document else None,
            "source_description_placeholder": (record["description"] or "").strip().lower() in {"", "todo"},
            "dependencies": record["dependencies"],
            "consumer_operation_ids": consumers[identity],
            "local_pages": [str(part.relative_to(skill)).replace("\\", "/") for part in destinations],
            "local_page_sha256": [digest(part.read_bytes()) for part in destinations],
            "reader_prose_sha256": digest(reader_prose),
            "reader_prose_excerpt": description[:400],
            "unfenced_public_url_count": len(re.findall(r"https?://", reader_prose)),
            "source_fidelity_review": "pending_independent_review",
            "local_meaning_review": "pending_independent_review",
        })
    (root / "maintainer/rest-model-semantic-matrix.json").write_text(json.dumps({
        "sdk_release": RELEASE,
        "source_commit": COMMIT,
        "scope": "Complete transitive model, error and SDK core definition closure for all 425 operations",
        "symbol_count": len(model_review_rows),
        "source_fidelity_review": "pending_independent_review",
        "local_meaning_review": "pending_independent_review",
        "symbols": model_review_rows,
    }, indent=2) + "\n", encoding="utf-8")
    register = []
    for row in selected:
        path = refs / "contracts" / row["version"] / row["service"] / row["resource"] / f"{row['method']}.md"
        node = row["node"]
        description, _, documented_errors = doc_sections(node)
        documented_errors = [
            (name, _ERROR_TODO_NOTES.get((row["id"], name), meaning))
            for name, meaning in documented_errors
        ]
        behavior = behavior_leaf(
            refs / row['version'] / row['service'] / f"{row['resource']}.md",
            row['method'],
        )
        blocks = [f"API {row['version']}; release stage: {row['stage']}. "
                  "Check enrollment enablement and resource access before live execution.",
                  "## Purpose and parameter meaning\n\n" + description,
                  "## Public Python client route\n\nWith a configured "
                  f"`foundry_sdk.{row['version']}.FoundryClient` named `client`, call "
                  f"`{client_paths[row['id']]}`. This is the public composed resource path "
                  "in SDK 1.101.0; nested resource names and capitalization matter. "
                  "Use the signature below for required arguments and selectors. "
                  "The same resource also exposes documented raw and streaming wrappers when "
                  "the response-mode table lists them.",
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
            "client_path": client_paths[row["id"]],
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
            _SERVICE_CONTEXT[namespace] + " Read the selected operation contract before invocation; "
            "stage, API version and result lifetime remain operation-specific.",
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
