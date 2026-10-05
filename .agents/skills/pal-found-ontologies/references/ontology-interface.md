# Ontology interface operations

These records describe the `ontology_interface` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### ontology_interface.aggregate

- **Purpose and behavior:** :::callout{theme=warning title=Warning} This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object sets. ::: Perform functions on object fields in the specified ontology and of the specified interface type. Any properties specified in the query must be shared property type API names defined on the interface.
- **CLI inputs:** positionals `ontology`, `interface_type`; optional `--aggregation`, `--group-by`, `--accuracy`, `--branch`, `--preview`, `--where`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `interface_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to aggregate objects from. If omitted, uses the default branch. `--where`: JSON query that filters matching objects, such as `{"type":"eq","field":"status","value":"active"}`. `--accuracy` sets the requested aggregate accuracy mode; `--aggregation` defines the aggregate calculation over the selected objects; `--group-by` groups aggregate results by the specified properties; `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The interface exists in the ontology and the caller can read its metadata or implementing objects.
- **Result:** Returns `AggregateObjectsResponseV2` with the computed aggregate for the selected scope.
- **Failure:** Unknown interface or invalid filter fails; an empty successful result can mean no implementing objects matched.
- **Example:** `pal-found-ontologies ontology-interface aggregate palantir Employee --aggregation '[{"type":"min","field":"tenure","name":"min_tenure"},{"type":"avg","field":"tenure","name":"avg_tenure"}]' --group-by '[{"field":"startDate","type":"range","ranges":[{"startValue":"2020-01-01","endValue":"2020-06-01"}]},{"field":"city","type":"exact"}]' --where '{"type":"eq","field":"name","value":"john"}'`

### ontology_interface.get

- **Purpose and behavior:** Gets a specific interface type with the given API name.
- **CLI inputs:** positionals `ontology`, `interface_type`; optional `--branch`, `--preview`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `interface_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to load the interface type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--preview` enables endpoint preview behavior when that feature is available; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The interface exists in the ontology and the caller can read its metadata or implementing objects.
- **Result:** Returns `InterfaceType` for the selected ontology interface.
- **Failure:** Unknown interface or invalid filter fails; an empty successful result can mean no implementing objects matched.
- **Example:** `pal-found-ontologies ontology-interface get palantir Employee`

### ontology_interface.get_outgoing_interface_link_type

- **Purpose and behavior:** Get an outgoing interface link type for an interface type.
- **CLI inputs:** positionals `ontology`, `interface_type`, `interface_link_type`; optional `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `interface_type`: API name defined in the ontology; discover it through the corresponding metadata command. `interface_link_type`: The API name of the outgoing interface link. To find the API name for your interface link type, check the **Ontology Manager** page for the parent interface. `--branch`: The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The interface exists in the ontology and the caller can read its metadata or implementing objects.
- **Result:** Returns `InterfaceLinkType` for the selected ontology interface.
- **Failure:** Unknown interface or invalid filter fails; an empty successful result can mean no implementing objects matched.
- **Example:** `pal-found-ontologies ontology-interface get-outgoing-interface-link-type palantir Employee worksAt`

### ontology_interface.list

- **Purpose and behavior:** Lists the interface types for the given Ontology. Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.
- **CLI inputs:** positionals `ontology`; optional `--page-size`, `--page-token`, `--branch`, `--preview`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--branch`: The Foundry branch to list the interface types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page; `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The interface exists in the ontology and the caller can read its metadata or implementing objects.
- **Result:** Returns `ListInterfaceTypesResponse` containing the visible matching ontology interface entries; an empty page means none matched that page.
- **Failure:** Unknown interface or invalid filter fails; an empty successful result can mean no implementing objects matched.
- **Example:** `pal-found-ontologies ontology-interface list palantir`

### ontology_interface.list_interface_linked_objects

- **Purpose and behavior:** Lists the linked objects for a specific object and the given interface link type. Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or repeated objects in the response pages. For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response. Note that null value properties will not be returned.
- **CLI inputs:** positionals `ontology`, `interface_type`, `object_type`, `primary_key`, `interface_link_type`; optional `--page-size`, `--page-token`, `--branch`, `--exclude-rid`, `--order-by`, `--preview`, `--select`, `--snapshot`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `interface_type`: API name defined in the ontology; discover it through the corresponding metadata command. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `--branch` selects a Foundry branch; omit it for the default branch; `--exclude-rid` omits the object's `__rid` property when true; `--order-by` defines the result sort order using the endpoint's order-by schema; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page; `--preview` enables endpoint preview behavior when that feature is available; `--select` lists property API names to include in returned objects; `--snapshot` uses a stable result snapshot across pages when true; live paging may see duplicates or omissions; `interface_link_type` is the API name of the interface link type to traverse.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The interface exists in the ontology and the caller can read its metadata or implementing objects.
- **Result:** Returns `ListInterfaceLinkedObjectsResponse` containing the visible matching ontology interface entries; an empty page means none matched that page.
- **Failure:** Unknown interface or invalid filter fails; an empty successful result can mean no implementing objects matched.
- **Example:** `pal-found-ontologies ontology-interface list-interface-linked-objects palantir Employee employee <PRIMARY_KEY> worksAt`

### ontology_interface.list_objects_for_interface

- **Purpose and behavior:** Lists the objects for the given Ontology and interface type. Note that this endpoint does not guarantee consistency, unless you use the snapshot flag specified below. Changes to the data could result in missing or repeated objects in the response pages. For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response. Note that null value properties will not be returned.
- **CLI inputs:** positionals `ontology`, `interface_type`; optional `--page-size`, `--page-token`, `--branch`, `--exclude-rid`, `--order-by`, `--preview`, `--select`, `--snapshot`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `interface_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to list objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--select`: JSON array of selected property API names or property identifiers, respectively. `--exclude-rid` omits the object's `__rid` property when true; `--order-by` defines the result sort order using the endpoint's order-by schema; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page; `--preview` enables endpoint preview behavior when that feature is available; `--snapshot` uses a stable result snapshot across pages when true; live paging may see duplicates or omissions.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The interface exists in the ontology and the caller can read its metadata or implementing objects.
- **Result:** Returns `ListObjectsForInterfaceResponse` containing the visible matching ontology interface entries; an empty page means none matched that page.
- **Failure:** Unknown interface or invalid filter fails; an empty successful result can mean no implementing objects matched.
- **Example:** `pal-found-ontologies ontology-interface list-objects-for-interface palantir employee`

### ontology_interface.list_outgoing_interface_link_types

- **Purpose and behavior:** List the outgoing interface link types for an interface type.
- **CLI inputs:** positionals `ontology`, `interface_type`; optional `--branch`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `interface_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to get the outgoing link type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The interface exists in the ontology and the caller can read its metadata or implementing objects.
- **Result:** Returns `ListOutgoingInterfaceLinkTypesResponse` containing the visible matching ontology interface entries; an empty page means none matched that page.
- **Failure:** Unknown interface or invalid filter fails; an empty successful result can mean no implementing objects matched.
- **Example:** `pal-found-ontologies ontology-interface list-outgoing-interface-link-types palantir Employee`

### ontology_interface.search

- **Purpose and behavior:** :::callout{theme=warning title=Warning} This endpoint will be removed once TS OSDK is updated to use `objectSets/loadObjects` with interface object sets. ::: Search for objects in the specified ontology and interface type. Any properties specified in the "where" or "orderBy" parameters must be shared property type API names defined on the interface. The following search queries are supported: | Query type | Description | Supported Types | |-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------| | lt | The provided property is less than the provided value. | number, string, date, timestamp | | gt | The provided property is greater than the provided value. | number, string, date, timestamp | | lte | The provided property is less than or equal to the provided value.
- **CLI inputs:** positionals `ontology`, `interface_type`; optional `--page-size`, `--page-token`, `--augmented-interface-property-types`, `--augmented-properties`, `--augmented-shared-property-types`, `--other-interface-types`, `--selected-interface-property-types`, `--selected-object-types`, `--selected-shared-property-types`, `--branch`, `--order-by`, `--preview`, `--where`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `interface_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to search objects from. If omitted, uses the default branch. `--where`: JSON query that filters matching objects, such as `{"type":"eq","field":"status","value":"active"}`. `--augmented-interface-property-types` adds interface property type metadata to search results; `--augmented-properties` adds object property values to interface search results; `--augmented-shared-property-types` adds shared property type metadata to search results; `--order-by` defines the result sort order using the endpoint's order-by schema; `--other-interface-types` requires returned object types to implement every listed additional interface; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page; `--preview` enables endpoint preview behavior when that feature is available; `--selected-interface-property-types` selects interface property types to return from the search; `--selected-object-types` restricts search results to these object types implementing the interface; `--selected-shared-property-types` selects shared property types to return from the search.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The interface exists in the ontology and the caller can read its metadata or implementing objects.
- **Result:** Returns `SearchObjectsResponseV2` containing the visible matching ontology interface entries; an empty page means none matched that page.
- **Failure:** Unknown interface or invalid filter fails; an empty successful result can mean no implementing objects matched.
- **Example:** `pal-found-ontologies ontology-interface search palantir Employee --augmented-interface-property-types '[]' --augmented-properties '[]' --augmented-shared-property-types '[]' --other-interface-types '[]' --selected-interface-property-types '[]' --selected-object-types '[]' --selected-shared-property-types '[]'`
