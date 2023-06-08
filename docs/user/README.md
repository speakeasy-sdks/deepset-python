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
    user_id='18d16230-9fb0-4929-921a-efb9f58c4d86',
)

res = s.user.delete(req, operations.DeleteUserAPIV1UsersUserIDDeleteSecurity(
    http_bearer="",
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
    user_id='e68e4be0-5601-43f5-9da7-57a59ecfef66',
)

res = s.user.get(req, operations.GetUserAPIV1UsersUserIDGetSecurity(
    http_bearer="",
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
    after='ef1caa33-83c2-4beb-8773-73c8d72f64d1',
    before='db1f2c43-1066-41e9-a349-e1cf9e06e3a4',
    include_deleted=False,
    limit=224467,
    page_number=483394,
)

res = s.user.list(req, operations.ListUsersAPIV1UsersGetSecurity(
    http_bearer="",
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
    http_bearer="",
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
        role=shared.RolesToDB.ZERO,
    ),
    user_id='00ae6b6b-c9b8-4f75-9eac-55a9741d3113',
)

res = s.user.update_permission(req, operations.UpdateUserPermissionAPIV1UsersUserIDPatchSecurity(
    http_bearer="",
))

if res.status_code == 200:
    # handle response
```
