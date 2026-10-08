# Ontology operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

An Ontology identifies the business schema. Its metadata operations reveal visible types and links; they do not read instances or prove permission to execute Actions.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `Ontology.get`

Stage: Stable. Required SDK arguments: `ontology`.

Gets a specific ontology for a given Ontology API name or RID.

Read [exact contract](../../contracts/v2/ontologies/Ontology/get.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/Ontology/invoke_get.py): `python -B examples/rest/079/v2/ontologies/Ontology/invoke_get.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Ontology.get_full_metadata`

Stage: Public Beta. Required SDK arguments: `ontology`.

Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces. This endpoint is designed to return as much metadata as possible in a single request to support OSDK workflows. It may omit certain entities rather than fail the request.

Read [exact contract](../../contracts/v2/ontologies/Ontology/get_full_metadata.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/Ontology/invoke_get_full_metadata.py): `python -B examples/rest/079/v2/ontologies/Ontology/invoke_get_full_metadata.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Ontology.list`

Stage: Stable. Required SDK arguments: none beyond client configuration.

Lists the Ontologies visible to the current user.

Read [exact contract](../../contracts/v2/ontologies/Ontology/list.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/Ontology/invoke_list.py): `python -B examples/rest/079/v2/ontologies/Ontology/invoke_list.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Ontology.load_metadata`

Stage: Private Beta. Required SDK arguments: `ontology`, `action_types`, `interface_types`, `link_types`, `object_types`, `query_types`.

Load Ontology metadata for the requested object, link, action, query, and interface types.

Read [exact contract](../../contracts/v2/ontologies/Ontology/load_metadata.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/Ontology/invoke_load_metadata.py): `python -B examples/rest/079/v2/ontologies/Ontology/invoke_load_metadata.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Resolve the selected Ontology first, then request visible object, link, Action, query and interface metadata for a client. Keep the Ontology RID/API name and branch explicit. Missing metadata needs an access or selection check before code generation.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
