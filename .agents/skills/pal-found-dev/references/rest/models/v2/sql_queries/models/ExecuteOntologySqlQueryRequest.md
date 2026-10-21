# foundry_sdk.v2.sql_queries.models.ExecuteOntologySqlQueryRequest


ExecuteOntologySqlQueryRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| query | query | str | required; no default | The SQL query to execute. |
| parameters | parameters | typing.Optional[Parameters] | None | Parameters for the SQL query. Can be either unnamed positional parameters<br>    or a named parameter mapping. |
| row_limit | rowLimit | typing.Optional[int] | default None | Maximum number of rows to return. |
| dry_run | dryRun | typing.Optional[bool] | default None | If true, parse and validate the query without executing it. Defaults to false. |
| branch | branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to execute the query against. If not specified, the default (main) branch is used. |
| scenario_rid | scenarioRid | typing.Optional[ScenarioRid] | default None | The scenario to evaluate the query against. If not specified, no scenario is applied. |
| ontology_identifier | ontologyIdentifier | typing.Optional[ontologies_models.OntologyIdentifier] | default None | Either an ontology RID or an ontology API name. |
| table_providers | tableProviders | typing.Optional[typing.Dict[TableName, ontologies_models.ObjectSet]] | default None | Map of table providers, requires ontologyIdentifier to be provided otherwise it will throw. |

```python
class ExecuteOntologySqlQueryRequest(core.ModelBase):
    """ExecuteOntologySqlQueryRequest"""

    query: str
    """The SQL query to execute."""

    parameters: typing.Optional[Parameters] = None
    """
    Parameters for the SQL query. Can be either unnamed positional parameters
    or a named parameter mapping.
    """

    row_limit: typing.Optional[int] = pydantic.Field(alias=str("rowLimit"), default=None)  # type: ignore[literal-required]
    """Maximum number of rows to return."""

    dry_run: typing.Optional[bool] = pydantic.Field(alias=str("dryRun"), default=None)  # type: ignore[literal-required]
    """If true, parse and validate the query without executing it. Defaults to false."""

    branch: typing.Optional[core_models.FoundryBranch] = None
    """The Foundry branch to execute the query against. If not specified, the default (main) branch is used."""

    scenario_rid: typing.Optional[ScenarioRid] = pydantic.Field(alias=str("scenarioRid"), default=None)  # type: ignore[literal-required]
    """The scenario to evaluate the query against. If not specified, no scenario is applied."""

    ontology_identifier: typing.Optional[ontologies_models.OntologyIdentifier] = pydantic.Field(alias=str("ontologyIdentifier"), default=None)  # type: ignore[literal-required]
    """Either an ontology RID or an ontology API name."""

    table_providers: typing.Optional[typing.Dict[TableName, ontologies_models.ObjectSet]] = pydantic.Field(alias=str("tableProviders"), default=None)  # type: ignore[literal-required]
    """Map of table providers, requires ontologyIdentifier to be provided otherwise it will throw."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../core/models/FoundryBranch.md)
- [foundry_sdk.v2.ontologies.models.ObjectSet](../../ontologies/models/ObjectSet.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.sql_queries.models.Parameters](Parameters.md)
- [foundry_sdk.v2.sql_queries.models.ScenarioRid](ScenarioRid.md)
- [foundry_sdk.v2.sql_queries.models.TableName](TableName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExecuteOntologySqlQueryRequest.md)
