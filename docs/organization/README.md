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
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.organization_name is not None:
    # handle response
```

## invite

Sends an email to the user inviting them to your deepset Cloud organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostRequest(
    request_body=operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostUserInvitation(
        email='Stuart.Kautzer69@gmail.com',
        family_name='occaecati',
        given_name='minima',
        role=shared.RolesToDBEnum.THREE,
    ),
    organization_id='eligendi',
)

res = s.organization.invite(req, operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.invite_user_to_organization_api_v1_organization_organization_id_invitation_post_201_application_json_any is not None:
    # handle response
```
