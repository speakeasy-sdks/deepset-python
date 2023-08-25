# organization

### Available Operations

* [get](#get) - Get Organization [private]
* [invite](#invite) - Invite User To Organization [private]

## get

Returns the name of the organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.organization.get(operations.GetOrganizationAPIV1OrganizationGetSecurity(
    http_bearer="",
))

if res.organization_name is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                       | [operations.GetOrganizationAPIV1OrganizationGetSecurity](../../models/operations/getorganizationapiv1organizationgetsecurity.md) | :heavy_check_mark:                                                                                                               | The security requirements to use for the request.                                                                                |


### Response

**[operations.GetOrganizationAPIV1OrganizationGetResponse](../../models/operations/getorganizationapiv1organizationgetresponse.md)**


## invite

Sends an email to the user inviting them to your deepset Cloud organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.organization.invite(operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostSecurity(
    http_bearer="",
), request_body=operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostUserInvitation(
    email='Kameron39@gmail.com',
    family_name='fugit',
    given_name='sapiente',
    role=shared.RolesToDB.ZERO,
), organization_id='ratione')

if res.invite_user_to_organization_api_v1_organization_organization_id_invitation_post_201_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                        | Type                                                                                                                                                                                                             | Required                                                                                                                                                                                                         | Description                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                       | [operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostSecurity](../../models/operations/inviteusertoorganizationapiv1organizationorganizationidinvitationpostsecurity.md)             | :heavy_check_mark:                                                                                                                                                                                               | The security requirements to use for the request.                                                                                                                                                                |
| `request_body`                                                                                                                                                                                                   | [operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostUserInvitation](../../models/operations/inviteusertoorganizationapiv1organizationorganizationidinvitationpostuserinvitation.md) | :heavy_check_mark:                                                                                                                                                                                               | N/A                                                                                                                                                                                                              |
| `organization_id`                                                                                                                                                                                                | *str*                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                               | A unique identifier of the organization. You can obtain it from Get Organization.                                                                                                                                |


### Response

**[operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostResponse](../../models/operations/inviteusertoorganizationapiv1organizationorganizationidinvitationpostresponse.md)**

