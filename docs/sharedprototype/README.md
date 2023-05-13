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
        description='voluptatem',
        expiration_date=dateutil.parser.isoparse('2021-07-31T10:53:55.286Z'),
        pipeline_names=[
            'consequatur',
            'esse',
        ],
        show_files=False,
        show_metadata_filters=False,
    ),
    workspace_name='ipsam',
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
    existing_user_id='088e5186-2065-4e90-8f3b-1194b8abf603',
    workspace_name='deserunt',
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
    shared_prototype_id='79f9dfe0-ab7d-4a8a-90ce-187f86bc173d',
    workspace_name='ea',
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
    after='89eee952-6f8d-4986-a881-ead4f0e10125',
    before='63f94e29-e973-4e92-aa57-a15be3e06080',
    filter='molestiae',
    limit=907733,
    page_number=184362,
    workspace_name='cum',
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
    shared_prototype_id='6e3ab884-5f05-497a-a0ff-2a54a31e9476',
    workspace_name='ut',
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
        description='culpa',
        show_files=False,
        show_metadata_filters=False,
    ),
    shared_prototype_id='3e865e79-56f9-4251-a5a9-da660ff57bfa',
    workspace_name='laborum',
)

res = s.shared_prototype.update(req, operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.shared_prototype is not None:
    # handle response
```
