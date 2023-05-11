# workspace

### Available Operations

* [create](#create) - Create Workspace [private]
* [delete](#delete) - Delete Workspace [private]
* [get](#get) - Get Workspace [private]
* [get_stats](#get_stats) - Get Workspace Stats [private]
* [list](#list) - List Workspaces [private]
* [search_count](#search_count) - Search Count [private]
* [search_history](#search_history) - Search History [private]

## create

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = shared.WorkspaceName(
    name='Camille Crist',
)

res = s.workspace.create(req, operations.CreateWorkspaceAPIV1WorkspacesPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.create_workspace_api_v1_workspaces_post_201_application_json_any is not None:
    # handle response
```

## delete

Deletes a workspace and everything that is associated with it. Be careful as this action cannot be undone. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteWorkspaceAPIV1WorkspacesWorkspaceNameDeleteRequest(
    workspace_name='velit',
)

res = s.workspace.delete(req, operations.DeleteWorkspaceAPIV1WorkspacesWorkspaceNameDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## get

Returns the workspace and its properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetWorkspaceAPIV1WorkspacesWorkspaceNameGetRequest(
    workspace_name='illo',
)

res = s.workspace.get(req, operations.GetWorkspaceAPIV1WorkspacesWorkspaceNameGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.workspace is not None:
    # handle response
```

## get_stats

Displays the number of files and documents in a workspace, the number of search requests, and the average response time. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetWorkspaceStatsAPIV1WorkspacesWorkspaceNameStatsGetRequest(
    workspace_name='accusantium',
)

res = s.workspace.get_stats(req, operations.GetWorkspaceStatsAPIV1WorkspacesWorkspaceNameStatsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.workspace_stats is not None:
    # handle response
```

## list

Lists all deepset Cloud workspaces and their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.workspace.list(operations.ListWorkspacesAPIV1WorkspacesGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.workspace_list is not None:
    # handle response
```

## search_count

Returns the number of search requests on a given day for a specified period of time. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetRequest(
    after='661e9634-9e1c-4f9e-86e3-a437000ae6b6',
    before='bc9b8f75-9eac-455a-9741-d311352965bb',
    limit=526907,
    page_number=678060,
    workspace_name='odio',
)

res = s.workspace.search_count(req, operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.search_count_pagination is not None:
    # handle response
```

## search_history

Returns the search history which includes information such as the query, the answer, the pipeline used, and more. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetRequest(
    after='20261143-5e13-49db-8225-9b1abda8c070',
    before='e1084cb0-672d-41ad-879e-eb9665b85efb',
    limit=872303,
    page_number=5152,
    workspace_name='quia',
)

res = s.workspace.search_history(req, operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.search_history_pagination is not None:
    # handle response
```
