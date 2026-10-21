# Value type discovery

[Functions operations](index.md) | [REST client behavior](../../client-behavior.md)

## Concept and prerequisites

A ValueType RID identifies a reusable published value schema used by Functions. `get` returns its latest version; the caller must inspect that version before assuming an argument or result contract is unchanged. Prepare SDK 1.101.0 and a known RID. Live metadata requires authorized access; the local fixture uses prepared libraries only.

## Procedure and worked example

Use [ValueType.get](../../contracts/v2/functions/ValueType/get.md) with `value_type_rid`. Inspect the returned RID and current version before binding code to its fields. When reproducibility matters, retain the version ID and use [VersionId.get](VersionId.md) to fetch that exact version on later runs. The [SDK fixture](../../../../examples/rest/085/v2/functions/ValueType/invoke_get.py) checks URL encoding, decoded metadata and named source errors through an offline transport; run it with `python -B` from the skill root.

## Expected result, recovery and access boundary

The returned schema should identify the requested RID and a version usable by the consuming Query. A missing or denied RID calls for checking the selected versioned resource and caller access, not inventing a substitute schema. `get` is a read; bounded retry after transient transport failure is safe when the application still needs the latest version, but the version can advance between attempts. Pin a version for stable code generation. The fixture establishes request handling only; tenant metadata and permissions require enrollment access.
