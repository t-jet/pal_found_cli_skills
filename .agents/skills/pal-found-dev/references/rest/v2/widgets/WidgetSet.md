# Widget set identity

[REST catalog](../../catalog.md) | [Widget development lifecycle](../../../widgets/lifecycle.md)

Use the widget-set RID to relate dev settings, repositories and releases.
`client.widgets.WidgetSet.get(widget_set_rid, preview=True)` returns the
set metadata without changing it. Check the returned RID and relevant
repository or release information before selecting another operation. In SDK
1.101.0 this is Private Beta; check availability and resource access first.

`WidgetSetNotFound` calls for checking the RID and visibility. It does not
establish that the set can be created through this SDK resource. See the
[exact contract](../../contracts/v2/widgets/WidgetSet/get.md) and run the
[offline SDK fixture](../../../../examples/rest/091/v2/widgets/WidgetSet/invoke_get.py).
