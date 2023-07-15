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
), shared.PostSharedPrototype(
    description='sit',
    expiration_date=dateutil.parser.isoparse('2021-02-14T22:16:10.503Z'),
    pipeline_names=[
        'minima',
        'recusandae',
    ],
    show_files=False,
    show_metadata_filters=False,
), 'reiciendis')

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
), 'nulla', '20e457e1-858b-46a8-9fbe-3a5aa8e4824d')

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
), '0ab40750-88e5-4186-a065-e904f3b1194b', 'atque')

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
    after='abf603a7-9f9d-4fe0-ab7d-a8a50ce187f8',
    before='6bc173d6-89ee-4e95-a6f8-d986e881ead4',
    filter='reiciendis',
    limit=42976,
    page_number=919783,
    workspace_name='dicta',
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
), '012563f9-4e29-4e97-be92-2a57a15be3e0', 'iure')

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
), shared.PatchSharedPrototype(
    description='ipsa',
    show_files=False,
    show_metadata_filters=False,
), '807e2b6e-3ab8-4845-b059-7a60ff2a54a3', 'quae')

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

