# Workspace
(*workspace*)

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
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = shared.WorkspaceName(
    name='Anna Bergnaum',
)

res = s.workspace.create(req)

if res.create_workspace_api_v1_workspaces_post_201_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.WorkspaceName](../../models/shared/workspacename.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.CreateWorkspaceAPIV1WorkspacesPostResponse](../../models/operations/createworkspaceapiv1workspacespostresponse.md)**


## delete

Deletes a workspace and everything that is associated with it. Be careful as this action cannot be undone. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.workspace.delete(workspace_name='exercitationem')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.DeleteWorkspaceAPIV1WorkspacesWorkspaceNameDeleteResponse](../../models/operations/deleteworkspaceapiv1workspacesworkspacenamedeleteresponse.md)**


## get

Returns the workspace and its properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.workspace.get(workspace_name='itaque')

if res.workspace is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.GetWorkspaceAPIV1WorkspacesWorkspaceNameGetResponse](../../models/operations/getworkspaceapiv1workspacesworkspacenamegetresponse.md)**


## get_stats

Displays the number of files and documents in a workspace, the number of search requests, and the average response time. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.workspace.get_stats(workspace_name='et')

if res.workspace_stats is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.GetWorkspaceStatsAPIV1WorkspacesWorkspaceNameStatsGetResponse](../../models/operations/getworkspacestatsapiv1workspacesworkspacenamestatsgetresponse.md)**


## list

Lists all deepset Cloud workspaces and their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.workspace.list()

if res.workspace_list is not None:
    # handle response
```


### Response

**[operations.ListWorkspacesAPIV1WorkspacesGetResponse](../../models/operations/listworkspacesapiv1workspacesgetresponse.md)**


## search_count

Returns the number of search requests on a given day for a specified period of time. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetRequest(
    after='39dbc225-9b1a-4bda-8c07-0e1084cb0672',
    before='d1ad879e-eb96-465b-85ef-bd02bae0be2d',
    limit=483518,
    page_number=510128,
    workspace_name='odit',
)

res = s.workspace.search_count(req)

if res.search_count_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetRequest](../../models/operations/searchcountapiv1workspacesworkspacenamesearchcountgetrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetResponse](../../models/operations/searchcountapiv1workspacesworkspacenamesearchcountgetresponse.md)**


## search_history

Returns the search history which includes information such as the query, the answer, the pipeline used, and more. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetRequest(
    after='259e3ea4-b519-47f9-a443-da7ce52b895c',
    before='537c6454-efb0-4b34-896c-3ca5acfbe2fd',
    limit=362888,
    page_number=441321,
    workspace_name='aperiam',
)

res = s.workspace.search_history(req)

if res.search_history_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetRequest](../../models/operations/searchhistoryapiv1workspacesworkspacenamesearchhistorygetrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetResponse](../../models/operations/searchhistoryapiv1workspacesworkspacenamesearchhistorygetresponse.md)**

