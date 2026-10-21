# foundry_sdk.v2.admin.errors.PreregisterGroupPermissionDenied


The definition below supplies its fields or permitted values.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | typing.Literal['PreregisterGroupPermissionDenied'] | required; no default | No additional field description in SDK source. |
| parameters | parameters | PreregisterGroupPermissionDeniedParameters | required; no default | No additional field description in SDK source. |
| error_instance_id | error_instance_id | str | required; no default | No additional field description in SDK source. |

```python
@dataclass
class PreregisterGroupPermissionDenied(errors.PermissionDeniedError):
    name: typing.Literal["PreregisterGroupPermissionDenied"]
    parameters: PreregisterGroupPermissionDeniedParameters
    error_instance_id: str
```

## Referenced definitions

- [foundry_sdk.v2.admin.errors.PreregisterGroupPermissionDeniedParameters](PreregisterGroupPermissionDeniedParameters.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PreregisterGroupPermissionDenied.md)
