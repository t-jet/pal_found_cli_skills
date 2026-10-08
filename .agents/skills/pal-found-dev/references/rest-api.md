# Develop with the Foundry REST API

[Development guide](../SKILL.md)

## Discover and author any frozen SDK REST operation

### Concept and lifecycle

The Foundry Platform REST SDK addresses platform resources through versioned
HTTP contracts: datasets, Ontology, filesystem governance, identity/markings,
pipeline orchestration, Functions, AIP agents, language/models, connectivity,
streams, SQL, media, widgets, audit and application registration. SDK 1.101.0
provides 425 logical operations across 113 resources and 20 version/service
namespaces. Sync, async and response wrappers are forms of those operations.

Use the [local catalog](rest/catalog.md) to select an exact contract. The
Platform SDK differs from an application-specific generated Ontology SDK.
OSDK bindings reflect selected enrollment entities; Platform SDK methods expose
the frozen platform API. The optional CLI has a separate command surface.

An operation can return a resource, page, bytes, stream or pending job/session.
HTTP success establishes its documented result. It does not automatically
prove a build finished, transaction committed, Action side effect succeeded
or model deployment became ready.

### Prerequisites

Prepare SDK 1.101.0 with matching Python dependencies, the permitted host and
identity, resource IDs, branch/version context and relevant data schemas.
Fixture authoring uses synthetic values and a fake transport. Live execution
requires authorized identity/application registration and enrollment metadata.
Private/beta capability enablement is a separate administrator prerequisite.
Missing tenant values cannot be replaced with guessed names or permissions.

Root FoundryClient and AsyncFoundryClient imports select v2; v1 clients come
from foundry_sdk.v1. [Authentication](rest/authentication.md) explains acting
identity, configured application grants and resource access. [Client behavior](rest/client-behavior.md)
explains actual modes and finite work.

### Procedure

1. Describe the intended resource effect and success evidence. For governance,
   name the project/folder/resource and permitted modification. For AIP,
   name the agent/session or model capability and completion lifecycle.
2. Choose the API version/service in the local catalog. Read its exact method,
   signature, stage and HTTP body/query/header contract.
3. Follow local input/output/error definitions: aliases, nullable versus
   optional fields, nested unions/discriminators, enums and validation limits.
   Obtain tenant-specific schemas from supplied fixtures or authorized metadata.
4. Adapt the invocation using declared IDs and identity. Select ordinary/raw/
   streaming handling from its actual return type. Bound requests, pages,
   objects, bytes, attempts and polls where needed.
5. Verify the serialized request and response/error handling with a fake
   transport. Record which assertions establish fixture behavior.
6. With enrollment access, execute and inspect its documented resource effect
   or supported status lookup. Reconcile partial, denied, canceled and uncertain
   outcomes before another mutation.

### Worked example

Illustrative governance task: inspect a known folder before planning a change.
Folder.get is a Stable v2 read with no body. Supply an authorized folder RID
and prepared client; its local contract defines all Folder fields and errors.

    from foundry_sdk import Config, FoundryClient, UserTokenAuth

    # Replace illustrative values only for an authorized live call.
    client = FoundryClient(
        hostname="example.palantirfoundry.com",
        auth=UserTokenAuth(token="<authorized-user-token>"),
        config=Config(timeout=30, max_retries=1,
                      propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
    )
    folder_rid = "ri.compass.main.folder.00000000-0000-0000-0000-000000000001"
    folder = client.filesystem.Folder.get(folder_rid, request_timeout=30)
    assert folder.rid == folder_rid
    print(folder.display_name, folder.parent_folder_rid, folder.trash_status)

Read [Folder.get and its complete models/errors](rest/contracts/v2/filesystem/Folder/get.md).
Check trash_status and the supplied hierarchy before selecting a modification.
This read does not establish modification permission. A synthetic HTTP fixture
establishes serialization and handling; a live call needs authorized values.

For traversal, use [raw pages and the local helper](rest/client-behavior.md#bounded-pagination).
It preserves empty intermediate pages, rejects repeated tokens, closes
responses and records partial progress. AIP integrations use their own local
agent/session/model inputs and lifecycle contracts.

### Expected result and checks

Code uses one exact versioned method, correct SDK/JSON field names and complete
nested shapes. Assertions distinguish response parsing from resource effect
and later completion. Evidence names identity, availability, budgets, schemas,
expected errors and safe recovery. Public retrieval supplies no required fact.

### Failures and recovery

Use named errors and their local parameter models. For access failures, check
identity, registration and resource policy. For invalid data, correct the
documented constraint before another call. For unavailable API/capability,
confirm enablement with its owner. [Client behavior](rest/client-behavior.md)
explains throttling, cleanup and uncertain writes.

After a timed-out mutation, retain request/target IDs and use the resource's
supported reconciliation path. If still unknown, record uncertainty and involve
its owner before replay. Exhausted page/poll budgets produce partial or pending
outcomes, not a completed task.

### Access boundary

Local contracts, authoring, synthetic validation and fixture runs use prepared
tools while public internet access is blocked. Real discovery, OAuth
authorization, API calls and completion checks need enrollment access.
Missing schema/binding, identity, capability or runtime identifies a blocked
step. Fixture evidence cannot claim live execution or permission.

Optional attribution: [API overview](https://www.palantir.com/docs/foundry/api/)
and [official SDK release](https://github.com/palantir/foundry-platform-python/releases/tag/1.101.0).
