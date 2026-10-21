# foundry_sdk.v2.ontologies.models.SynchronousWebhookOutputArgument


Represents a synchronous webhook output argument in a logic rule.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| webhook_output_param_name | webhookOutputParamName | str | required; no default | The name of the webhook output parameter. |
| type | type | typing.Literal['synchronousWebhookOutput'] | 'synchronousWebhookOutput' | No additional field description in SDK source. |

```python
class SynchronousWebhookOutputArgument(core.ModelBase):
    """Represents a synchronous webhook output argument in a logic rule."""

    webhook_output_param_name: str = pydantic.Field(alias=str("webhookOutputParamName"))  # type: ignore[literal-required]
    """The name of the webhook output parameter."""

    type: typing.Literal["synchronousWebhookOutput"] = "synchronousWebhookOutput"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SynchronousWebhookOutputArgument.md)
