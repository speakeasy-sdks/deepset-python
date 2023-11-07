# InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostUserInvitation

The definition of the user that you want to invite to the organization.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `email`                                                  | *str*                                                    | :heavy_check_mark:                                       | Email of a user                                          |
| `family_name`                                            | *str*                                                    | :heavy_check_mark:                                       | Family name of a user                                    |
| `given_name`                                             | *str*                                                    | :heavy_check_mark:                                       | Given name of a user                                     |
| `role`                                                   | [components.RolesToDB](../../models/shared/rolestodb.md) | :heavy_check_mark:                                       | An enumeration.                                          |