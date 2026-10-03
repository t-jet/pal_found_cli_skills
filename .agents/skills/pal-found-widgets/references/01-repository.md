# Widget repository and settings operations

This part documents the `dev_mode_settings` (2), `release` (3), `repository`
(2), and `widget_set` (1) resource clients (8 operations). A widget-set
repository holds widget code; releases are taggable builds; dev-mode settings
control runtime overrides.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/widgets/scripts/pal_found_widgets_cli.py`;
SDK `foundry_sdk/v2/widgets/{dev_mode_settings,release,repository,widget_set}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-054), 2026-10-03.
QA baseline TESTCASE-022.

## Operation records

### dev_mode_settings.enable

- **Class**: change (write). Enables dev mode.
- **Preconditions**: can write dev-mode settings.
- **Effect**: turns on dev mode for the widget runtime.
- **Inputs**: settings/scope context.
- **Success**: returns the updated dev-mode settings.

### dev_mode_settings.set_widget_set_by_id

- **Class**: change (write). Sets the active widget set by its id.
- **Preconditions**: can write dev-mode settings.
- **Effect**: points dev mode at a specific widget set.
- **Inputs**: `--settings-json` (`WidgetSetDevModeSettingsById` payload),
  `--widget-set-rid`.
- **Success**: returns the updated settings.
- **Example**: `pal-found-widgets dev-mode-settings set-widget-set-by-id --widget-set-rid <WIDGET_SET_RID> --settings-json '{}'`.

### release.delete

- **Class**: delete (write). Deletes a widget release.
- **Preconditions**: can delete the release.
- **Effect**: removes the release.
- **Inputs**: positional `widget_set_repository_rid`, `release`.
- **Success**: returns the deleted release.

### release.get

- **Class**: read. Returns a widget release.
- **Preconditions**: can read the release.
- **Effect**: returns the release record.
- **Inputs**: positional `widget_set_repository_rid`, `release`.
- **Success**: the release.
- **Failure**: exit 4 if missing.

### release.list

- **Class**: read. Lists releases of a repository.
- **Preconditions**: can read the repository.
- **Effect**: returns releases, paged.
- **Inputs**: positional `widget_set_repository_rid`; paging options.
- **Success**: releases; empty if none.

### repository.get

- **Class**: read. Returns a widget-set repository.
- **Preconditions**: can read the repository.
- **Effect**: returns the repository record.
- **Inputs**: positional `widget_set_repository_rid`.
- **Success**: the repository.
- **Failure**: exit 4 if missing.

### repository.publish

- **Class**: create (binary upload). Publishes a new widget release.
- **Preconditions**: can write the repository.
- **Effect**: stores a release build (zip) and publishes it.
- **Inputs**: positional `widget_set_repository_rid`; `--file` (bounded zip
  with a `.palantir/widgets.config.json` manifest), `--repository-version`.
- **Success**: the published release.
- **Failure**: exit 1 missing/invalid manifest or too-large file; exit 8
  readonly block.
- **Example**: `pal-found-widgets repository publish <REPOSITORY_RID> --file ./repo.zip --repository-version 1.0.0`.

### widget_set.get

- **Class**: read. Returns a widget set.
- **Preconditions**: can read the widget set.
- **Effect**: returns the widget set.
- **Inputs**: positional `widget_set_rid`.
- **Success**: the widget set.
- **Failure**: exit 4 if missing.

## Evidence and review

Reviewed against the installed `pal-found-widgets` parser and pinned SDK
sources (commit `2da67907`). Dev-mode settings writes and repository publish
write with material runtime/release effects; publish is a bounded zip upload
(AC-D-013-09). The four legacy `dev-mode-settings` operations
(disable/get/pause/set-widget-set) are unsupported negatives and are not
documented as callable here. No other unsupported operation is documented as
callable.
