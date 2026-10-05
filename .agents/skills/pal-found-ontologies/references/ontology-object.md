# Ontology object operations

These records describe the `ontology_object` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### ontology_object.aggregate

- **Purpose and behavior:** Perform functions on object fields in the specified ontology and object type.
- **CLI inputs:** positionals `ontology`, `object_type`; optional `--aggregation`, `--group-by`, `--accuracy`, `--branch`, `--sdk-package-rid`, `--sdk-version`, `--where`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to aggregate objects from. If omitted, uses the default branch. `--where`: JSON query that filters matching objects, such as `{"type":"eq","field":"status","value":"active"}`. `--accuracy` sets the requested aggregate accuracy mode; `--aggregation` defines the aggregate calculation over the selected objects; `--group-by` groups aggregate results by the specified properties; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object type is defined in the ontology and the caller can read its objects.
- **Result:** Returns `AggregateObjectsResponseV2` with the computed aggregate for the selected scope.
- **Failure:** An unknown object type, invalid aggregation or filter, or missing read permission returns a structured error.
- **Example:** `pal-found-ontologies ontology-object aggregate palantir employee --aggregation '[{"type":"min","field":"tenure","name":"min_tenure"},{"type":"avg","field":"tenure","name":"avg_tenure"}]' --group-by '[{"field":"startDate","type":"range","ranges":[{"startValue":"2020-01-01","endValue":"2020-06-01"}]},{"field":"city","type":"exact"}]' --where '{"type":"eq","field":"name","value":"john"}'`

### ontology_object.count

- **Purpose and behavior:** Returns a count of the objects of the given object type.
- **CLI inputs:** positionals `ontology`, `object_type`; optional `--branch`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to count the objects from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object type is defined in the ontology and the caller can read its objects.
- **Result:** Returns `CountObjectsResponseV2` with the computed count for the selected scope.
- **Failure:** An unknown object type or missing read permission returns a structured error; a successful zero count means no objects matched.
- **Example:** `pal-found-ontologies ontology-object count palantir employee`

### ontology_object.get

- **Purpose and behavior:** Gets a specific object with the given primary key.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`; optional `--branch`, `--exclude-rid`, `--sdk-package-rid`, `--sdk-version`, `--select`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `--branch`: The Foundry branch to get the object from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. `--exclude-rid` omits the object's `__rid` property when true; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `--select` lists property API names to include in returned objects.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object type is defined in the ontology and the caller can read its objects; `get` also needs an existing primary key.
- **Result:** Returns `OntologyObjectV2` for the selected ontology object.
- **Failure:** Unknown object type or primary key and invalid search/filter JSON produce structured errors; an empty successful search means no match.
- **Example:** `pal-found-ontologies ontology-object get palantir employee 50030`

### ontology_object.list

- **Purpose and behavior:** Lists the objects for the given Ontology and object type. Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or repeated objects in the response pages. For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response. Note that null value properties will not be returned.
- **CLI inputs:** positionals `ontology`, `object_type`; optional `--page-size`, `--page-token`, `--branch`, `--exclude-rid`, `--order-by`, `--sdk-package-rid`, `--sdk-version`, `--select`, `--snapshot`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch`: The Foundry branch to list objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--select`: JSON array of selected property API names or property identifiers, respectively. `--exclude-rid` omits the object's `__rid` property when true; `--order-by` defines the result sort order using the endpoint's order-by schema; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `--snapshot` uses a stable result snapshot across pages when true; live paging may see duplicates or omissions.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object type is defined in the ontology and the caller can read its objects.
- **Result:** Returns `ListObjectsResponseV2` containing the visible matching ontology object entries; an empty page means none matched that page.
- **Failure:** An unknown object type or missing read permission returns a structured error. A successful empty page means no objects were returned on that page.
- **Example:** `pal-found-ontologies ontology-object list palantir employee`

### ontology_object.search

- **Purpose and behavior:** Searches objects of one ontology type using a JSON filter. Comparison operators include `eq`, `lt`, `lte`, `gt`, and `gte`; the filter can combine conditions where supported by the SDK query type. Search returns matching objects and can project selected properties. Check the `SearchJsonQueryV2` schema for the full query grammar.
- **CLI inputs:** positionals `ontology`, `object_type`; optional `--page-size`, `--page-token`, `--select`, `--branch`, `--exclude-rid`, `--order-by`, `--sdk-package-rid`, `--sdk-version`, `--select-v2`, `--snapshot`, `--where`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--select`: JSON array of selected property API names or property identifiers, respectively. `--branch`: The Foundry branch to search objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. `--exclude-rid` omits the object's `__rid` property when true; `--order-by` defines the result sort order using the endpoint's order-by schema; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `--select-v2` selects returned properties using the endpoint's v2 property identifiers; `--snapshot` uses a stable result snapshot across pages when true; live paging may see duplicates or omissions; `--where` filters objects using the SDK search-query JSON schema.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object type is defined in the ontology and the caller can read its objects.
- **Result:** Returns `SearchObjectsResponseV2` containing the visible matching ontology object entries; an empty page means none matched that page.
- **Failure:** An unknown object type, invalid query, or missing read permission returns a structured error. A successful empty result means no objects matched.
- **Example:** `pal-found-ontologies ontology-object search palantir employee --select '["name"]' --where '{"type":"eq","field":"age","value":21}'`
