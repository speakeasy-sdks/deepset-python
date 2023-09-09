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
), user_id='813d5208-ece7-4e25-bb66-8451c6c6e205')

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
), user_id='e16deab3-fec9-4578-a645-84273a8418d1')

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
    after='62309fb0-9299-421a-afb9-f58c4d86e68e',
    before='4be05601-3f59-4da7-97a5-9ecfef66ef1c',
    include_deleted=False,
    limit=685478,
    page_number=675689,
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
    role=shared.RolesToDB.ONE,
), user_id='383c2beb-4773-473c-8d72-f64d1db1f2c4')

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

