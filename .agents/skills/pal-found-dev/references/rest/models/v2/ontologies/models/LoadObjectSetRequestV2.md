# foundry_sdk.v2.ontologies.models.LoadObjectSetRequestV2


Represents the API POST body when loading an `ObjectSet`.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_set | objectSet | ObjectSet | required; no default | No additional field description in SDK source. |
| order_by | orderBy | typing.Optional[SearchOrderByV2] | default None | No additional field description in SDK source. |
| select | select | typing.List[SelectedPropertyApiName] | required; no default | No additional field description in SDK source. |
| select_v2 | selectV2 | typing.Optional[typing.List[PropertyIdentifier]] | default None | The identifiers of the properties to include in the response. Only selectV2 or select should be populated,<br>    but not both. |
| page_token | pageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| page_size | pageSize | typing.Optional[core_models.PageSize] | default None | No additional field description in SDK source. |
| exclude_rid | excludeRid | typing.Optional[bool] | default None | A flag to exclude the retrieval of the `__rid` property.<br>    Setting this to true may improve performance of this endpoint for object types in OSV2. |
| load_property_securities | loadPropertySecurities | typing.Optional[bool] | default None | A flag to load the securities for all properties.<br>    Setting this flag to true will return a list of securities in the `propertySecurities` field of the response.<br>    Returned objects will return all properties as Secured Property Values, which provide the property data<br>    as well an index into the `propertySecurities` list.<br>    This feature is experimental and not yet generally available. |
| snapshot | snapshot | typing.Optional[bool] | None | A flag to use snapshot consistency when paging.<br>    Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items.<br>    Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items.<br>    This defaults to false if not specified, which means you will always get the latest results. |
| include_compute_usage | includeComputeUsage | typing.Optional[core_models.IncludeComputeUsage] | default None | No additional field description in SDK source. |
| reference_signing_options | referenceSigningOptions | typing.Optional[ReferenceSigningOptions] | default None | No additional field description in SDK source. |

```python
class LoadObjectSetRequestV2(core.ModelBase):
    """Represents the API POST body when loading an `ObjectSet`."""

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    order_by: typing.Optional[SearchOrderByV2] = pydantic.Field(alias=str("orderBy"), default=None)  # type: ignore[literal-required]
    select: typing.List[SelectedPropertyApiName]
    select_v2: typing.Optional[typing.List[PropertyIdentifier]] = pydantic.Field(alias=str("selectV2"), default=None)  # type: ignore[literal-required]
    """
    The identifiers of the properties to include in the response. Only selectV2 or select should be populated,
    but not both.
    """

    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)  # type: ignore[literal-required]
    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    exclude_rid: typing.Optional[bool] = pydantic.Field(alias=str("excludeRid"), default=None)  # type: ignore[literal-required]
    """
    A flag to exclude the retrieval of the `__rid` property.
    Setting this to true may improve performance of this endpoint for object types in OSV2.
    """

    load_property_securities: typing.Optional[bool] = pydantic.Field(alias=str("loadPropertySecurities"), default=None)  # type: ignore[literal-required]
    """
    A flag to load the securities for all properties.
    Setting this flag to true will return a list of securities in the `propertySecurities` field of the response.
    Returned objects will return all properties as Secured Property Values, which provide the property data
    as well an index into the `propertySecurities` list.
    This feature is experimental and not yet generally available.
    """

    snapshot: typing.Optional[bool] = None
    """
    A flag to use snapshot consistency when paging.
    Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items.
    Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items.
    This defaults to false if not specified, which means you will always get the latest results.
    """

    include_compute_usage: typing.Optional[core_models.IncludeComputeUsage] = pydantic.Field(alias=str("includeComputeUsage"), default=None)  # type: ignore[literal-required]
    reference_signing_options: typing.Optional[ReferenceSigningOptions] = pydantic.Field(alias=str("referenceSigningOptions"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.IncludeComputeUsage](../../core/models/IncludeComputeUsage.md)
- [foundry_sdk.v2.core.models.PageSize](../../core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.ontologies.models.ObjectSet](ObjectSet.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](PropertyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.ReferenceSigningOptions](ReferenceSigningOptions.md)
- [foundry_sdk.v2.ontologies.models.SearchOrderByV2](SearchOrderByV2.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApiName](SelectedPropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LoadObjectSetRequestV2.md)
