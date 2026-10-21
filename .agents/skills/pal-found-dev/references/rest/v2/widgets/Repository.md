# Widget repositories and publication

[REST catalog](../../catalog.md) | [Widget distribution](../../../widgets/distribution.md)

A repository holds widget-set content. A release refers to a repository
version. Read the repository RID and intended widget-set identity before
publishing. SDK 1.101.0 marks these methods Private Beta.

## get

Call `client.widgets.Repository.get(repository_rid, preview=True)` and
inspect the returned repository identity before using it as a publication
target. `RepositoryNotFound` requires checking the RID and access. Read the
[exact contract](../../contracts/v2/widgets/Repository/get.md) and run the
[offline SDK fixture](../../../../examples/rest/091/v2/widgets/Repository/invoke_get.py).

## publish

Prepare a ZIP file as `bytes` and include a valid manifest at
`.palantir/widgets.config.json`. Choose a `repository_version` for that
content. Call `client.widgets.Repository.publish(repository_rid,
body=zip_bytes, repository_version=..., preview=True)`. The returned
`Release` identifies the published widget-set version and locator; check those
fields against the intended repository and version. The method is a write;
after an uncertain response, read the resulting release and repository state
before repeating it. `PublishReleasePermissionDenied` requires checking
publication access. The [exact contract](../../contracts/v2/widgets/Repository/publish.md)
defines the byte body and response model. The [offline SDK fixture](../../../../examples/rest/091/v2/widgets/Repository/invoke_publish.py)
checks the request bytes and decoded result without publishing to a tenant.
Its small in-memory ZIP checks the transport shape and manifest path. For a
real publication, use a built widget artifact and inspect its manifest against
the widget build configuration; this fixture does not validate tenant manifest
semantics.

For an adaptable publication input, build the widget project first and use
its generated `dist/.palantir/widgets.config.json` with the built entry
assets. The widget build plugin generates the manifest; its version must match
the intended release. Keep the manifest and assets at the ZIP root, with no
wrapping `dist/` directory:

```python
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile
import json

dist = Path("dist")
manifest = dist / ".palantir" / "widgets.config.json"
assert manifest.is_file(), "Build the widget set before publishing"
assert isinstance(json.loads(manifest.read_text(encoding="utf-8")), dict)
html_entries = [item for item in dist.glob("*.html") if item.is_file()]
assert html_entries, "Built widget entry HTML is missing"
archive_bytes = BytesIO()
with ZipFile(archive_bytes, "w") as archive:
    for asset in sorted(dist.rglob("*")):
        if asset.is_file():
            archive.write(asset, asset.relative_to(dist).as_posix())
with ZipFile(BytesIO(archive_bytes.getvalue())) as archive:
    assert ".palantir/widgets.config.json" in archive.namelist()
    assert all(item.name in archive.namelist() for item in html_entries)
release = client.widgets.Repository.publish(
    repository_rid, body=archive_bytes.getvalue(),
    repository_version=approved_version, request_timeout=30,
)
assert release.locator.repository_rid == repository_rid
assert release.locator.repository_version == approved_version
```

Check the generated manifest's release version against `approved_version`
before calling publish. The exact manifest contents come from the local build;
the transport fixture's synthetic manifest is not a substitute for one.
