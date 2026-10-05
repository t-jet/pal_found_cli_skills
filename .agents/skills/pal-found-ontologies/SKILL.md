---
name: pal-found-ontologies
description: Understand Foundry's operational Ontology and use 67 Ontologies API v2 CLI operations for type discovery, object queries, Actions, rich properties, and transactions.
---

# Foundry Ontologies CLI

## Capability and source

The Ontology is Foundry's operational representation of an organization. It
maps data and models to business entities such as orders, equipment, and
transactions. Object types define entities and their properties; link types
define relationships. Objects and links carry the current values. Interfaces
let applications address compatible object types through a common contract.
Object sets select objects for search, loading, and aggregation. These concepts
give users and applications a shared account of what data means, not merely
where it is stored. See Palantir's [Ontology overview](https://www.palantir.com/docs/foundry/ontology/overview)
and [platform overview](https://www.palantir.com/docs/foundry/platform-overview/overview).

Source: Palantir's Ontology, platform, and action type overviews linked in
this section; the operation records below explain each supported command.
`Ontologies` documentation.

Actions are the Ontology's controlled write path. An action type defines
parameters, validation, permissions, and the edits or external effects that
execution may perform. A query type exposes reusable logic; attachment,
media, and time-series properties attach richer values to objects. Discover
types before constructing object queries or action payloads, and inspect an
action response's validation result before treating the edit as applied.
Object Storage V1 edits may take time to become visible; V2 edits are visible
when the action completes. See Palantir's [action type overview](https://www.palantir.com/docs/foundry/action-types/overview)
and the SDK `Ontologies/Action.md` method description.

67 Foundry Ontologies API v2 operations are exposed by `pal-found-ontologies`. Its scope is existing
ontology metadata and runtime data; each resource page states whether a call
reads, executes, or changes state.

## Usage

```bash
pal-found-ontologies <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, and `--batch-pages`.

`--timeout` sets the request timeout in seconds. `--format` selects JSON,
TOON, or automatic structured output; `--pretty` indents it. For paged
operations, `--page-size` requests entries per page, `--page-token` resumes
from a returned cursor, and `--batch-pages` bounds how many pages this call
fetches.

Binary downloads use the shared download handler and return a metadata
envelope with the saved file path and checksums. Binary uploads use
`--body-file`; `--content-length` is inferred when omitted.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

The 67 operations are split into two disjoint parts. The discovery part
(DEV-046) covers reading the ontology model; the action/rich-property part
(DEV-047) covers executing actions and reading attachments, media, and time
series.

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Discovery: ontology metadata and model](references/01-discovery-metadata.md) | `ontology`, `ontology_value_type`, `object_type`, `action_type`, `action_type_full_metadata`, `query_type` | 21 |
| [Discovery: linked objects and ontology objects](references/02-discovery-objects.md) | `linked_object`, `ontology_object` | 7 |
| [Actions and rich properties](references/03-actions-rich-properties.md) | `action`, `attachment`, `attachment_property`, `cipher_text_property`, `geotemporal_series_property`, `media_reference_property`, `ontology_interface`, `ontology_object_set`, `ontology_transaction`, `query`, `time_series_property_v2`, `time_series_value_bank_property` | 39 |

## Parameters and JSON

Read [identifiers and JSON inputs](references/inputs.md) before constructing
action payloads, object sets, or property requests.

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paginated operations add `--page-size`, `--page-token`, and
`--batch-pages`. JSON variants include `--parameters`, `--attribution`,
`--filters`, `--aggregation`, `--group-by`, `--order-by`, `--where`,
`--select`, `--select-v2`, `--options`, `--requests`, `--request`, `--edits`,
`--overrides`, `--links`, `--object-types`, `--interface-types`,
`--action-types`, `--query-types`, `--augmented-properties`,
`--augmented-interface-property-types`, `--augmented-shared-property-types`,
`--selected-object-types`, `--selected-interface-property-types`,
`--selected-shared-property-types`, `--object-type-api-names`, and `--range`
where help shows them. Binary attachment/media operations use `--body-file`,
`--output-filename`, `--content-type`, `--content-length`, `--filename`, and
`--media-item-path`. Positional variants are the ontology, object, link,
action, query, property, and transaction identifiers listed by help; `--preview`,
`--branch`, `--sdk-package-rid`, `--sdk-version`, `--version`, and
`--transaction-id` are optional scalar variants. Additional scalar choices and
switches are `--accuracy`, `--aggregate`, `--exclude-rid`,
`--include-all-previous-properties`, `--include-compute-usage`,
`--link-types`, `--load-property-securities`, `--object-primary-key`,
`--object-set`, `--other-interface-types`, `--snapshot`, `--sort-order`, and
`--stream-format`.

## Install requirement

`pal-found-ontologies` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
