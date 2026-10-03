# Check and check-report operations

This part documents the `check` (4) and `check_report` (2) resource clients (6
operations). A check defines a data-quality rule; a check report records a
run's outcome.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/data_health/scripts/pal_found_data_health_cli.py`;
SDK `foundry_sdk/v2/data_health/{check,check_report}.py` at pinned commit
`2da67907`. Reviewer architect (CODEREVIEW-048), 2026-10-03. QA baseline
TESTCASE-020.

## Operation records

### check.create

- **Class**: create (write). Defines a new data-health check.
- **Preconditions**: can create checks; a dataset target and rule.
- **Effect**: creates a check that will evaluate the target.
- **Inputs**: `--display-name`, target dataset/rule JSON.
- **Success**: the created check, including its RID.
- **Failure**: exit 1 invalid rule; exit 8 readonly block.
- **Example**: `pal-found-data-health check create --display-name "No nulls in id" --dataset-rid <DATASET_RID> --rule-json '{}'`.

### check.delete

- **Class**: delete (write). Deletes a check.
- **Preconditions**: can delete the check.
- **Effect**: removes the check definition; reports remain historical.
- **Inputs**: positional `check_rid`.
- **Success**: returns the deleted check.

### check.get

- **Class**: read. Returns a check definition.
- **Preconditions**: can read the check.
- **Effect**: returns the check.
- **Inputs**: positional `check_rid`.
- **Success**: the check record.
- **Failure**: exit 4 if missing.

### check.replace

- **Class**: change (write). Replaces a check definition.
- **Preconditions**: can write the check.
- **Effect**: replaces the check's rule/target.
- **Inputs**: positional `check_rid`; replacement fields.
- **Success**: the updated check.

### check_report.get

- **Class**: read. Returns a check report.
- **Preconditions**: can read the check/report.
- **Effect**: returns the report for a specific check run.
- **Inputs**: positional `check_rid`, `check_report_rid`.
- **Success**: the report.
- **Failure**: exit 4 if report missing.

### check_report.get_latest

- **Class**: read. Returns the latest check report.
- **Preconditions**: can read the check.
- **Effect**: returns the most recent report for the check.
- **Inputs**: positional `check_rid`; routed through the nested
  Check.CheckReport accessor.
- **Success**: the latest report.
- **Failure**: exit 4 if no report yet (check never ran).

## Evidence and review

Reviewed against the installed `pal-found-data-health` parser and pinned SDK
sources (commit `2da67907`). `check.create/delete/replace` write; `check_report`
operations read run results. `get_latest` returns nothing until the check has
run; an empty/not-found outcome is valid for a never-run check. No unsupported
operation is documented as callable.
