# Widget repositories and publication

[REST catalog](../../catalog.md) | [Widget distribution](../../../widgets/distribution.md)

A repository holds widget-set content. A release refers to a repository
version. Read the repository RID and intended widget-set identity before
publishing. SDK 1.101.0 marks these methods Private Beta.

## get

Call `client.widgets.repository.get(repository_rid, preview=True)` and
inspect the returned repository identity before using it as a publication
target. `RepositoryNotFound` requires checking the RID and access. Read the
[exact contract](../../contracts/v2/widgets/Repository/get.md) and run the
[offline SDK fixture](../../../../examples/rest/091/v2/widgets/Repository/invoke_get.py).

## publish

Prepare a ZIP file as `bytes` and include a valid manifest at
`.palantir/widgets.config.json`. Choose a `repository_version` for that
content. Call `client.widgets.repository.publish(repository_rid,
body=zip_bytes, repository_version=..., preview=True)`. The returned
`Release` identifies the published widget-set version and locator; check those
fields against the intended repository and version. The method is a write;
after an uncertain response, read the resulting release and repository state
before repeating it. `PublishReleasePermissionDenied` requires checking
publication access. The [exact contract](../../contracts/v2/widgets/Repository/publish.md)
defines the byte body and response model. The [offline SDK fixture](../../../../examples/rest/091/v2/widgets/Repository/invoke_publish.py)
checks the request bytes and decoded result without publishing to a tenant.
