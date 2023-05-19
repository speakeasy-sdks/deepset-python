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

req = operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostRequest(
    post_shared_prototype=shared.PostSharedPrototype(
        description='ut',
        expiration_date=dateutil.parser.isoparse('2022-11-28T21:25:01.550Z'),
        pipeline_names=[
            'expedita',
            'magnam',
            'consequatur',
        ],
        show_files=False,
        show_metadata_filters=False,
    ),
    workspace_name='esse',
)

res = s.shared_prototype.create(req, operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.shared_prototype is not None:
    # handle response
```

## create_external_user

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostRequest(
    existing_user_id='5088e518-6206-45e9-84f3-b1194b8abf60',
    workspace_name='amet',
)

res = s.shared_prototype.create_external_user(req, operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.external_user_information is not None:
    # handle response
```

## get

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetRequest(
    shared_prototype_id='a79f9dfe-0ab7-4da8-a50c-e187f86bc173',
    workspace_name='assumenda',
)

res = s.shared_prototype.get(req, operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.shared_prototype is not None:
    # handle response
```

## list

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest(
    after='689eee95-26f8-4d98-ae88-1ead4f0e1012',
    before='563f94e2-9e97-43e9-a2a5-7a15be3e0608',
    filter='quae',
    limit=474668,
    page_number=907733,
    workspace_name='qui',
)

res = s.shared_prototype.list(req, operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.paginated_shared_prototypes is not None:
    # handle response
```

## revoke

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteRequest(
    shared_prototype_id='b6e3ab88-45f0-4597-a60f-f2a54a31e947',
    workspace_name='ex',
)

res = s.shared_prototype.revoke(req, operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.revoke_shared_prototype_api_v1_workspaces_workspace_name_shared_prototypes_shared_prototype_id_delete_200_application_json_any is not None:
    # handle response
```

## update

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchRequest(
    patch_shared_prototype=shared.PatchSharedPrototype(
        description='ut',
        show_files=False,
        show_metadata_filters=False,
    ),
    shared_prototype_id='a3e865e7-956f-4925-9a5a-9da660ff57bf',
    workspace_name='officia',
)

res = s.shared_prototype.update(req, operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.shared_prototype is not None:
    # handle response
```
