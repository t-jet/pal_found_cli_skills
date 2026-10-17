# foundry_sdk.v1.ontologies.models.SelectedPropertyApiName



By default, whenever an object is requested, all of its properties are returned, except for properties of the 
following types:
- Vector

The response can be filtered to only include certain properties using the `properties` query parameter. Note
that ontology object set endpoints refer to this parameter as `select`.

Properties to include can be specified in one of two ways.

- A comma delimited list as the value for the `properties` query parameter
  `properties={property1ApiName},{property2ApiName}`
- Multiple `properties` query parameters.
  `properties={property1ApiName}&properties={property2ApiName}`

The primary key of the object will always be returned even if it wasn't specified in the `properties` values.

Unknown properties specified in the `properties` list will result in a `PropertiesNotFound` error.

To find the API name for your property, use the `Get object type` endpoint or check the **Ontology Manager**.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SelectedPropertyApiName: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SelectedPropertyApiName.md)
