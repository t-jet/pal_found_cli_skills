# Experiment operations

These records describe the `experiment` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

## Reading an experiment

An `Experiment` contains `rid`, `modelRid`, creation identity/time, `branch`,
`source`, `status`, parameters, series summaries, summary metrics, artifacts,
and tags. `status` is `RUNNING`, `SUCCEEDED`, or `FAILED`; optional
`statusMessage` gives additional detail. Optional `linkedModelVersion`
identifies an associated version, and optional `jobRid` identifies its job.
An experiment's success alone does not establish deployment readiness.

`parameters` entries have `name` and a typed `value` (`boolean`, `string`,
`integer`, `double`, or `datetime`, with its own `value`). `series` entries
have `name`, optional `length`, and `value` with `type=double` and optional
`min`, `max`, and `last` aggregations. Missing aggregations were not computed;
they are not zero. `summaryMetrics` entries contain `seriesName`,
`aggregation` (`MIN`, `MAX`, `LAST`), and numeric `value`.
Use `series[].name` for series reads. `artifacts` maps names to metadata
containing `name`, optional `description`, `sizeBytes`, and `details`;
SDK 1.101.0 table details have `type=table` and `rowCount`. Use that artifact
name for artifact-table reads. A metadata response does not include raw rows.

## Search JSON

`--where-json` takes one object with a `type` discriminator. Nested filters
use the same shape. SDK 1.101.0 supports:

| `type` | Other required keys and accepted values |
| --- | --- |
| `and`, `or` | `filters`: array of filter objects |
| `not` | `value`: one filter object |
| `eq` | `field`: `STATUS`, `BRANCH`, `EXPERIMENT_NAME`, `EXPERIMENT_RID`, `JOB_RID`, `TAG`, `PARAMETER_NAME`, or `SERIES_NAME`; `value` |
| `contains`, `startsWith` | `field`: `EXPERIMENT_NAME`, `PARAMETER_NAME`, or `SERIES_NAME`; `value` |
| `parameterFilter` | `parameterName`, `operator` (`EQ`, `GT`, `LT`, `CONTAINS`), `value` |
| `seriesFilter` | `seriesName`, `field` (`LENGTH`, `AGGREGATION_MIN`, `AGGREGATION_MAX`, `AGGREGATION_LAST`), `operator` (`EQ`, `GT`, `LT`), `value` |
| `summaryMetricFilter` | `seriesName`, `aggregation` (`MIN`, `MAX`, `LAST`), `operator` (`EQ`, `GT`, `LT`), `value` |

Parameter comparisons bind name and value to the same parameter. `EQ` supports
boolean, double, integer, or datetime values; `GT`/`LT` support double, integer,
or datetime; `CONTAINS` uses a string substring. Series and summary predicates
bind their name and numeric comparison together. The SDK types predicate values
as `Any`; local validation does not prove that a value has valid server semantics.

`--order-by-json` takes `{"field":"CREATED_TIME","direction":"DESC"}`;
fields are `EXPERIMENT_NAME` or `CREATED_TIME`, directions `ASC` or `DESC`.
Omitting ordering uses service relevance ordering. Example filter and ordering:

```bash
pal-found-models experiment search <MODEL_RID> --where-json '{"type":"and","filters":[{"type":"eq","field":"STATUS","value":"SUCCEEDED"},{"type":"parameterFilter","parameterName":"learning_rate","operator":"GT","value":0.01}]}' --order-by-json '{"field":"CREATED_TIME","direction":"DESC"}'
```

Additional shapes: `{"type":"not","value":{"type":"eq","field":"BRANCH","value":"scratch"}}`,
`{"type":"seriesFilter","seriesName":"loss","field":"AGGREGATION_LAST","operator":"LT","value":0.1}`,
and `{"type":"summaryMetricFilter","seriesName":"loss","aggregation":"LAST","operator":"LT","value":0.1}`.
Boolean children may contain any supported filter. Invalid discriminator, field,
or direction fails SDK validation. Correct the JSON before retrying.

### experiment.get

- **Purpose and behavior:** Retrieve a single experiment with all metadata, parameters, series metadata, and summary metrics.
- **CLI inputs:** positionals `model_rid`, `experiment_rid`.
- **Input meaning:** `model_rid`: Resource identifier (RID) of the named Foundry resource. `experiment_rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can inspect its experiments.
- **Result:** Returns `Experiment` for the selected experiment.
- **Failure:** An unknown experiment identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-models experiment get <MODEL_RID> <EXPERIMENT_RID>`

### experiment.search

- **Purpose and behavior:** Search experiments using complex nested queries on experiment metadata, parameters, series, and summary metrics. Supports AND/OR/NOT combinations and various predicates. Returns a maximum of 100 results per page.
- **CLI inputs:** positionals `model_rid`; optional `--page-size`, `--page-token`, `--all`, `--max-pages`, `--order-by-json`, `--where-json`.
- **Input meaning:** `model_rid`: Resource identifier (RID) of the named Foundry resource. `--where-json`: Optional search filter for filtering experiments. If not provided, all experiments for the model are returned. `--order-by-json` sorts experiments using the SDK order-by JSON schema; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from `next_page_token` in the previous call's stderr metadata; omit on the first page. By default, the CLI fetches one page. `--max-pages` fetches up to the given number of pages; `--all` fetches until no cursor remains or the configured limit of at most 40 pages is reached. If both are set, `--all` takes precedence.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model exists and the caller can inspect its experiments.
- **Result:** Prints matching experiment entries as a list on stdout. Pagination metadata, including `next_page_token` when another page exists, follows a separator on stderr. An empty list means this page contains no entries; follow a returned token to check the next page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-models experiment search <MODEL_RID>`
