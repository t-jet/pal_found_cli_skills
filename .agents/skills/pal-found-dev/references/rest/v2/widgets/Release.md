# Widget set releases

[REST catalog](../../catalog.md) | [Widget distribution](../../../widgets/distribution.md)

A release binds a widget-set RID and version to a repository locator. Read the
set first, then choose the exact version. These methods are Private Beta in SDK
1.101.0 and require enrollment support plus access to the target set.

## get

Use `client.widgets.WidgetSet.Release.get(widget_set_rid, release_version,
preview=True)` to retrieve one release. Verify the returned `widgetSetRid`,
`version` and repository locator before using it in a host application.
`ReleaseNotFound` can indicate a wrong set, version or unavailable release;
compare with a bounded list before selecting a replacement. See the
[exact contract](../../contracts/v2/widgets/Release/get.md) and [offline SDK fixture](../../../../examples/rest/091/v2/widgets/Release/invoke_get.py).

## list

Use `client.widgets.WidgetSet.Release.list(widget_set_rid, page_size=...,
preview=True)` to discover versions. Ordinary sync returns a `ResourceIterator`;
ordinary async returns an `AsyncResourceIterator`. For explicit page control,
use the raw response wrapper and carry `nextPageToken` into `page_token`.
Bound pages and time, reject a repeated token, and record partial results if
the scan stops early. A page may contain fewer or more items than requested.
See the [exact contract](../../contracts/v2/widgets/Release/list.md),
[finite pagination](../../client-behavior.md), and [offline SDK fixture](../../../../examples/rest/091/v2/widgets/Release/invoke_list.py).

## delete

Use `client.widgets.WidgetSet.Release.delete(widget_set_rid, release_version,
preview=True)` only after recording the exact release identity and checking
which hosts refer to it. Success returns `None`. If the request times out,
look up the exact version before deciding whether another delete is needed.
`DeleteReleasePermissionDenied` calls for checking set access; it does not
justify deleting a different version. See the [exact contract](../../contracts/v2/widgets/Release/delete.md)
and [offline SDK fixture](../../../../examples/rest/091/v2/widgets/Release/invoke_delete.py).
