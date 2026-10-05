# Linked object operations

These records describe the `linked_object` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### linked_object.get_linked_object

- **Purpose and behavior:** Get a specific linked object that originates from another object. If there is no link between the two objects, `LinkedObjectNotFound` is thrown.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `link_type`, `linked_object_primary_key`; optional `--branch`, `--exclude-rid`, `--sdk-package-rid`, `--sdk-version`, `--select`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `link_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch` selects a Foundry branch; omit it for the default branch; `--exclude-rid` omits the object's `__rid` property when true; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `--select` lists property API names to include in returned objects; `linked_object_primary_key` is the primary-key value of the linked object to retrieve.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The source object exists, the link type is defined on its object type, and the caller can read the linked target.
- **Result:** Returns `OntologyObjectV2` for the selected linked object.
- **Failure:** An unknown source key, undefined link type, or denied target object produces a structured error or an empty successful result, according to the query outcome.
- **Example:** `pal-found-ontologies linked-object get-linked-object palantir employee 50030 directReport 80060`

### linked_object.list_linked_objects

- **Purpose and behavior:** Lists the linked objects for a specific object and the given link type. Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or repeated objects in the response pages. For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response. Note that null value properties will not be returned.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `link_type`; optional `--page-size`, `--page-token`, `--branch`, `--exclude-rid`, `--order-by`, `--sdk-package-rid`, `--sdk-version`, `--select`, `--snapshot`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `link_type`: API name defined in the ontology; discover it through the corresponding metadata command. `--branch` selects a Foundry branch; omit it for the default branch; `--exclude-rid` omits the object's `__rid` property when true; `--order-by` defines the result sort order using the endpoint's order-by schema; `--page-size` sets the requested maximum entries in one result page; `--page-token` continues from the previous response's `nextPageToken`; omit on the first page; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `--select` lists property API names to include in returned objects; `--snapshot` uses a stable result snapshot across pages when true; live paging may see duplicates or omissions.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The source object exists, the link type is defined on its object type, and the caller can read the linked target.
- **Result:** Returns `ListLinkedObjectsResponseV2` containing the visible matching linked object entries; an empty page means none matched that page.
- **Failure:** An unknown source key, undefined link type, or denied target object produces a structured error or an empty successful result, according to the query outcome.
- **Example:** `pal-found-ontologies linked-object list-linked-objects palantir employee 50030 directReport`
