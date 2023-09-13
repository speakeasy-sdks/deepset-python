# shared_prototype

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

s = deepset_cloud.DeepsetCloud()


res = s.shared_prototype.create(operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostSecurity(
    http_bearer="",
), post_shared_prototype=shared.PostSharedPrototype(
    description='occaecati',
    expiration_date=dateutil.parser.isoparse('2021-01-18T16:49:49.451Z'),
    pipeline_names=[
        'tempora',
    ],
    show_files=False,
    show_metadata_filters=False,
), workspace_name='tempora')

if res.shared_prototype is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                               | [operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostSecurity](../../models/operations/createprototypeapiv1workspacesworkspacenamesharedprototypespostsecurity.md) | :heavy_check_mark:                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                        |
| `post_shared_prototype`                                                                                                                                                                  | [shared.PostSharedPrototype](../../models/shared/postsharedprototype.md)                                                                                                                 | :heavy_check_mark:                                                                                                                                                                       | N/A                                                                                                                                                                                      |
| `workspace_name`                                                                                                                                                                         | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | Type the name of the workspace.                                                                                                                                                          |


### Response

**[operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostResponse](../../models/operations/createprototypeapiv1workspacesworkspacenamesharedprototypespostresponse.md)**


## create_external_user

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.shared_prototype.create_external_user(operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostSecurity(
    http_bearer="",
), workspace_name='voluptate', existing_user_id='f603e8b4-45e8-40ca-95ef-d20e457e1858')

if res.external_user_information is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                             | [operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostSecurity](../../models/operations/createexternaluserapiv1workspacesworkspacenamesharedprototypeuserspostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                                      |
| `workspace_name`                                                                                                                                                                                       | *str*                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                     | Type the name of the workspace.                                                                                                                                                                        |
| `existing_user_id`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                     | The ID of an existing external user                                                                                                                                                                    |


### Response

**[operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostResponse](../../models/operations/createexternaluserapiv1workspacesworkspacenamesharedprototypeuserspostresponse.md)**


## get

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.shared_prototype.get(operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetSecurity(
    http_bearer="",
), shared_prototype_id='b6a89fbe-3a5a-4a8e-8824-d0ab4075088e', workspace_name='corporis')

if res.shared_prototype is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                     | [operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetSecurity](../../models/operations/getsharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeidgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                                                              |
| `shared_prototype_id`                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                             | The ID of the shared prototype                                                                                                                                                                                                 |
| `workspace_name`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                             | Type the name of the workspace.                                                                                                                                                                                                |


### Response

**[operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetResponse](../../models/operations/getsharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeidgetresponse.md)**


## list

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest(
    after='1862065e-904f-43b1-994b-8abf603a79f9',
    before='dfe0ab7d-a8a5-40ce-987f-86bc173d689e',
    filter='officiis',
    limit=880107,
    page_number=618826,
    workspace_name='minima',
)

res = s.shared_prototype.list(req, operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetSecurity(
    http_bearer="",
))

if res.paginated_shared_prototypes is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                            | [operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest](../../models/operations/listprototypesapiv1workspacesworkspacenamesharedprototypesgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                   | The request object to use for the request.                                                                                                                                           |
| `security`                                                                                                                                                                           | [operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetSecurity](../../models/operations/listprototypesapiv1workspacesworkspacenamesharedprototypesgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                   | The security requirements to use for the request.                                                                                                                                    |


### Response

**[operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetResponse](../../models/operations/listprototypesapiv1workspacesworkspacenamesharedprototypesgetresponse.md)**


## revoke

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.shared_prototype.revoke(operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteSecurity(
    http_bearer="",
), shared_prototype_id='26f8d986-e881-4ead-8f0e-1012563f94e2', workspace_name='occaecati')

if res.revoke_shared_prototype_api_v1_workspaces_workspace_name_shared_prototypes_shared_prototype_id_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                                 | [operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteSecurity](../../models/operations/revokesharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeiddeletesecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                         | The security requirements to use for the request.                                                                                                                                                                                          |
| `shared_prototype_id`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | The ID of the shared prototype                                                                                                                                                                                                             |
| `workspace_name`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | Type the name of the workspace.                                                                                                                                                                                                            |


### Response

**[operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteResponse](../../models/operations/revokesharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeiddeleteresponse.md)**


## update

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.shared_prototype.update(operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchSecurity(
    http_bearer="",
), patch_shared_prototype=shared.PatchSharedPrototype(
    description='officiis',
    show_files=False,
    show_metadata_filters=False,
), shared_prototype_id='973e922a-57a1-45be-be06-0807e2b6e3ab', workspace_name='voluptatum')

if res.shared_prototype is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                           | [operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchSecurity](../../models/operations/editsharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeidpatchsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                   | The security requirements to use for the request.                                                                                                                                                                                    |
| `patch_shared_prototype`                                                                                                                                                                                                             | [shared.PatchSharedPrototype](../../models/shared/patchsharedprototype.md)                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                  |
| `shared_prototype_id`                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                   | The ID of the shared prototype                                                                                                                                                                                                       |
| `workspace_name`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                   | Type the name of the workspace.                                                                                                                                                                                                      |


### Response

**[operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchResponse](../../models/operations/editsharedprototypeapiv1workspacesworkspacenamesharedprototypessharedprototypeidpatchresponse.md)**

