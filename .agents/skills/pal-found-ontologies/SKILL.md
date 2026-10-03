---
name: pal-found-ontologies
description: Offline entry point for Foundry Ontologies API v2 CLI. Documents 67 operations across ontology metadata, object types, objects, object sets, actions, queries, attachments, media, and time series. Navigation to the discovery part (DEV-046) and the action/rich-property part (DEV-047).
---

# Foundry Ontologies CLI

## Capability and source

Foundry Ontology APIs expose semantic object types, links, actions, queries,
attachments, media, and time-series values. The `pal-found-ontologies` command
maps those concepts to 67 operations across ontology metadata, objects,
object sets, transactions, and property clients.

Source: [Palantir Ontology-aware applications](https://www.palantir.com/docs/foundry/ontology/applications/index.html); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

67 Foundry Ontologies API v2 operations are available through the installed `pal-found-ontologies` command.

## Usage

```bash
pal-found-ontologies <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, and `--batch-pages`.

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

## File layout

```
.agents/skills/pal-found-ontologies/
├── SKILL.md
└── references/
    ├── 01-discovery-metadata.md
    ├── 02-discovery-objects.md
    └── 03-actions-rich-properties.md
```

Copy the entire `pal-found-ontologies` folder, including `references/`, so the
relative links above resolve offline. Parts 01 and 02 (discovery) are owned by
DEV-046; part 03 (actions and rich properties) is owned by DEV-047.
