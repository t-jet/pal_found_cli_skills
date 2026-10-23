# Data Health configuration contracts

[Checks and reports](01-check-report.md) | [Data Health skill](../SKILL.md)

A configuration selects the health signal, monitored dataset/branch and failure
policy. `CheckConfig` is a union selected by the JSON `type` field. Each create
variant contains a dataset subject. `ReplaceCheckConfig` selects the same type
and changes the replacement fields shown in its local contract; it retains the
subject and any fields absent from the replacement contract.

## Select a rule

| Type and complete local contract | Signal |
| --- | --- |
| [`numericColumnRange`](check-config/numericColumnRange.md) | Checks that values in a numeric column fall within a specified range. |
| [`jobStatus`](check-config/jobStatus.md) | Checks the status of the most recent job run on the dataset. |
| [`numericColumnMean`](check-config/numericColumnMean.md) | Checks the mean value of a numeric column. |
| [`dateColumnRange`](check-config/dateColumnRange.md) | Checks that values in a date column fall within a specified range. |
| [`jobDuration`](check-config/jobDuration.md) | Checks the total time a job takes to complete. |
| [`approximateUniquePercentage`](check-config/approximateUniquePercentage.md) | Checks the approximate percentage of unique values in a specific column. |
| [`buildStatus`](check-config/buildStatus.md) | Checks the status of the most recent build of the dataset. |
| [`columnType`](check-config/columnType.md) | Checks the existence and optionally the type of a specific column. |
| [`allowedColumnValues`](check-config/allowedColumnValues.md) | Checks that values in a column are within an allowed set of values. |
| [`timeSinceLastUpdated`](check-config/timeSinceLastUpdated.md) | Checks the total time since the dataset has updated. |
| [`nullPercentage`](check-config/nullPercentage.md) | Checks the percentage of null values in a specific column. |
| [`totalColumnCount`](check-config/totalColumnCount.md) | Checks the total number of columns in the dataset. |
| [`numericColumnMedian`](check-config/numericColumnMedian.md) | Checks the median value of a numeric column. |
| [`buildDuration`](check-config/buildDuration.md) | Checks the total time a build takes to complete. |
| [`schemaComparison`](check-config/schemaComparison.md) | Checks the dataset schema against an expected schema. |
| [`primaryKey`](check-config/primaryKey.md) | Checks the uniqueness and non-null values of one or more columns (primary key constraint). |

## Author and validate a configuration

1. Inspect the dataset branch/schema and saved check when replacing. Identify
   the monitored signal and the failure condition appropriate to the business.
2. Open its local contract above. Preserve exact camelCase JSON fields and
   `type`; follow nested model links for every bound, severity and value union.
3. Set the dataset subject for creation. Select `MODERATE` or `CRITICAL` where
   required. Numeric/time/date/percentage bounds carry their own field names
   and units; seconds are not milliseconds. Date values use date-time strings.
4. For numeric mean/median configuration, supply at least one of `numericBounds`
   or `trend`. Trend needs at least one of `trendType` or `differenceBounds`.
   Both checks may be provided. SDK structure validation alone does not enforce
   every semantic rule described by these model contracts.
   Percentage configuration needs at least one of `percentageBounds` or
   `medianDeviation`. Time and transaction-time configuration need at least
   one of `timeBounds` or `medianDeviation`. Nullable/default fields do not
   permit omitting both checks; Foundry rejects those empty configurations.
5. For `allowedColumnValues`, give every value its own `type` (`string`,
   `numeric`, `boolean` or `date`) and matching `value`. `allowNull` controls
   the optional null policy. A JSON boolean is not a quoted string.
6. Validate locally against the prepared SDK and the field contracts above.
   Then pass the adapted JSON to `check create` or `check replace` from the
   local [operation guide](01-check-report.md). Read the saved check and
   subsequent reports to verify configuration and actual evaluation separately.

`primaryKey` creation specifies column names; its replacement configuration
changes severity, retaining those names. Column type and numeric/percentage
replacement shapes similarly retain fields omitted from their replace tables.
For schema comparison, the configured enum distinguishes ordered/unordered
exact matching from allowed additions. Preserve the expected schema and chosen
comparison mode deliberately when modifying its policy.

## Local examples and operational boundaries

Every variant guide includes complete create/replace JSON and all recursive
model links. The examples target prepared `foundry-platform-sdk==1.101.0`.
They use synthetic resource and column values; adapt them to your authorized
dataset and schema. The union has 16 variants. A server/enrollment may restrict
availability even when the prepared model can parse its JSON.

Local parsing is not a substitute for server validation. The prepared SDK
parses all 16 create and 16 replace payloads but rejects a wrong `type`, a
create payload without its `subject`, and a `statusCheckConfig` whose
`severity` is not a valid enum value. Cross-field choices are not enforced by
SDK parsing: numeric mean/median configuration needs `numericBounds` or
`trend`; a `trend` needs `trendType` or `differenceBounds`; percentage
configuration needs `percentageBounds` or `medianDeviation`; and time and
transaction-time configuration each need `timeBounds` or `medianDeviation`.
An empty `timeCheckConfig` is an invalid duration rule, and
`ignoreEmptyTransactions` alone is an invalid transaction-time rule. Check
these constraints yourself before submitting. Pydantic may coerce some inputs
and the SDK permits extra properties; successful parsing is not proof that an
unknown field or a semantically inconsistent policy is accepted by Foundry.

Saving and evaluating checks requires authorized enrollment connectivity and
resource permissions. Creation is not evaluation; an empty latest-report list
can mean no report exists yet. Reading a report does not run a check. An unhealthy
report concerns the dataset signal, while an API error concerns the request.

If validation fails, inspect the exact field/type and nested contract before
retrying. If saving is denied, resolve permissions or capability availability.
After an uncertain create, reconcile the observed check identity and effects
before repeating the request. If evaluation is unhealthy, investigate the
actual branch/schema/build or data condition; weakening a severity does not
repair data. Keep saved check identity and report evidence for later comparison.
