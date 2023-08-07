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


res = s.user.delete(operations.DeleteUserAPIV1UsersUserIDDeleteSecurity(
    http_bearer="",
), user_id='451c6c6e-205e-416d-aab3-fec9578a6458')

if res.delete_user_api_v1_users_user_id_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                 | [operations.DeleteUserAPIV1UsersUserIDDeleteSecurity](../../models/operations/deleteuserapiv1usersuseriddeletesecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |
| `user_id`                                                                                                                  | *str*                                                                                                                      | :heavy_check_mark:                                                                                                         | A unique identifier of the user. You can obtain it by running the Get Users endpoint.                                      |


### Response

**[operations.DeleteUserAPIV1UsersUserIDDeleteResponse](../../models/operations/deleteuserapiv1usersuseriddeleteresponse.md)**


## get

Retrieves the properties of the user object. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.user.get(operations.GetUserAPIV1UsersUserIDGetSecurity(
    http_bearer="",
), user_id='4273a841-8d16-4230-9fb0-929921aefb9f')

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                     | [operations.GetUserAPIV1UsersUserIDGetSecurity](../../models/operations/getuserapiv1usersuseridgetsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |
| `user_id`                                                                                                      | *str*                                                                                                          | :heavy_check_mark:                                                                                             | A unique identifier of the user. You can obtain it by running the Get Users endpoint.                          |


### Response

**[operations.GetUserAPIV1UsersUserIDGetResponse](../../models/operations/getuserapiv1usersuseridgetresponse.md)**


## list

Retrieves the properties of all the user objects in your organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListUsersAPIV1UsersGetRequest(
    after='58c4d86e-68e4-4be0-9601-3f59da757a59',
    before='ecfef66e-f1ca-4a33-83c2-beb477373c8d',
    include_deleted=False,
    limit=437814,
    page_number=139072,
)

res = s.user.list(req, operations.ListUsersAPIV1UsersGetSecurity(
    http_bearer="",
))

if res.user_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListUsersAPIV1UsersGetRequest](../../models/operations/listusersapiv1usersgetrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.ListUsersAPIV1UsersGetSecurity](../../models/operations/listusersapiv1usersgetsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.ListUsersAPIV1UsersGetResponse](../../models/operations/listusersapiv1usersgetresponse.md)**


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

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `security`                                                                                           | [operations.ReadUsersMeAPIV1MeGetSecurity](../../models/operations/readusersmeapiv1megetsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.ReadUsersMeAPIV1MeGetResponse](../../models/operations/readusersmeapiv1megetresponse.md)**


## update_permission

Updates user permissions. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.user.update_permission(operations.UpdateUserPermissionAPIV1UsersUserIDPatchSecurity(
    http_bearer="",
), request_body=operations.UpdateUserPermissionAPIV1UsersUserIDPatchUserRole(
    role=shared.RolesToDB.FOUR,
), user_id='64d1db1f-2c43-4106-a1e9-6349e1cf9e06')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                   | [operations.UpdateUserPermissionAPIV1UsersUserIDPatchSecurity](../../models/operations/updateuserpermissionapiv1usersuseridpatchsecurity.md) | :heavy_check_mark:                                                                                                                           | The security requirements to use for the request.                                                                                            |
| `request_body`                                                                                                                               | [operations.UpdateUserPermissionAPIV1UsersUserIDPatchUserRole](../../models/operations/updateuserpermissionapiv1usersuseridpatchuserrole.md) | :heavy_check_mark:                                                                                                                           | N/A                                                                                                                                          |
| `user_id`                                                                                                                                    | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | A unique identifier of the user. You can obtain it by running the Get Users endpoint.                                                        |


### Response

**[operations.UpdateUserPermissionAPIV1UsersUserIDPatchResponse](../../models/operations/updateuserpermissionapiv1usersuseridpatchresponse.md)**

