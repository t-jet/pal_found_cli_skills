# foundry_sdk.v2.ontologies.models.ReferenceSigningOptions


Options for signing references in the response.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| sign_media_references | signMediaReferences | typing.Optional[bool] | default None | Deprecated and ignored. Media references backed by a media set view are signed by default:<br>    the response includes a `token` on each `MediaReference` value that can be used to access the<br>    referenced media item directly, enabling item-level access control (the caller needs access to<br>    the object whose property holds the reference, not view access on the parent media set).<br><br>    This field no longer has any effect; setting it to true or false is ignored. Arrays of media<br>    references are not signed. |

```python
class ReferenceSigningOptions(core.ModelBase):
    """Options for signing references in the response."""

    sign_media_references: typing.Optional[bool] = pydantic.Field(alias=str("signMediaReferences"), default=None)  # type: ignore[literal-required]
    """
    Deprecated and ignored. Media references backed by a media set view are signed by default:
    the response includes a `token` on each `MediaReference` value that can be used to access the
    referenced media item directly, enabling item-level access control (the caller needs access to
    the object whose property holds the reference, not view access on the parent media set).

    This field no longer has any effect; setting it to true or false is ignored. Arrays of media
    references are not signed.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReferenceSigningOptions.md)
