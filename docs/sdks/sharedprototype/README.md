# SharedPrototype

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
    description='ex',
    expiration_date=dateutil.parser.isoparse('2022-12-23T03:00:58.000Z'),
    pipeline_names=[
        'vel',
    ],
    show_files=False,
    show_metadata_filters=False,
), workspace_name='nostrum')

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


res = s.shared_prototype.create_external_user(workspace_name='saepe', existing_user_id='904f3b11-94b8-4abf-a03a-79f9dfe0ab7d')

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


res = s.shared_prototype.get(shared_prototype_id='a8a50ce1-87f8-46bc-973d-689eee9526f8', workspace_name='at')

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
    after='986e881e-ad4f-40e1-8125-63f94e29e973',
    before='e922a57a-15be-43e0-a080-7e2b6e3ab884',
    filter='ad',
    limit=997963,
    page_number=3099,
    workspace_name='corporis',
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


res = s.shared_prototype.revoke(shared_prototype_id='97a60ff2-a54a-431e-9476-4a3e865e7956', workspace_name='reiciendis')

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
    description='provident',
    show_files=False,
    show_metadata_filters=False,
), shared_prototype_id='251a5a9d-a660-4ff5-bbfa-ad4f9efc1b45', workspace_name='inventore')

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

