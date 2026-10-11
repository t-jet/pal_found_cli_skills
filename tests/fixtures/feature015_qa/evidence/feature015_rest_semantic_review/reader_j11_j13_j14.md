# Isolated offline reader: J11, J13, J14

Input: only `reader_prompts.json` cases J11/J13/J14, isolated `pal-found-dev` skill, SDK 1.101.0 and synthetic HTTP fixtures. No public documentation or expected-answer file was used. Code below is an adaptable application outline; fixture runs prove SDK request/response handling, not tenant permission or live effects.

## J11: folder pages, dataset metadata, binary file content

Local route: `SKILL.md` > Choose a development path > REST APIs; `references/rest-api.md` > Procedure; `references/rest/client-behavior.md` > Response modes, Bounded pagination, Timeouts, throttling and uncertain writes; `references/rest/v2/filesystem/Folder.md` > Procedure; `references/rest/v2/datasets/Dataset.md` > get; `references/rest/v2/datasets/File.md` > content. Exact signatures and errors: `references/rest/contracts/v2/filesystem/Folder/children.md`, `.../datasets/Dataset/get.md`, `.../datasets/File/content.md`.

```python
from functools import partial
from foundry_sdk import Config, FoundryClient, UserTokenAuth
# Load fetch_pages from this skill's examples/rest/common/bounded_pages.py.

client = FoundryClient(hostname=host, auth=UserTokenAuth(token=token),
    config=Config(timeout=30, max_retries=1,
        propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"))
folder = client.filesystem.Folder.get(folder_rid, request_timeout=30)
assert folder.rid == folder_rid
page_call = partial(client.filesystem.Folder.with_raw_response.children,
    folder_rid=folder_rid, page_size=100, request_timeout=30)
walk = fetch_pages(page_call, max_pages=10, max_items=1000)
if not walk.complete:
    report_partial(walk.items, walk.remaining_on_page,
        walk.next_page_token, walk.reason)
    # Stop on repeated token or budget; never report a complete traversal.
dataset = client.datasets.Dataset.get(dataset_rid, request_timeout=30)
assert dataset.rid == dataset_rid
byte_count = 0
with client.datasets.File.with_streaming_response.content(
        dataset_rid, file_path, request_timeout=30) as response:
    with open(output_path, "wb") as sink:
        for chunk in response.iter_bytes():
            byte_count += len(chunk)
            if byte_count > 1_048_576:
                raise ValueError("binary download budget exceeded")
            sink.write(chunk)
# Treat output as complete only if stream reached EOF and content format validates.
```

Use a caller-provided permitted host/token and valid RIDs. The prepared synthetic transport needs no enrollment. Live calls require folder/dataset/file access; dataset metadata access does not prove file-content access. `Folder.children` can yield an empty page with `nextPageToken`; the helper follows it and rejects repeated tokens. A 401 requires checking configured identity/token; a 403 requires checking grants and exact resource policy; a 404 can mean missing or invisible resource. `File.content` has named `FileNotFoundOnBranch`, `FileNotFoundOnTransactionRange`, `FileSizeLimitExceeded`, `GetFileContentPermissionDenied`, and invalid selector errors. Generic 429/503 are bounded by the one-attempt SDK configuration and caller budget; do not retry indefinitely. On partial binary consumption, close the context and label the output incomplete; discard or quarantine it before interpreting bytes. The file/branch/transaction selectors must match the intended view.

Offline output from isolated skill root: `Folder create/get/children request, result and error fixtures passed`; `v2.datasets.File.content: serialized request, decoded result and 9 named errors passed`.

## J13: discover and modify one governed folder

Local route: `references/rest/v2/filesystem/Project.md` > Procedure; `references/rest/v2/filesystem/Folder.md` > Procedure, Failures and recovery; `references/rest/v2/filesystem/Resource.md` > Resolve access, then change one resource; `references/rest/client-behavior.md` > Bounded pagination and Timeouts, throttling and uncertain writes. Exact project, folder and access requirement methods are in `references/rest/contracts/v2/filesystem/`.

```python
project = client.filesystem.Project.get(project_rid, request_timeout=30)
assert project.rid == project_rid
parent = client.filesystem.Folder.get(parent_folder_rid, request_timeout=30)
assert parent.rid == parent_folder_rid
requirements = client.filesystem.Resource.get_access_requirements(
    parent_folder_rid, request_timeout=30)
required_markings = {mark.marking_id for mark in requirements.markings}
assert approved_identity_has(required_markings, requirements.organizations)
page_call = partial(client.filesystem.Folder.with_raw_response.children,
    folder_rid=parent_folder_rid, page_size=100, request_timeout=30)
walk = fetch_pages(page_call, max_pages=10, max_items=1000)
if not walk.complete:
    report_partial(walk.items, walk.remaining_on_page,
        walk.next_page_token, walk.reason)
    raise RuntimeError("folder traversal incomplete")
new_folder = client.filesystem.Folder.create(
    display_name="Governance review", parent_folder_rid=parent_folder_rid,
    request_timeout=30)
verified = client.filesystem.Folder.get(new_folder.rid, request_timeout=30)
assert verified.rid == new_folder.rid
assert verified.parent_folder_rid == parent_folder_rid
assert verified.display_name == "Governance review"
```

`approved_identity_has` is application policy supplied by the project owner; reading access requirements does not grant rights or prove creation permission. A disappeared child is recorded as a concurrent change; refresh that RID or bounded parent listing and do not substitute an item with a similar name. A denied create requires checking identity and parent write grant. On timeout after create submission, list the intended parent's children under finite budgets and compare RID, type, parent and name. A matching name alone cannot prove which request created it; report uncertainty before replay. Synthetic fixture output: `Folder create/get/children request, result and error fixtures passed`; `v2.filesystem.Resource.get_access_requirements: serialized request, decoded result and 2 named errors passed`.

## J14: versioned AIP session and bounded response

Local route: `references/rest/v2/aip_agents/AgentVersion.md` > Select a session-compatible version; `references/rest/v2/aip_agents/Session.md` > Procedure, Worked example, Failures and recovery; `references/rest/contracts/v2/aip_agents/Session/streaming_continue.md` > Parameters and defaults, Documented operation errors; `references/rest/contracts/v2/aip_agents/Session/cancel.md` > Purpose and parameter meaning; `references/rest/client-behavior.md` > Response modes and Errors and cleanup.

```python
import uuid

agent = client.aip_agents.Agent.get(agent_rid, preview=True, request_timeout=30)
version = client.aip_agents.Agent.AgentVersion.get(
    agent_rid, chosen_version_string, preview=True, request_timeout=30)
session = client.aip_agents.Agent.Session.create(
    agent_rid, agent_version=version.string, preview=True, request_timeout=30)
assert session.agent_version == version.string
message_id = str(uuid.uuid4())
consumed = 0
with client.aip_agents.Agent.Session.with_streaming_response.streaming_continue(
        agent_rid, session.rid,
        parameter_inputs=validated_inputs_for_this_version,
        user_input={"text": "Summarize the permitted record"},
        message_id=message_id, preview=True,
        request_timeout=30) as stream:
    for chunk in stream.iter_bytes():
        consumed += len(chunk)
        if consumed > 16_384:
            break  # Context exit closes client response. Outcome remains incomplete.
        consume_markdown_bytes(chunk)
content = client.aip_agents.Agent.Session.Content.get(
    agent_rid, session.rid, preview=True, request_timeout=30)
# Inspect the recorded exchange and result; stream bytes alone are not completion proof.
```

Use a finite elapsed deadline as well as the byte bound. Choose `chosen_version_string` from bounded `AgentVersion.list` results, then match application-variable keys and discriminated values to that version. Session creation alone has no exchange. `streaming_continue` produces Markdown bytes, not SSE events. If cancellation is needed, send `Session.cancel(agent_rid, session.rid, message_id=message_id, preview=True)` for the same UUID, close the original response, then reload content. Cancel does not close the original stream itself; `CancelSessionFailedMessageNotInProgress` can reflect a race or already completed exchange. A byte/deadline budget exit is an incomplete outcome, not server cancellation. When preview is unavailable, check enrollment capability and identity with its owner; a different identity must not be treated as implicit authorization. Missing Agent/version/tool/model and invalid application variables require distinct corrections. Live Agent, tools, Ontology and model access remains tenant-specific. Synthetic fixture output: `Session create/get/list request, result and error fixtures passed`; `v2.aip_agents.Session.streaming_continue: serialized request, decoded result and 12 named errors passed`.
