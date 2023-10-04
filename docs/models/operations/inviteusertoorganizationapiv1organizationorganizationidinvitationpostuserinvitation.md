# InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostUserInvitation

The definition of the user that you want to invite to the organization.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `email`                                                            | *Optional[str]*                                                    | :heavy_check_mark:                                                 | Email of a user                                                    |
| `family_name`                                                      | *Optional[str]*                                                    | :heavy_check_mark:                                                 | Family name of a user                                              |
| `given_name`                                                       | *Optional[str]*                                                    | :heavy_check_mark:                                                 | Given name of a user                                               |
| `role`                                                             | [Optional[shared.RolesToDB]](undefined/models/shared/rolestodb.md) | :heavy_check_mark:                                                 | An enumeration.                                                    |