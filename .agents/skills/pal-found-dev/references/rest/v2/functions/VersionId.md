# Pinned value type version

[Functions operations](index.md) | [Value type discovery](ValueType.md)

## Concept and prerequisites

VersionId `get` retrieves one version of a ValueType by its RID and version ID. Use it when an application must interpret parameters or results according to a stable schema rather than whichever version is latest. Obtain both identifiers from published metadata and verify authorized enrollment access for live reads.

## Procedure and worked example

Call [VersionId.get](../../contracts/v2/functions/VersionId/get.md) with `value_type_rid` and `version_id_version_id`. Preserve both values with the code or persisted record that depends on the schema. The [offline SDK fixture](../../../../examples/rest/085/v2/functions/VersionId/invoke_get.py) checks both path fields, response decoding and named failures. Run it from the skill root with `python -B` followed by the linked example path.

## Expected result, recovery and access boundary

Compare the returned RID and version with the requested pair. If either identifier is unavailable, first resolve the published ValueType metadata; substituting latest would change the application contract. A missing or denied version needs identity and permission checks. Retrying a read after a transient timeout does not mutate a value type. The fixture runs without tenant access and cannot establish that a version exists in the enrollment.
