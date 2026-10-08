# Ontology types and backing data

[Development guide](../../SKILL.md) | [Ontology overview](../ontology-compute.md)

## Concept and lifecycle

An object type defines the schema of an operational entity. Objects have stable
primary keys; title properties provide readable labels. Backing data maps
columns to properties, while link types connect object identities. Choosing a
display label as a key can accidentally change identity when the label changes.
Schema configuration and indexed object data have separate outcomes.

## Prerequisites

Prepare the selected Ontology, storage mode, resource/project ownership, backing
tables, property types and key/link design. Configuration and indexing require
authorized enrollment access; property/schema visibility does not imply object
visibility. A synthetic mapping fixture validates design assumptions locally.
It cannot create a type or prove indexing and permissions.

## Procedure

1. In Ontology Manager, verify the selected Ontology. Choose New > Create
   object type and use the guided helper.
2. Select the backing datasource. Inspect automatically mapped columns and
   remove properties outside the intended public contract. Datasource-backed
   mapping does not support arbitrary MapType/StructType source columns through
   this creation path. Configure supported property types deliberately.
3. Select a unique, stable primary-key property and a useful title property.
   Check source duplicates before saving. Object Storage v2 duplicate primary
   keys can fail the indexing pipeline. Action-populated types can use the
   supported no-backing-datasource path; verify its storage/configuration limits.
4. Define links with endpoint types, direction names and cardinality. A foreign
   key relationship maps the source property to the target primary key with
   matching types. Many-to-many relationships use a join datasource carrying
   both endpoint keys; every pair must identify the intended objects.
5. Save metadata, mappings, location and security settings. Build/index backing
   data through the configured pipeline and inspect actual object properties
   and both link directions with representative permitted/restricted identities.

## Worked example

Synthetic datasource contract:

| Type | Source fields | Key/title | Link |
| --- | --- | --- | --- |
| Customer | `customer_id:string`, `customer_name:string` | key `customerId`, title `customerName` | reverse `orders` |
| Order | `order_id:string`, `customer_id:string`, `total_cents:long` | key/title `orderId` | `customer` through `customerId` |

Map snake_case source columns to the declared camelCase property API names.
Customer row `c1/Ada` and Order row `o1/c1/1200` should produce two objects and
one Order-to-Customer relationship. Renaming Ada to Grace changes the title
property while retaining Customer identity `c1` and the link from `o1`.

A second Order row with `order_id=o1` violates the key design. A Customer ID
stored as an integer does not match the declared string relationship. A missing
Customer row for `c2` requires an explicit orphan-data policy before claiming
that every Order has a resolved Customer.

Use the [local mapping fixture](../../examples/ontology/model_fixture.py) to
exercise these synthetic rules. Its tables are examples, not a platform schema
definition file. Actual API names and generated SDK resources come from the
configured Ontology and must be verified before consumer code uses them.

## Expected result and checks

The saved schema has stable keys, correct property types and named relationships.
Indexed permitted objects have expected values and traversal endpoints. Check
key uniqueness, nulls and orphans before indexing, then verify actual object
counts/content and link direction separately. Record schema and data evidence;
a saved type alone does not prove that source rows became queryable objects.

## Failures and recovery

For duplicate keys, repair backing data and rebuild; changing display labels
does not repair identity. For missing links, inspect endpoint key types, mapping,
backing branch/index state and visibility. Fix the failing layer and repeat the
specific object/traversal check. Schema changes can break generated consumers;
coordinate versioned contracts and regenerate prepared bindings before release.

Optional provenance: [type creation](https://www.palantir.com/docs/foundry/object-link-types/create-object-type),
[link creation](https://www.palantir.com/docs/foundry/object-link-types/create-link-type),
[object identifiers](https://www.palantir.com/docs/foundry/functions/object-identifiers).
