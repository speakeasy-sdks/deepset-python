# User
(*user*)

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
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.user.delete(user_id='29921aef-b9f5-48c4-986e-68e4be056013')

if res.delete_user_api_v1_users_user_id_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `user_id`                                                                             | *str*                                                                                 | :heavy_check_mark:                                                                    | A unique identifier of the user. You can obtain it by running the Get Users endpoint. |


### Response

**[operations.DeleteUserAPIV1UsersUserIDDeleteResponse](../../models/operations/deleteuserapiv1usersuseriddeleteresponse.md)**


## get

Retrieves the properties of the user object. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.user.get(user_id='f59da757-a59e-4cfe-b66e-f1caa3383c2b')

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `user_id`                                                                             | *str*                                                                                 | :heavy_check_mark:                                                                    | A unique identifier of the user. You can obtain it by running the Get Users endpoint. |


### Response

**[operations.GetUserAPIV1UsersUserIDGetResponse](../../models/operations/getuserapiv1usersuseridgetresponse.md)**


## list

Retrieves the properties of all the user objects in your organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.ListUsersAPIV1UsersGetRequest(
    after='eb477373-c8d7-42f6-8d1d-b1f2c4310661',
    before='e96349e1-cf9e-406e-ba43-7000ae6b6bc9',
    include_deleted=False,
    limit=709036,
    page_number=537236,
)

res = s.user.list(req)

if res.user_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListUsersAPIV1UsersGetRequest](../../models/operations/listusersapiv1usersgetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.ListUsersAPIV1UsersGetResponse](../../models/operations/listusersapiv1usersgetresponse.md)**


## me

Retrieves the properties of the user object. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.user.me()

if res.user is not None:
    # handle response
```


### Response

**[operations.ReadUsersMeAPIV1MeGetResponse](../../models/operations/readusersmeapiv1megetresponse.md)**


## update_permission

Updates user permissions. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.user.update_permission(request_body=operations.UpdateUserPermissionAPIV1UsersUserIDPatchUserRole(
    role=shared.RolesToDB.FOUR,
), user_id='759eac55-a974-41d3-9135-2965bb8a7202')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                               | [operations.UpdateUserPermissionAPIV1UsersUserIDPatchUserRole](../../models/operations/updateuserpermissionapiv1usersuseridpatchuserrole.md) | :heavy_check_mark:                                                                                                                           | N/A                                                                                                                                          |
| `user_id`                                                                                                                                    | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | A unique identifier of the user. You can obtain it by running the Get Users endpoint.                                                        |


### Response

**[operations.UpdateUserPermissionAPIV1UsersUserIDPatchResponse](../../models/operations/updateuserpermissionapiv1usersuseridpatchresponse.md)**

