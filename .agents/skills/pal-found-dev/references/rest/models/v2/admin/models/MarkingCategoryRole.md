# foundry_sdk.v2.admin.models.MarkingCategoryRole



Represents the operations that a user can perform with regards to a Marking Category.
  * ADMINISTER: The user can update a Marking Category's metadata and permissions
  * VIEW: The user can view the Marking Category and the Markings within it.

NOTE: Permissions to administer or view a Marking Category do not confer any permissions to administer or view data protected by the Markings within that category.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
MarkingCategoryRole: typing_extensions.TypeAlias = typing.Literal["ADMINISTER", "VIEW"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MarkingCategoryRole.md)
