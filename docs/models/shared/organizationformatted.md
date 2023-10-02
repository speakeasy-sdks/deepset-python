# OrganizationFormatted


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `name`                                                           | *Optional[str]*                                                  | :heavy_check_mark:                                               | Unique name of an organization                                   |
| `organization_id`                                                | *Optional[str]*                                                  | :heavy_check_mark:                                               | Unique identifier of an organization                             |
| `pricing_plan`                                                   | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Pricing plan of an organization, between 0 and 3                 |
| `role`                                                           | *Optional[str]*                                                  | :heavy_check_mark:                                               | N/A                                                              |
| `workspaces`                                                     | list[[shared.EntityRole](undefined/models/shared/entityrole.md)] | :heavy_check_mark:                                               | N/A                                                              |