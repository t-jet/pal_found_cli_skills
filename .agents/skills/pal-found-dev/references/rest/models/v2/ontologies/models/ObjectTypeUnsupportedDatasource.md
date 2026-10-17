# foundry_sdk.v2.ontologies.models.ObjectTypeUnsupportedDatasource


A datasource of a kind not yet exposed in the public API. The `unsupportedType` discriminator supplies the
underlying OMS variant so callers can recognize known but unmodelled cases (e.g., derived properties). Variants
the adapter does not recognise at all are returned with an `"unknown"` discriminator. The `properties` list
enumerates the property API names this datasource backs. The `properties` will be empty for `"unknown"`
datasources.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| unsupported_type | unsupportedType | str | required; no default | A short, stable discriminator naming the underlying OMS variant. E.g., `"derivedProperties"` for<br>    derived-properties datasources or `"unknown"` for variants the adapter does not recognize. |
| properties | properties | typing.List[PropertyApiName] | required; no default | The property API names that this datasource backs. |
| type | type | typing.Literal['unsupported'] | 'unsupported' | No additional field description in SDK source. |

```python
class ObjectTypeUnsupportedDatasource(core.ModelBase):
    """
    A datasource of a kind not yet exposed in the public API. The `unsupportedType` discriminator supplies the
    underlying OMS variant so callers can recognize known but unmodelled cases (e.g., derived properties). Variants
    the adapter does not recognise at all are returned with an `"unknown"` discriminator. The `properties` list
    enumerates the property API names this datasource backs. The `properties` will be empty for `"unknown"`
    datasources.
    """

    unsupported_type: str = pydantic.Field(alias=str("unsupportedType"))  # type: ignore[literal-required]
    """
    A short, stable discriminator naming the underlying OMS variant. E.g., `"derivedProperties"` for
    derived-properties datasources or `"unknown"` for variants the adapter does not recognize.
    """

    properties: typing.List[PropertyApiName]
    """The property API names that this datasource backs."""

    type: typing.Literal["unsupported"] = "unsupported"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeUnsupportedDatasource.md)
