# Object type metadata and visible relationships

[REST development](../../../rest-api.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

An object type defines the schema and identity of Ontology objects. Its API name,
RID, primary-key property, title property and typed property definitions describe
how applications read object records. They are distinct from a particular object's
primary-key value. Link-type metadata describes relationships between types;
reading that metadata does not fetch all linked objects or grant access to them.

## Prerequisites

Select the intended Ontology and branch, then resolve an accessible object type.
Use SDK 1.101.0 and the exact v2 models linked from each operation contract. Prepare
the business schema before constructing property filters, object inputs or Action
parameters. A synthetic type named `Asset` has no platform-wide meaning. Missing
visibility can reflect permissions rather than absence.

## Procedure

| Operation | Read and interpret |
| --- | --- |
| [get](../../contracts/v2/ontologies/ObjectType/get.md) | Resolve the API name and inspect primary key, title and property types. |
| [get_full_metadata](../../contracts/v2/ontologies/ObjectType/get_full_metadata.md) | Request the complete metadata representation supported by that operation. |
| [get_by_rid_batch](../../contracts/v2/ontologies/ObjectType/get_by_rid_batch.md) | Resolve at most100 RIDs; match visible returned identities to inputs. Missing or denied types are filtered out. |
| [list](../../contracts/v2/ontologies/ObjectType/list.md) | Enumerate visible type metadata with finite paging. Its aliases field is always empty; use the get-by-RID paths when aliases are required. |
| [get_outgoing_link_type](../../contracts/v2/ontologies/ObjectType/get_outgoing_link_type.md) | Resolve one outgoing relationship by the selected type/link identity. |
| [list_outgoing_link_types](../../contracts/v2/ontologies/ObjectType/list_outgoing_link_types.md) | Enumerate outgoing relationship definitions before authoring object traversal. |
| [get_outgoing_link_types_by_object_type_rid_batch](../../contracts/v2/ontologies/ObjectType/get_outgoing_link_types_by_object_type_rid_batch.md) | Resolve links for at most100 type RIDs with optional link-RID filtering; inaccessible/missing types are silently omitted. |
| [get_edits_history](../../contracts/v2/ontologies/ObjectType/get_edits_history.md) | Read object additions/modifications/deletions, newest first by default. Its filters are ignored for Object Storage V1 types. |

Keep API names, RIDs and primary-key property names separate in generated code.
Confirm a property's discriminated `dataType` before converting a Python value.
A business value type can add semantics beyond the base storage type; inspect its
linked definition rather than assuming every string or number is interchangeable.
List/batch omissions establish a visibility-limited result and cannot prove an
object type was deleted. Record requested and returned IDs explicitly.

## Worked example

Run from this skill directory:

```bash
python -B examples/rest/079/object_type_schema.py
```

The complete synthetic `Asset` type has string properties `assetId` and `status`;
`assetId` is both primary key and title. The actual SDK retrieves and decodes that
metadata on explicit branch `master`. Assertions check type identity, presence of
key/title properties and the string discriminator. Adapt the Ontology, type and
branch using permitted metadata; do not substitute these names for an undeclared
tenant schema. The example executes no schema mutation or object write.

## Expected result and checks

Check exact identity, branch, primary key and each property needed by the application.
For batches, record omissions; for lists, preserve cursors and partial results.
For history, retain ordering/filter assumptions with the underlying storage version.
Each contract supplies complete request/response/error definitions and actual sync,
async iterator/raw response handling.

## Failures and recovery

Missing metadata requires verifying Ontology/type identity and visibility before
changing application assumptions. Incompatible property types require updating
the application schema or selecting the intended version/branch. A history result
on Object Storage V1 cannot validate that server-side filters were applied.
Pagination exhaustion leaves partial inventory; it is not proof that no other
types or outgoing links exist. These metadata reads alone authorize no subsequent
Action or write.

## Access boundary

Prepared SDK/mock transport fixtures run offline. Actual type visibility, property
definitions, alias resolution, storage version and permissions require authorized
enrollment metadata. The fixture proves local decoding and application checks only.
