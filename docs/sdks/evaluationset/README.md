# evaluation_set

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

s = deepset_cloud.DeepsetCloud()


res = s.evaluation_set.delete(operations.DeleteEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameDeleteSecurity(
    http_bearer="",
), evaluation_set_name='iste', workspace_name='dolorum')

if res.delete_evaluation_set_api_v1_workspaces_workspace_name_evaluation_sets_evaluation_set_name_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                         | [operations.DeleteEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameDeleteSecurity](../../models/operations/deleteevaluationsetapiv1workspacesworkspacenameevaluationsetsevaluationsetnamedeletesecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                                                                  |
| `evaluation_set_name`                                                                                                                                                                                                              | *str*                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                 | The name of the evaluation set to delete.                                                                                                                                                                                          |
| `workspace_name`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                 | Type the name of the workspace.                                                                                                                                                                                                    |


### Response

**[operations.DeleteEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameDeleteResponse](../../models/operations/deleteevaluationsetapiv1workspacesworkspacenameevaluationsetsevaluationsetnamedeleteresponse.md)**


## get

Returns the contents of the evaluation set.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.evaluation_set.get(operations.GetEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameGetSecurity(
    http_bearer="",
), evaluation_set_name='deleniti', workspace_name='pariatur')

if res.label_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                              | Type                                                                                                                                                                                                                   | Required                                                                                                                                                                                                               | Description                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                             | [operations.GetEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameGetSecurity](../../models/operations/getevaluationsetapiv1workspacesworkspacenameevaluationsetsevaluationsetnamegetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                                                      |
| `evaluation_set_name`                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                     | The name of the evaluation set to return.                                                                                                                                                                              |
| `workspace_name`                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                     | Type the name of the workspace.                                                                                                                                                                                        |


### Response

**[operations.GetEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameGetResponse](../../models/operations/getevaluationsetapiv1workspacesworkspacenameevaluationsetsevaluationsetnamegetresponse.md)**


## get_csv

Fetches the evaluation set as a CSV file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.evaluation_set.get_csv(operations.GetEvaluationSetCsvFileAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameCsvGetSecurity(
    http_bearer="",
), evaluation_set_name='provident', workspace_name='nobis')

if res.get_evaluation_set_csv_file_api_v1_workspaces_workspace_name_evaluation_sets_evaluation_set_name_csv_get_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                                 | [operations.GetEvaluationSetCsvFileAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameCsvGetSecurity](../../models/operations/getevaluationsetcsvfileapiv1workspacesworkspacenameevaluationsetsevaluationsetnamecsvgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                         | The security requirements to use for the request.                                                                                                                                                                                          |
| `evaluation_set_name`                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | The name of the evaluation set to fetch.                                                                                                                                                                                                   |
| `workspace_name`                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                         | Type the name of the workspace.                                                                                                                                                                                                            |


### Response

**[operations.GetEvaluationSetCsvFileAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameCsvGetResponse](../../models/operations/getevaluationsetcsvfileapiv1workspacesworkspacenameevaluationsetsevaluationsetnamecsvgetresponse.md)**


## import_evaluation_set

Imports an evaluation set into deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.evaluation_set.import_evaluation_set(operations.ImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostSecurity(
    http_bearer="",
), body_import_evaluation_set_api_v1_workspaces_workspace_name_evaluation_sets_import_post=shared.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPost(
    file=shared.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostFile(
        file='libero',
        content='delectus'.encode(),
    ),
), workspace_name='quaerat')

if res.evaluation_set_import is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                               | [operations.ImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostSecurity](../../models/operations/importevaluationsetapiv1workspacesworkspacenameevaluationsetsimportpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                                        |
| `body_import_evaluation_set_api_v1_workspaces_workspace_name_evaluation_sets_import_post`                                                                                                                | [shared.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPost](../../models/shared/bodyimportevaluationsetapiv1workspacesworkspacenameevaluationsetsimportpost.md)                 | :heavy_check_mark:                                                                                                                                                                                       | N/A                                                                                                                                                                                                      |
| `workspace_name`                                                                                                                                                                                         | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | Type the name of the workspace.                                                                                                                                                                          |


### Response

**[operations.ImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostResponse](../../models/operations/importevaluationsetapiv1workspacesworkspacenameevaluationsetsimportpostresponse.md)**


## list

Displays all evaluation sets and their properties.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetRequest(
    after='8633323f-9b77-4f3a-8100-674ebf69280d',
    before='1ba77a89-ebf7-437a-a420-3ce5e6a95d8a',
    limit=55,
    name='Alex Goodwin',
    page_number=885338,
    workspace_name='qui',
)

res = s.evaluation_set.list(req, operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetSecurity(
    http_bearer="",
))

if res.evaluation_set_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                | [operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetRequest](../../models/operations/listevaluationsetsapiv1workspacesworkspacenameevaluationsetsgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                       | The request object to use for the request.                                                                                                                                               |
| `security`                                                                                                                                                                               | [operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetSecurity](../../models/operations/listevaluationsetsapiv1workspacesworkspacenameevaluationsetsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                        |


### Response

**[operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetResponse](../../models/operations/listevaluationsetsapiv1workspacesworkspacenameevaluationsetsgetresponse.md)**


## retrigger

Retrigger matching labels from an evaluation set to the files in your workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.evaluation_set.retrigger(operations.RetriggerLabelMatchingAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameLabelMatchingPostSecurity(
    http_bearer="",
), evaluation_set_name='dolorum', workspace_name='a')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                                                     | [operations.RetriggerLabelMatchingAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameLabelMatchingPostSecurity](../../models/operations/retriggerlabelmatchingapiv1workspacesworkspacenameevaluationsetsevaluationsetnamelabelmatchingpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                                                                                              |
| `evaluation_set_name`                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                             | Which evaluation set do you want to view? Type its name.                                                                                                                                                                                                       |
| `workspace_name`                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                             | Type the name of the workspace.                                                                                                                                                                                                                                |


### Response

**[operations.RetriggerLabelMatchingAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameLabelMatchingPostResponse](../../models/operations/retriggerlabelmatchingapiv1workspacesworkspacenameevaluationsetsevaluationsetnamelabelmatchingpostresponse.md)**

