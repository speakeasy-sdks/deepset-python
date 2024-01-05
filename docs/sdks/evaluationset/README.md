# EvaluationSet
(*evaluation_set*)

### Available Operations

* [delete](#delete) - Delete Evaluation Set
* [get](#get) - Get Evaluation Set
* [get_csv](#get_csv) - Get Evaluation Set Csv File
* [import_evaluation_set](#import_evaluation_set) - Import Evaluation Set
* [list](#list) - Get Evaluation Sets
* [retrigger](#retrigger) - Retrigger Label Matching

## delete

Deletes an evaluation set from the workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.evaluation_set.delete(evaluation_set_name='string', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `evaluation_set_name`                     | *str*                                     | :heavy_check_mark:                        | The name of the evaluation set to delete. |
| `workspace_name`                          | *str*                                     | :heavy_check_mark:                        | Type the name of the workspace.           |


### Response

**[operations.DeleteEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameDeleteResponse](../../models/operations/deleteevaluationsetapiv1workspacesworkspacenameevaluationsetsevaluationsetnamedeleteresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## get

Returns the contents of the evaluation set.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.evaluation_set.get(evaluation_set_name='string', workspace_name='string')

if res.label_list is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                 | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `evaluation_set_name`                     | *str*                                     | :heavy_check_mark:                        | The name of the evaluation set to return. |
| `workspace_name`                          | *str*                                     | :heavy_check_mark:                        | Type the name of the workspace.           |


### Response

**[operations.GetEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameGetResponse](../../models/operations/getevaluationsetapiv1workspacesworkspacenameevaluationsetsevaluationsetnamegetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## get_csv

Fetches the evaluation set as a CSV file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.evaluation_set.get_csv(evaluation_set_name='string', workspace_name='string')

if res.two_hundred_application_json_any is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `evaluation_set_name`                    | *str*                                    | :heavy_check_mark:                       | The name of the evaluation set to fetch. |
| `workspace_name`                         | *str*                                    | :heavy_check_mark:                       | Type the name of the workspace.          |


### Response

**[operations.GetEvaluationSetCsvFileAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameCsvGetResponse](../../models/operations/getevaluationsetcsvfileapiv1workspacesworkspacenameevaluationsetsevaluationsetnamecsvgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## import_evaluation_set

Imports an evaluation set into deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.evaluation_set.import_evaluation_set(body_import_evaluation_set_api_v1_workspaces_workspace_name_evaluation_sets_import_post=components.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPost(
    file=components.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostFile(
        content='0xe0a9E4eDCB'.encode(),
        file_name='forward.jpeg',
    ),
), workspace_name='string')

if res.evaluation_set_import is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                        | Type                                                                                                                                                                                             | Required                                                                                                                                                                                         | Description                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `body_import_evaluation_set_api_v1_workspaces_workspace_name_evaluation_sets_import_post`                                                                                                        | [components.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPost](../../models/components/bodyimportevaluationsetapiv1workspacesworkspacenameevaluationsetsimportpost.md) | :heavy_check_mark:                                                                                                                                                                               | N/A                                                                                                                                                                                              |
| `workspace_name`                                                                                                                                                                                 | *str*                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                               | Type the name of the workspace.                                                                                                                                                                  |


### Response

**[operations.ImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostResponse](../../models/operations/importevaluationsetapiv1workspacesworkspacenameevaluationsetsimportpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## list

Displays all evaluation sets and their properties.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)

req = operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetRequest(
    workspace_name='string',
)

res = s.evaluation_set.list(req)

if res.evaluation_set_pagination is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                              | [operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetRequest](../../models/operations/listevaluationsetsapiv1workspacesworkspacenameevaluationsetsgetrequest.md) | :heavy_check_mark:                                                                                                                                                                     | The request object to use for the request.                                                                                                                                             |


### Response

**[operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetResponse](../../models/operations/listevaluationsetsapiv1workspacesworkspacenameevaluationsetsgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

## retrigger

Retrigger matching labels from an evaluation set to the files in your workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.evaluation_set.retrigger(evaluation_set_name='string', workspace_name='string')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `evaluation_set_name`                                    | *str*                                                    | :heavy_check_mark:                                       | Which evaluation set do you want to view? Type its name. |
| `workspace_name`                                         | *str*                                                    | :heavy_check_mark:                                       | Type the name of the workspace.                          |


### Response

**[operations.RetriggerLabelMatchingAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameLabelMatchingPostResponse](../../models/operations/retriggerlabelmatchingapiv1workspacesworkspacenameevaluationsetsevaluationsetnamelabelmatchingpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |
