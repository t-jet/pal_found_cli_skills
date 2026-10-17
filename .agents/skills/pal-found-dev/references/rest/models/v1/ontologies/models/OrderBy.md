# foundry_sdk.v1.ontologies.models.OrderBy



A command representing the list of properties to order by. Properties should be delimited by commas and
prefixed by `p` or `properties`. The format expected format is
`orderBy=properties.{property}:{sortDirection},properties.{property}:{sortDirection}...`

By default, the ordering for a property is ascending, and this can be explicitly specified by appending 
`:asc` (for ascending) or `:desc` (for descending).

Example: use `orderBy=properties.lastName:asc` to order by a single property, 
`orderBy=properties.lastName,properties.firstName,properties.age:desc` to order by multiple properties. 
You may also use the shorthand `p` instead of `properties` such as `orderBy=p.lastName:asc`.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
OrderBy: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OrderBy.md)
