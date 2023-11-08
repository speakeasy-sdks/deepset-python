# SharedPrototype
(*.shared_prototype*)

### Available Operations

* [create](#create) - Create Prototype [private]
* [create_external_user](#create_external_user) - Create External User [private]
* [get](#get) - Get Shared Prototype [private]
* [list](#list) - List Prototypes [private]
* [revoke](#revoke) - Revoke Shared Prototype [private]
* [update](#update) - Edit Shared Prototype [private]

## create

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import dateutil.parser
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.create(post_shared_prototype=components.PostSharedPrototype(
    expiration_date=dateutil.parser.isoparse('2022-06-17T19:34:14.348Z'),
    pipeline_names=[
        'string',
    ],
), workspace_name='string')

if res.shared_prototype is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `post_shared_prototype`                                                      | [components.PostSharedPrototype](../../models/shared/postsharedprototype.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `workspace_name`                                                             | *str*                                                                        | :heavy_check_mark:                                                           | Type the name of the workspace.                                              |


### Response

**[operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostResponse](../../models/operations/createprototypeapiv1workspacesworkspacenamesharedprototypespostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## create_external_user

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.create_external_user(workspace_name='string', existing_user_id='cb14aeb0-f38a-4ede-8206-c6a3a8239cb0')

if res.external_user_information is not None:
    # handle response
    pass
```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `workspace_name`                    | *str*                               | :heavy_check_mark:                  | Type the name of the workspace.     |
| `existing_user_id`                  | *Optional[str]*                     | :heavy_minus_sign:                  | The ID of an existing external user |


### Response

**[operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostResponse](../../models/operations/createexternaluserapiv1workspacesworkspacenamesharedprototypeuserspostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.get(shared_prototype_id='b18d8d81-fd7b-4764-a31e-475cb1f36591', workspace_name='string')

if res.shared_prototype is not None:
    # handle response
    pass
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `shared_prototype_id`           | *str*                           | :heavy_check_mark:              | The ID of the shared prototype  |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetResponse](../../models/operations/getsharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeidgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## list

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest(
    workspace_name='string',
)

res = s.shared_prototype.list(req)

if res.paginated_shared_prototypes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                          | [operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest](../../models/operations/listprototypesapiv1workspacesworkspacenamesharedprototypesgetrequest.md) | :heavy_check_mark:                                                                                                                                                                 | The request object to use for the request.                                                                                                                                         |


### Response

**[operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetResponse](../../models/operations/listprototypesapiv1workspacesworkspacenamesharedprototypesgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## revoke

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.revoke(shared_prototype_id='db021625-f680-4f7d-9078-89cd3534dba0', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `shared_prototype_id`           | *str*                           | :heavy_check_mark:              | The ID of the shared prototype  |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteResponse](../../models/operations/revokesharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeiddeleteresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## update

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.update(patch_shared_prototype=components.PatchSharedPrototype(), shared_prototype_id='d0905bf4-aa77-4f20-8e77-54c352acfe54', workspace_name='string')

if res.shared_prototype is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `patch_shared_prototype`                                                       | [components.PatchSharedPrototype](../../models/shared/patchsharedprototype.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `shared_prototype_id`                                                          | *str*                                                                          | :heavy_check_mark:                                                             | The ID of the shared prototype                                                 |
| `workspace_name`                                                               | *str*                                                                          | :heavy_check_mark:                                                             | Type the name of the workspace.                                                |


### Response

**[operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchResponse](../../models/operations/editsharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeidpatchresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |
