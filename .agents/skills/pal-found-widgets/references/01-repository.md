# Widget repository and settings operations

`repository` commands take repository RID. `widget-set` and `release`
commands take widget set RID; releases use semantic version. Dev mode applies
to user associated with CLI token. Examples use `REPOSITORY_RID` and
`WIDGET_SET_RID` shell variables. Input errors exit 1, SDK permission denials
exit 3, missing resources exit 4, and read-only policy blocks writes (8).
Server may conceal a denial as 404. SDK: `docs/v2/Widgets/`.

### dev_mode_settings.enable

Enables dev mode for user associated with CLI token. Response contains dev
mode `status` and `widgetSetSettings` map. This does not publish widget code
or affect other users. Development server and matching overrides must exist
for widget to show unpublished assets; otherwise host shows published build.
Session expires after 24 hours. A new widget needs first published release
before Workshop can select it; playground can preview it sooner. Permission
or disabled feature can reject request.

**Example:** `pal-found-widgets dev-mode-settings enable`

### dev_mode_settings.set_widget_set_by_id

Sets dev mode overrides for one widget set, identifying widgets by widget ID.
Requires widget set RID and JSON settings object matching SDK's
`WidgetSetDevModeSettingsById`: `baseHref` is HTML base path;
`widgetSettings` maps widget IDs to `scriptEntrypoints` and
`stylesheetEntrypoints` file paths. A script entrypoint also has `scriptType`.
Response contains updated `status` and settings map for token's user.
Malformed JSON or inaccessible set can fail.

**Example:** `pal-found-widgets dev-mode-settings set-widget-set-by-id --widget-set-rid "$WIDGET_SET_RID" --settings-json '{"baseHref":"/","widgetSettings":{"myCustomWidget":{"scriptEntrypoints":[{"filePath":"dist/app.js","scriptType":"DEFAULT"}],"stylesheetEntrypoints":[{"filePath":"dist/app.css"}]}}}'`

### release.delete

Deletes named release from widget set. Positional widget set RID and semantic
release version identify target. Successful call returns no body. Check which
version host applications use before deletion; missing release or delete
permission fails.

**Example:** `pal-found-widgets release delete "$WIDGET_SET_RID" 1.2.0`

### release.get

Retrieves release by positional widget set RID and semantic version. Response
contains widget set RID, version, optional description, and locator with
repository RID/version holding build files. Missing release or read
permission fails.

**Example:** `pal-found-widgets release get "$WIDGET_SET_RID" 1.2.0`

### release.list

Lists releases of positional widget set RID. Response has `data` array and
optional `nextPageToken`; server may return page of different size than
`--page-size` request. Omit `--page-token` on first page, then pass returned
token for next. `--all --max-pages` bounds automatic traversal. Missing
widget set or read access fails.

**Example:** `pal-found-widgets release list "$WIDGET_SET_RID" --page-size 50`

### repository.get

Retrieves repository by positional repository RID. Response contains RID and
optional `widgetSetRid` authorized to publish from this repository. Confirm
authorization target before publishing. Absent repository or read denial
fails.

**Example:** `pal-found-widgets repository get "$REPOSITORY_RID"`

### repository.publish

Publishes new release from zipped widget build. Requires repository RID,
`--repository-version`, and existing `--file` no larger than 16 MiB. Archive
must contain valid `.palantir/widgets.config.json` manifest describing build.
Response is Release with widget set RID, release version, and backing
repository locator. Invalid archive, version conflict, or missing publish
permission fails. Host applications must select new version to display it.

**Example:** `pal-found-widgets repository publish "$REPOSITORY_RID" --repository-version 1.2.0 --file ./widgets.zip`

### widget_set.get

Retrieves widget set by positional RID. Response contains widget set RID and
optional `publishRepositoryRid` authorized to publish releases. Use that
repository RID with `repository publish`; missing set or read permission
fails.

**Example:** `pal-found-widgets widget-set get "$WIDGET_SET_RID"`
