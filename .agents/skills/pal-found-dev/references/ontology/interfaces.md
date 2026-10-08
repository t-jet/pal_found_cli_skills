# Interfaces and implementations

[Development guide](../../SKILL.md) | [Object mapping](modeling.md)

## Concept and lifecycle

An interface defines properties and constraints shared by concrete object
types. A concrete type implements it by mapping local properties and required
link/action constraints. Consumers can use that common contract where the
platform feature supports interfaces. An interface is not a backing datasource
or a guarantee that every application supports every interface operation.

## Prerequisites

Identify the selected Ontology, consumer capability, concrete types, interface
property types/optionality and link/action requirements. Prepare exact generated
bindings for code consumers. Configuration needs authorized Ontology access;
supported feature availability must be checked in the actual enrollment. Local
fixtures validate your synthetic mapping contract without claiming publication.

## Procedure

1. Verify the Ontology in Ontology Manager. Select New > Interface, or the
   Interfaces resource page's New interface option.
2. Define metadata and properties. Declare required properties and optional
   properties deliberately; optionality changes what a consumer must handle.
   Add the intended link/action constraints when the contract needs them.
3. Implement the interface on each concrete object type. Map every required
   interface property to a compatible existing object property; optional mappings
   may be omitted. Map required link constraints to satisfying link types.
4. Map required Action constraints to compatible Action types and configure
   their parameter mappings through the implementing type's Interfaces tab.
5. Save and validate each implementation and consumer. Changing interface
   property types also requires updating implementing types. If consumers cannot
   migrate together, prepare a separate or extended interface version and migrate
   deliberately rather than breaking existing callers.

## Worked example

Synthetic `NamedEntity` interface has required `name:string` and optional
`region:string`. `Customer.customerName` and `Supplier.supplierName` both map to
`name`. Customer has no region mapping; Supplier maps `supplierRegion`.

The consumer displays Customer `c1/Ada/(region unavailable)` and Supplier
`s1/Acme/West` using the same interface contract. It checks the optional region
before use. Mapping an integer `supplierNumber` to required `name:string` is
incompatible. Leaving required `name` unmapped also rejects the implementation
design; optional region alone does not satisfy it.

The [local fixture](../../examples/ontology/model_fixture.py) exercises accepted
and rejected mappings with declared types and values. Its interface objects
are business design fixtures, not serialized Foundry resource definitions.
Actual enrollment implementations and generated consumer types must match.

## Expected result and checks

Every implementation supplies the required common properties and constraints.
Consumers handle optional values and return the expected concrete objects.
Check both a type with every optional mapping and one without it, plus an
incompatible/absent required mapping. Then verify actual query/Action behavior
and permissions in the selected supported consumer, using the saved interface.

## Failures and recovery

For incompatible mappings, correct the concrete property type or choose a
compatible property. For missing required constraints, configure the matching
link/Action and parameter mapping before accepting the implementation. If an
interface edit breaks consumers, restore the compatible contract or finish the
planned version migration. Missing feature support is an explicit prerequisite
failure; concrete-type success alone does not prove interface compatibility.

Optional provenance: [creation](https://www.palantir.com/docs/foundry/interfaces/create-interface),
[implementation](https://www.palantir.com/docs/foundry/interfaces/implement-interface),
[definition changes](https://www.palantir.com/docs/foundry/interfaces/edit-interface-definition),
[overview and supported consumers](https://www.palantir.com/docs/foundry/interfaces/interface-overview).
