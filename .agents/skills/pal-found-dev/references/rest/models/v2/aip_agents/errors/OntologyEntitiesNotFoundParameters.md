# foundry_sdk.v2.aip_agents.errors.OntologyEntitiesNotFoundParameters


The error names unavailable Ontology object or link types. Compare each identity with the permitted Ontology metadata before changing the Agent request.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| agentRid | agentRid | aip_agents_models.AgentRid | TypedDict key required | No additional field description in SDK source. |
| sessionRid | sessionRid | typing_extensions.NotRequired[aip_agents_models.SessionRid] | TypedDict key may be omitted | The session RID where the error occurred. This is omitted if the error occurred during session creation. |
| objectTypeRids | objectTypeRids | typing.List[ontologies_models.ObjectTypeRid] | TypedDict key required | No additional field description in SDK source. |
| linkTypeRids | linkTypeRids | typing.List[ontologies_models.LinkTypeRid] | TypedDict key required | No additional field description in SDK source. |

```python
class OntologyEntitiesNotFoundParameters(typing_extensions.TypedDict):
    """
    Some ontology types are configured for use by the Agent but could not be found.
    The types either do not exist or the client token does not have access.
    Object types and their link types can be checked by listing available object/link types through the API, or searching in [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: typing_extensions.NotRequired[aip_agents_models.SessionRid]
    """The session RID where the error occurred. This is omitted if the error occurred during session creation."""

    objectTypeRids: typing.List[ontologies_models.ObjectTypeRid]
    linkTypeRids: typing.List[ontologies_models.LinkTypeRid]
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.AgentRid](../models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../models/SessionRid.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeRid](../../ontologies/models/LinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeRid](../../ontologies/models/ObjectTypeRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyEntitiesNotFoundParameters.md)
