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
    name='Margarita Jacobson',
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
    workspace_name='libero',
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
    workspace_name='rem',
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
    workspace_name='dolorum',
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
    after='72026114-35e1-439d-bc22-59b1abda8c07',
    before='0e1084cb-0672-4d1a-9879-eeb9665b85ef',
    limit=737279,
    page_number=872303,
    workspace_name='alias',
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
    after='2bae0be2-d782-4259-a3ea-4b5197f92443',
    before='da7ce52b-895c-4537-8645-4efb0b34896c',
    limit=242099,
    page_number=795591,
    workspace_name='fuga',
)

res = s.workspace.search_history(req, operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.search_history_pagination is not None:
    # handle response
```
