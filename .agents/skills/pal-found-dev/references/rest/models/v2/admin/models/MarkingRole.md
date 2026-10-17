# foundry_sdk.v2.admin.models.MarkingRole



Represents the operations that a user can perform with regards to a Marking.
  * ADMINISTER: The user can add and remove members from the Marking, update Marking Role Assignments, and change Marking metadata.
  * DECLASSIFY: The user can remove the Marking from resources in the platform and stop the propagation of the Marking during a transform.
  * USE: The user can apply the marking to resources in the platform.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
MarkingRole: typing_extensions.TypeAlias = typing.Literal["ADMINISTER", "DECLASSIFY", "USE"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MarkingRole.md)
