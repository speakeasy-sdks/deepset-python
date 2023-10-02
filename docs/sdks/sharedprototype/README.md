# SharedPrototype
(*shared_prototype*)

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
import deepset_cloud
import dateutil.parser
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.shared_prototype.create(post_shared_prototype=shared.PostSharedPrototype(
    description='Multi-tiered human-resource model',
    expiration_date=dateutil.parser.isoparse('2023-07-30T20:06:15.478Z'),
    pipeline_names=[
        'Money',
    ],
    show_files=False,
    show_metadata_filters=False,
), workspace_name='blue')

if res.shared_prototype is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `post_shared_prototype`                                                  | [shared.PostSharedPrototype](../../models/shared/postsharedprototype.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `workspace_name`                                                         | *str*                                                                    | :heavy_check_mark:                                                       | Type the name of the workspace.                                          |


### Response

**[operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostResponse](../../models/operations/createprototypeapiv1workspacesworkspacenamesharedprototypespostresponse.md)**


## create_external_user

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.shared_prototype.create_external_user(workspace_name='lime', existing_user_id='14aeb0f3-8aed-4e02-86c6-a3a8239cb022')

if res.external_user_information is not None:
    # handle response
```

### Parameters

| Parameter                           | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `workspace_name`                    | *str*                               | :heavy_check_mark:                  | Type the name of the workspace.     |
| `existing_user_id`                  | *Optional[str]*                     | :heavy_minus_sign:                  | The ID of an existing external user |


### Response

**[operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostResponse](../../models/operations/createexternaluserapiv1workspacesworkspacenamesharedprototypeuserspostresponse.md)**


## get

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.shared_prototype.get(shared_prototype_id='b18d8d81-fd7b-4764-a31e-475cb1f36591', workspace_name='Optional')

if res.shared_prototype is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `shared_prototype_id`           | *str*                           | :heavy_check_mark:              | The ID of the shared prototype  |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetResponse](../../models/operations/getsharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeidgetresponse.md)**


## list

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest(
    after='c184a429-302e-4aca-80db-f1718b882a50',
    before='80555741-9e79-40e2-b205-5dd402eb66ec',
    filter='bedrock',
    limit=614946,
    page_number=897069,
    workspace_name='Virginia SMTP',
)

res = s.shared_prototype.list(req)

if res.paginated_shared_prototypes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                          | [operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest](../../models/operations/listprototypesapiv1workspacesworkspacenamesharedprototypesgetrequest.md) | :heavy_check_mark:                                                                                                                                                                 | The request object to use for the request.                                                                                                                                         |


### Response

**[operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetResponse](../../models/operations/listprototypesapiv1workspacesworkspacenamesharedprototypesgetresponse.md)**


## revoke

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.shared_prototype.revoke(shared_prototype_id='db021625-f680-4f7d-9078-89cd3534dba0', workspace_name='Hop')

if res.revoke_shared_prototype_api_v1_workspaces_workspace_name_shared_prototypes_shared_prototype_id_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `shared_prototype_id`           | *str*                           | :heavy_check_mark:              | The ID of the shared prototype  |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteResponse](../../models/operations/revokesharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeiddeleteresponse.md)**


## update

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.shared_prototype.update(patch_shared_prototype=shared.PatchSharedPrototype(
    description='Synchronised 3rd generation matrix',
    show_files=False,
    show_metadata_filters=False,
), shared_prototype_id='05bf4aa7-7f20-44e7-b54c-352acfe54077', workspace_name='Bicycle')

if res.shared_prototype is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `patch_shared_prototype`                                                   | [shared.PatchSharedPrototype](../../models/shared/patchsharedprototype.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `shared_prototype_id`                                                      | *str*                                                                      | :heavy_check_mark:                                                         | The ID of the shared prototype                                             |
| `workspace_name`                                                           | *str*                                                                      | :heavy_check_mark:                                                         | Type the name of the workspace.                                            |


### Response

**[operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchResponse](../../models/operations/editsharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeidpatchresponse.md)**

