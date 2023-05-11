# user

### Available Operations

* [delete](#delete) - Delete User [private]
* [get](#get) - Get User [private]
* [list](#list) - Get Users [private]
* [me](#me) - Read Users Me [private]
* [update_permission](#update_permission) - Update User Permission [private]

## delete

Deletes a user from deepset Cloud. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteUserAPIV1UsersUserIDDeleteRequest(
    user_id='8d162309-fb09-4299-a1ae-fb9f58c4d86e',
)

res = s.user.delete(req, operations.DeleteUserAPIV1UsersUserIDDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.delete_user_api_v1_users_user_id_delete_200_application_json_any is not None:
    # handle response
```

## get

Retrieves the properties of the user object. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetUserAPIV1UsersUserIDGetRequest(
    user_id='68e4be05-6013-4f59-9a75-7a59ecfef66e',
)

res = s.user.get(req, operations.GetUserAPIV1UsersUserIDGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.user is not None:
    # handle response
```

## list

Retrieves the properties of all the user objects in your organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListUsersAPIV1UsersGetRequest(
    after='f1caa338-3c2b-4eb4-b737-3c8d72f64d1d',
    before='b1f2c431-0661-4e96-b49e-1cf9e06e3a43',
    include_deleted=False,
    limit=483394,
    page_number=24753,
)

res = s.user.list(req, operations.ListUsersAPIV1UsersGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.user_pagination is not None:
    # handle response
```

## me

Retrieves the properties of the user object. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.user.me(operations.ReadUsersMeAPIV1MeGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.user is not None:
    # handle response
```

## update_permission

Updates user permissions. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.UpdateUserPermissionAPIV1UsersUserIDPatchRequest(
    request_body=operations.UpdateUserPermissionAPIV1UsersUserIDPatchUserRole(
        role=shared.RolesToDBEnum.ZERO,
    ),
    user_id='0ae6b6bc-9b8f-4759-aac5-5a9741d31135',
)

res = s.user.update_permission(req, operations.UpdateUserPermissionAPIV1UsersUserIDPatchSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```
