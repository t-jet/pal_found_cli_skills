# v2.admin resources and operations


Use Admin resources to read enrollment identity, users, groups, Organizations, role assignments and Markings before changing access. A role or membership change affects the named security boundary; identify the exact principal and resource, then read back assignments rather than assuming effective access from a write response. Read the selected operation contract before invocation; stage, API version and result lifetime remain operation-specific.

| Operation | Stage |
| --- | --- |
| [v2.admin.AuthenticationProvider.get](../../contracts/v2/admin/AuthenticationProvider/get.md) | Public Beta |
| [v2.admin.AuthenticationProvider.list](../../contracts/v2/admin/AuthenticationProvider/list.md) | Public Beta |
| [v2.admin.AuthenticationProvider.preregister_group](../../contracts/v2/admin/AuthenticationProvider/preregister_group.md) | Public Beta |
| [v2.admin.AuthenticationProvider.preregister_user](../../contracts/v2/admin/AuthenticationProvider/preregister_user.md) | Public Beta |
| [v2.admin.CbacBanner.get](../../contracts/v2/admin/CbacBanner/get.md) | Public Beta |
| [v2.admin.CbacMarkingRestrictions.get](../../contracts/v2/admin/CbacMarkingRestrictions/get.md) | Public Beta |
| [v2.admin.Enrollment.get](../../contracts/v2/admin/Enrollment/get.md) | Public Beta |
| [v2.admin.Enrollment.get_current](../../contracts/v2/admin/Enrollment/get_current.md) | Public Beta |
| [v2.admin.EnrollmentRoleAssignment.add](../../contracts/v2/admin/EnrollmentRoleAssignment/add.md) | Public Beta |
| [v2.admin.EnrollmentRoleAssignment.list](../../contracts/v2/admin/EnrollmentRoleAssignment/list.md) | Public Beta |
| [v2.admin.EnrollmentRoleAssignment.remove](../../contracts/v2/admin/EnrollmentRoleAssignment/remove.md) | Public Beta |
| [v2.admin.Group.create](../../contracts/v2/admin/Group/create.md) | Stable |
| [v2.admin.Group.delete](../../contracts/v2/admin/Group/delete.md) | Stable |
| [v2.admin.Group.get](../../contracts/v2/admin/Group/get.md) | Stable |
| [v2.admin.Group.get_batch](../../contracts/v2/admin/Group/get_batch.md) | Stable |
| [v2.admin.Group.list](../../contracts/v2/admin/Group/list.md) | Stable |
| [v2.admin.Group.list_current](../../contracts/v2/admin/Group/list_current.md) | Public Beta |
| [v2.admin.Group.replace](../../contracts/v2/admin/Group/replace.md) | Stable |
| [v2.admin.Group.search](../../contracts/v2/admin/Group/search.md) | Stable |
| [v2.admin.GroupMember.add](../../contracts/v2/admin/GroupMember/add.md) | Stable |
| [v2.admin.GroupMember.list](../../contracts/v2/admin/GroupMember/list.md) | Stable |
| [v2.admin.GroupMember.remove](../../contracts/v2/admin/GroupMember/remove.md) | Stable |
| [v2.admin.GroupMembership.list](../../contracts/v2/admin/GroupMembership/list.md) | Stable |
| [v2.admin.GroupMembershipExpirationPolicy.get](../../contracts/v2/admin/GroupMembershipExpirationPolicy/get.md) | Public Beta |
| [v2.admin.GroupMembershipExpirationPolicy.replace](../../contracts/v2/admin/GroupMembershipExpirationPolicy/replace.md) | Public Beta |
| [v2.admin.GroupProviderInfo.get](../../contracts/v2/admin/GroupProviderInfo/get.md) | Stable |
| [v2.admin.GroupProviderInfo.replace](../../contracts/v2/admin/GroupProviderInfo/replace.md) | Stable |
| [v2.admin.Host.list](../../contracts/v2/admin/Host/list.md) | Public Beta |
| [v2.admin.Marking.create](../../contracts/v2/admin/Marking/create.md) | Stable |
| [v2.admin.Marking.get](../../contracts/v2/admin/Marking/get.md) | Stable |
| [v2.admin.Marking.get_batch](../../contracts/v2/admin/Marking/get_batch.md) | Stable |
| [v2.admin.Marking.list](../../contracts/v2/admin/Marking/list.md) | Stable |
| [v2.admin.Marking.parse_classifications](../../contracts/v2/admin/Marking/parse_classifications.md) | Public Beta |
| [v2.admin.Marking.replace](../../contracts/v2/admin/Marking/replace.md) | Stable |
| [v2.admin.MarkingCategory.create](../../contracts/v2/admin/MarkingCategory/create.md) | Public Beta |
| [v2.admin.MarkingCategory.get](../../contracts/v2/admin/MarkingCategory/get.md) | Stable |
| [v2.admin.MarkingCategory.list](../../contracts/v2/admin/MarkingCategory/list.md) | Stable |
| [v2.admin.MarkingCategory.replace](../../contracts/v2/admin/MarkingCategory/replace.md) | Public Beta |
| [v2.admin.MarkingMember.add](../../contracts/v2/admin/MarkingMember/add.md) | Stable |
| [v2.admin.MarkingMember.list](../../contracts/v2/admin/MarkingMember/list.md) | Stable |
| [v2.admin.MarkingMember.remove](../../contracts/v2/admin/MarkingMember/remove.md) | Stable |
| [v2.admin.MarkingRoleAssignment.add](../../contracts/v2/admin/MarkingRoleAssignment/add.md) | Stable |
| [v2.admin.MarkingRoleAssignment.list](../../contracts/v2/admin/MarkingRoleAssignment/list.md) | Stable |
| [v2.admin.MarkingRoleAssignment.remove](../../contracts/v2/admin/MarkingRoleAssignment/remove.md) | Stable |
| [v2.admin.Organization.create](../../contracts/v2/admin/Organization/create.md) | Public Beta |
| [v2.admin.Organization.get](../../contracts/v2/admin/Organization/get.md) | Stable |
| [v2.admin.Organization.list_available_roles](../../contracts/v2/admin/Organization/list_available_roles.md) | Stable |
| [v2.admin.Organization.replace](../../contracts/v2/admin/Organization/replace.md) | Stable |
| [v2.admin.OrganizationGuestMember.add](../../contracts/v2/admin/OrganizationGuestMember/add.md) | Private Beta |
| [v2.admin.OrganizationGuestMember.list](../../contracts/v2/admin/OrganizationGuestMember/list.md) | Private Beta |
| [v2.admin.OrganizationGuestMember.remove](../../contracts/v2/admin/OrganizationGuestMember/remove.md) | Private Beta |
| [v2.admin.OrganizationRoleAssignment.add](../../contracts/v2/admin/OrganizationRoleAssignment/add.md) | Stable |
| [v2.admin.OrganizationRoleAssignment.list](../../contracts/v2/admin/OrganizationRoleAssignment/list.md) | Stable |
| [v2.admin.OrganizationRoleAssignment.remove](../../contracts/v2/admin/OrganizationRoleAssignment/remove.md) | Stable |
| [v2.admin.Role.get](../../contracts/v2/admin/Role/get.md) | Private Beta |
| [v2.admin.Role.get_batch](../../contracts/v2/admin/Role/get_batch.md) | Private Beta |
| [v2.admin.User.delete](../../contracts/v2/admin/User/delete.md) | Stable |
| [v2.admin.User.get](../../contracts/v2/admin/User/get.md) | Stable |
| [v2.admin.User.get_batch](../../contracts/v2/admin/User/get_batch.md) | Stable |
| [v2.admin.User.get_current](../../contracts/v2/admin/User/get_current.md) | Stable |
| [v2.admin.User.get_markings](../../contracts/v2/admin/User/get_markings.md) | Stable |
| [v2.admin.User.list](../../contracts/v2/admin/User/list.md) | Stable |
| [v2.admin.User.profile_picture](../../contracts/v2/admin/User/profile_picture.md) | Stable |
| [v2.admin.User.revoke_all_tokens](../../contracts/v2/admin/User/revoke_all_tokens.md) | Stable |
| [v2.admin.User.search](../../contracts/v2/admin/User/search.md) | Stable |
| [v2.admin.UserProviderInfo.get](../../contracts/v2/admin/UserProviderInfo/get.md) | Stable |
| [v2.admin.UserProviderInfo.replace](../../contracts/v2/admin/UserProviderInfo/replace.md) | Stable |

[All services](../../catalog.md) | [SDK handling](../../client-behavior.md)

[Part 1](index.md)
