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
        description='incidunt',
        expiration_date=dateutil.parser.isoparse('2022-05-29T20:03:41.130Z'),
        pipeline_names=[
            'necessitatibus',
            'ipsum',
        ],
        show_files=False,
        show_metadata_filters=False,
    ),
    workspace_name='ea',
)

res = s.shared_prototype.create(req, operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    existing_user_id='98f447f6-03e8-4b44-9e80-ca55efd20e45',
    workspace_name='in',
)

res = s.shared_prototype.create_external_user(req, operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    shared_prototype_id='e1858b6a-89fb-4e3a-9aa8-e4824d0ab407',
    workspace_name='ipsam',
)

res = s.shared_prototype.get(req, operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    after='088e5186-2065-4e90-8f3b-1194b8abf603',
    before='a79f9dfe-0ab7-4da8-a50c-e187f86bc173',
    filter='assumenda',
    limit=410301,
    page_number=539118,
    workspace_name='error',
)

res = s.shared_prototype.list(req, operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    shared_prototype_id='eee9526f-8d98-46e8-81ea-d4f0e1012563',
    workspace_name='a',
)

res = s.shared_prototype.revoke(req, operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
        description='molestias',
        show_files=False,
        show_metadata_filters=False,
    ),
    shared_prototype_id='4e29e973-e922-4a57-a15b-e3e060807e2b',
    workspace_name='iure',
)

res = s.shared_prototype.update(req, operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.shared_prototype is not None:
    # handle response
```
