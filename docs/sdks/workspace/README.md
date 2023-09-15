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
    name='Martha Bashirian',
)

res = s.workspace.create(req, operations.CreateWorkspaceAPIV1WorkspacesPostSecurity(
    http_bearer="",
))

if res.create_workspace_api_v1_workspaces_post_201_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [shared.WorkspaceName](../../models/shared/workspacename.md)                                                                   | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |
| `security`                                                                                                                     | [operations.CreateWorkspaceAPIV1WorkspacesPostSecurity](../../models/operations/createworkspaceapiv1workspacespostsecurity.md) | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |


### Response

**[operations.CreateWorkspaceAPIV1WorkspacesPostResponse](../../models/operations/createworkspaceapiv1workspacespostresponse.md)**


## delete

Deletes a workspace and everything that is associated with it. Be careful as this action cannot be undone. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.workspace.delete(operations.DeleteWorkspaceAPIV1WorkspacesWorkspaceNameDeleteSecurity(
    http_bearer="",
), workspace_name='beatae')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                   | [operations.DeleteWorkspaceAPIV1WorkspacesWorkspaceNameDeleteSecurity](../../models/operations/deleteworkspaceapiv1workspacesworkspacenamedeletesecurity.md) | :heavy_check_mark:                                                                                                                                           | The security requirements to use for the request.                                                                                                            |
| `workspace_name`                                                                                                                                             | *str*                                                                                                                                                        | :heavy_check_mark:                                                                                                                                           | Type the name of the workspace.                                                                                                                              |


### Response

**[operations.DeleteWorkspaceAPIV1WorkspacesWorkspaceNameDeleteResponse](../../models/operations/deleteworkspaceapiv1workspacesworkspacenamedeleteresponse.md)**


## get

Returns the workspace and its properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.workspace.get(operations.GetWorkspaceAPIV1WorkspacesWorkspaceNameGetSecurity(
    http_bearer="",
), workspace_name='vero')

if res.workspace is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                       | [operations.GetWorkspaceAPIV1WorkspacesWorkspaceNameGetSecurity](../../models/operations/getworkspaceapiv1workspacesworkspacenamegetsecurity.md) | :heavy_check_mark:                                                                                                                               | The security requirements to use for the request.                                                                                                |
| `workspace_name`                                                                                                                                 | *str*                                                                                                                                            | :heavy_check_mark:                                                                                                                               | Type the name of the workspace.                                                                                                                  |


### Response

**[operations.GetWorkspaceAPIV1WorkspacesWorkspaceNameGetResponse](../../models/operations/getworkspaceapiv1workspacesworkspacenamegetresponse.md)**


## get_stats

Displays the number of files and documents in a workspace, the number of search requests, and the average response time. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.workspace.get_stats(operations.GetWorkspaceStatsAPIV1WorkspacesWorkspaceNameStatsGetSecurity(
    http_bearer="",
), workspace_name='excepturi')

if res.workspace_stats is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                           | [operations.GetWorkspaceStatsAPIV1WorkspacesWorkspaceNameStatsGetSecurity](../../models/operations/getworkspacestatsapiv1workspacesworkspacenamestatsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                   | The security requirements to use for the request.                                                                                                                    |
| `workspace_name`                                                                                                                                                     | *str*                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                   | Type the name of the workspace.                                                                                                                                      |


### Response

**[operations.GetWorkspaceStatsAPIV1WorkspacesWorkspaceNameStatsGetResponse](../../models/operations/getworkspacestatsapiv1workspacesworkspacenamestatsgetresponse.md)**


## list

Lists all deepset Cloud workspaces and their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.workspace.list(operations.ListWorkspacesAPIV1WorkspacesGetSecurity(
    http_bearer="",
))

if res.workspace_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                 | [operations.ListWorkspacesAPIV1WorkspacesGetSecurity](../../models/operations/listworkspacesapiv1workspacesgetsecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |


### Response

**[operations.ListWorkspacesAPIV1WorkspacesGetResponse](../../models/operations/listworkspacesapiv1workspacesgetresponse.md)**


## search_count

Returns the number of search requests on a given day for a specified period of time. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetRequest(
    after='6349e1cf-9e06-4e3a-8370-00ae6b6bc9b8',
    before='f759eac5-5a97-441d-b113-52965bb8a720',
    limit=168042,
    page_number=425402,
    workspace_name='quae',
)

res = s.workspace.search_count(req, operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetSecurity(
    http_bearer="",
))

if res.search_count_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetRequest](../../models/operations/searchcountapiv1workspacesworkspacenamesearchcountgetrequest.md)   | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |
| `security`                                                                                                                                                           | [operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetSecurity](../../models/operations/searchcountapiv1workspacesworkspacenamesearchcountgetsecurity.md) | :heavy_check_mark:                                                                                                                                                   | The security requirements to use for the request.                                                                                                                    |


### Response

**[operations.SearchCountAPIV1WorkspacesWorkspaceNameSearchCountGetResponse](../../models/operations/searchcountapiv1workspacesworkspacenamesearchcountgetresponse.md)**


## search_history

Returns the search history which includes information such as the query, the answer, the pipeline used, and more. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetRequest(
    after='1435e139-dbc2-4259-b1ab-da8c070e1084',
    before='cb0672d1-ad87-49ee-b966-5b85efbd02ba',
    limit=919508,
    page_number=34070,
    workspace_name='expedita',
)

res = s.workspace.search_history(req, operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetSecurity(
    http_bearer="",
))

if res.search_history_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetRequest](../../models/operations/searchhistoryapiv1workspacesworkspacenamesearchhistorygetrequest.md)   | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |
| `security`                                                                                                                                                                   | [operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetSecurity](../../models/operations/searchhistoryapiv1workspacesworkspacenamesearchhistorygetsecurity.md) | :heavy_check_mark:                                                                                                                                                           | The security requirements to use for the request.                                                                                                                            |


### Response

**[operations.SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetResponse](../../models/operations/searchhistoryapiv1workspacesworkspacenamesearchhistorygetresponse.md)**

