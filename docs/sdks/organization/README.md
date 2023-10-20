# Organization
(*organization*)

### Available Operations

* [get](#get) - Get Organization [private]
* [invite](#invite) - Invite User To Organization [private]

## get

Returns the name of the organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.organization.get()

if res.organization_name is not None:
    # handle response
    pass
```


### Response

**[operations.GetOrganizationAPIV1OrganizationGetResponse](../../models/operations/getorganizationapiv1organizationgetresponse.md)**


## invite

Sends an email to the user inviting them to your deepset Cloud organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.organization.invite(request_body=operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostUserInvitation(
    email='Vivianne9@yahoo.com',
    family_name='wing',
    given_name='respectful',
    role=shared.RolesToDB.ZERO,
), organization_id='International')

if res.invite_user_to_organization_api_v1_organization_organization_id_invitation_post_201_application_json_any is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                        | Type                                                                                                                                                                                                             | Required                                                                                                                                                                                                         | Description                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                                                                                   | [operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostUserInvitation](../../models/operations/inviteusertoorganizationapiv1organizationorganizationidinvitationpostuserinvitation.md) | :heavy_check_mark:                                                                                                                                                                                               | N/A                                                                                                                                                                                                              |
| `organization_id`                                                                                                                                                                                                | *str*                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                               | A unique identifier of the organization. You can obtain it from Get Organization.                                                                                                                                |


### Response

**[operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostResponse](../../models/operations/inviteusertoorganizationapiv1organizationorganizationidinvitationpostresponse.md)**

