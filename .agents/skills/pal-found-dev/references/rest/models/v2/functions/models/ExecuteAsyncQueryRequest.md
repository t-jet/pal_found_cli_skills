# foundry_sdk.v2.functions.models.ExecuteAsyncQueryRequest


ExecuteAsyncQueryRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ontology | ontology | typing.Optional[ontologies_models.OntologyIdentifier] | None | Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped<br>    function. When omitted, executes a global function. |
| parameters | parameters | typing.Dict[ParameterId, typing.Optional[DataValue]] | required; no default | No additional field description in SDK source. |
| version | version | typing.Optional[FunctionVersion] | None | The version of the query to execute. When used with `branch`, the specified version must exist on the branch. |
| branch | branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to execute the query from. If not specified, the default branch is used.<br>    When provided without `version`, the latest version on this branch is used.<br>    When provided with `version`, the specified version must exist on the branch. |

```python
class ExecuteAsyncQueryRequest(core.ModelBase):
    """ExecuteAsyncQueryRequest"""

    ontology: typing.Optional[ontologies_models.OntologyIdentifier] = None
    """
    Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped
    function. When omitted, executes a global function.
    """

    parameters: typing.Dict[ParameterId, typing.Optional[DataValue]]
    version: typing.Optional[FunctionVersion] = None
    """The version of the query to execute. When used with `branch`, the specified version must exist on the branch."""

    branch: typing.Optional[core_models.FoundryBranch] = None
    """
    The Foundry branch to execute the query from. If not specified, the default branch is used.
    When provided without `version`, the latest version on this branch is used.
    When provided with `version`, the specified version must exist on the branch.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../core/models/FoundryBranch.md)
- [foundry_sdk.v2.functions.models.DataValue](DataValue.md)
- [foundry_sdk.v2.functions.models.FunctionVersion](FunctionVersion.md)
- [foundry_sdk.v2.functions.models.ParameterId](ParameterId.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../ontologies/models/OntologyIdentifier.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExecuteAsyncQueryRequest.md)
