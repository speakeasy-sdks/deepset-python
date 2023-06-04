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
    name='Tina Moore',
)

res = s.workspace.create(req, operations.CreateWorkspaceAPIV1WorkspacesPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
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
    workspace_name='soluta',
)

res = s.workspace.delete(req, operations.DeleteWorkspaceAPIV1WorkspacesWorkspaceNameDeleteSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
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
    workspace_name='libero',
)

res = s.workspace.get(req, operations.GetWorkspaceAPIV1WorkspacesWorkspaceNameGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
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
    workspace_name='rem',
)

res = s.workspace.get_stats(req, operations.GetWorkspaceStatsAPIV1WorkspacesWorkspaceNameStatsGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
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
    http_bearer="YOUR_BEARER_TOKEN_HERE",
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
    after='a7202611-435e-4139-9bc2-259b1abda8c0',
    before='70e1084c-b067-42d1-ad87-9eeb9665b85e',
    limit=972912,
    page_number=737279,
    workspace_name='at',
)

res = s.workspace.search_count(req, operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
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
    after='02bae0be-2d78-4225-9e3e-a4b5197f9244',
    before='3da7ce52-b895-4c53-bc64-54efb0b34896',
    limit=779180,
    page_number=242099,
    workspace_name='minus',
)

res = s.workspace.search_history(req, operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.search_history_pagination is not None:
    # handle response
```
