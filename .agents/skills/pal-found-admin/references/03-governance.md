# Governance: classifications, markings, and categories

Foundry uses markings, classification-based controls, and organizations as mandatory access requirements. They apply alongside project roles and can propagate with derived data. A marking category groups markings and controls discoverability. See [security overview](https://www.palantir.com/docs/foundry/security/overview), [CBAC](https://www.palantir.com/docs/foundry/security/classification-based-access-controls), and [marking management](https://www.palantir.com/docs/foundry/platform-security-management/manage-markings). Examples follow SDK `docs/v2/Admin` and the Admin CLI parser. Replace sample identifiers before running.

## Operation records

### cbac_banner.get

Compute the classification banner to display for a set of markings. Supply marking IDs with `--marking-ids`; `--display-type PORTION_MARKING` is the short form for a paragraph, while `BANNER_LINE` is the longer document-header form. The response contains banner text and colors; it does not grant access.

Required input: no required operation arguments. Optional: `--display-type`, `--marking-ids`. The SDK returns `CbacBanner` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin cbac-banner get`

### cbac_marking_restrictions.get

Inspect how classification markings interact before applying them to data. Supply marking IDs through `--marking-ids`; the response identifies disallowed combinations and markings that are implied or required. This is a read of classification rules, not an operation that adds markings.

Required input: no required operation arguments. Optional: `--marking-ids`. The SDK returns `CbacMarkingRestrictions` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin cbac-marking-restrictions get`

### host.list

List host addresses associated with the enrollment, useful when checking which Foundry host belongs to that administrative boundary. Results are paged, and page length may differ from `--page-size`; follow `nextPageToken` until absent.

Required input: `enrollment_rid`. The SDK returns `ListHostsResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin host list ri.multipass..enrollment.example`

### marking.create

Create a marking in the category named by `--category-id`. `--name` is the displayed marking label; optional `--description` explains what data it protects. A resource carrying the marking requires a reader to satisfy the marking's access condition as well as its other access controls. `--initial-members` names principals that can satisfy it; `--initial-role-assignments` names its administrators. The response includes the new marking ID for later membership changes.

Required input: `--category-id`, `--initial-members`, `--initial-role-assignments`, `--name`. Optional: `--description`. The SDK returns `Marking` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result. At least one initial `ADMINISTER` role is required. Include your own principal or an administering group you belong to, or you can create a marking you cannot manage. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin marking create --category-id 0950264e-01c8-4e83-81a9-1a6b7f77621a --initial-members '["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]' --initial-role-assignments '[{"role":"ADMINISTER","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]' --name PII`

### marking.get

Read a marking by ID to check its name, description, and category before changing membership or attaching it to a resource. Use `marking-member list` and `marking-role-assignment list` to inspect its access principals.

Required input: `marking_id`. The SDK returns `Marking` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin marking get 0950264e-01c8-4e83-81a9-1a6b7f77621a`

### marking.get_batch

Resolve up to 500 marking IDs from a resource's security metadata in one request. The positional `body` is a JSON array of `markingId` requests. Compare returned IDs to requested IDs, since a batch result should not be assumed complete.

Required input: `body`. The SDK returns `GetMarkingsBatchResponse` on success. The operation does not change Foundry state. Compare returned IDs with requested IDs; some endpoints omit unknown or inaccessible records. The endpoint accepts at most 500 marking IDs. An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin marking get-batch '[{"markingId":"18212f9a-0e63-4b79-96a0-aae04df23336"}]'`

### marking.list

List markings visible to this administrator to discover IDs and categories for later inspection. The maximum page size is 100; follow the returned `nextPageToken` even if a page contains fewer than 100 entries.

Required input: no required operation arguments. The SDK returns `ListMarkingsResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned. The maximum page size is 100. Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin marking list`

### marking.replace

Change a marking's displayed label with `--name` and its optional explanatory text with `--description`. This command does not alter its category, members, or role assignments. Read the marking first so the new metadata describes the right access requirement, and use the dedicated membership or role commands for access changes.

Required input: `marking_id`, `--name`. Optional: `--description`. The SDK returns `Marking` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin marking replace 0950264e-01c8-4e83-81a9-1a6b7f77621a --name PII`

### marking_category.create

A category groups related markings and controls who can discover or administer them. `--name` is the category label and `--description` explains its purpose. `--initial-permissions` specifies organization visibility, public visibility, and administrator role assignments. Include at least one `ADMINISTER` assignment for yourself or a group you belong to, or you may be unable to manage the created category.

Required input: `--description`, `--initial-permissions`, `--name`. The SDK returns `MarkingCategory` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin marking-category create --description 'Markings related to data about our customers' --initial-permissions '{"organizationRids":["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"],"roles":[{"role":"ADMINISTER","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"}],"isPublic":false}' --name 'Customer Data'`

### marking_category.get

Read a category by ID to inspect its name, description, and visibility before adding a marking to it. A category is an organizing and permission boundary; the individual marking still has its own members and roles.

Required input: `marking_category_id`. The SDK returns `MarkingCategory` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin marking-category get 0950264e-01c8-4e83-81a9-1a6b7f77621a`

### marking_category.list

List visible marking categories so an administrator can choose the category ID for a new marking. The maximum page size is 100; follow a returned continuation token to see later categories.

Required input: no required operation arguments. The SDK returns `ListMarkingCategoriesResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned. The maximum page size is 100. Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin marking-category list`

### marking_category.replace

Change a category's displayed label with `--name` and its explanation with `--description`, while keeping its ID. This call does not edit its permissions. Read the category afterward to verify the metadata.

Required input: `marking_category_id`, `--description`, `--name`. The SDK returns `MarkingCategory` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin marking-category replace 0950264e-01c8-4e83-81a9-1a6b7f77621a --description 'Markings related to data about our customers' --name 'Customer Data'`
