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

req = operations.DeleteEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameDeleteRequest(
    evaluation_set_name='dolor',
    workspace_name='qui',
)

res = s.evaluation_set.delete(req, operations.DeleteEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameDeleteSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.delete_evaluation_set_api_v1_workspaces_workspace_name_evaluation_sets_evaluation_set_name_delete_200_application_json_any is not None:
    # handle response
```

## get

Returns the contents of the evaluation set.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameGetRequest(
    evaluation_set_name='ipsum',
    workspace_name='hic',
)

res = s.evaluation_set.get(req, operations.GetEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.label_list is not None:
    # handle response
```

## get_csv

Fetches the evaluation set as a CSV file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetEvaluationSetCsvFileAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameCsvGetRequest(
    evaluation_set_name='excepturi',
    workspace_name='cum',
)

res = s.evaluation_set.get_csv(req, operations.GetEvaluationSetCsvFileAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameCsvGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.get_evaluation_set_csv_file_api_v1_workspaces_workspace_name_evaluation_sets_evaluation_set_name_csv_get_200_application_json_any is not None:
    # handle response
```

## import_evaluation_set

Imports an evaluation set into deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.ImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostRequest(
    body_import_evaluation_set_api_v1_workspaces_workspace_name_evaluation_sets_import_post=shared.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPost(
        file=shared.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostFile(
            file='voluptate',
            content='dignissimos'.encode(),
        ),
    ),
    workspace_name='reiciendis',
)

res = s.evaluation_set.import_evaluation_set(req, operations.ImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.evaluation_set_import is not None:
    # handle response
```

## list

Displays all evaluation sets and their properties.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetRequest(
    after='3a410067-4ebf-4692-80d1-ba77a89ebf73',
    before='7ae4203c-e5e6-4a95-98a0-d446ce2af7a7',
    limit=215507,
    name='Saul Fay',
    page_number=253941,
    workspace_name='enim',
)

res = s.evaluation_set.list(req, operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.evaluation_set_pagination is not None:
    # handle response
```

## retrigger

Retrigger matching labels from an evaluation set to the files in your workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.RetriggerLabelMatchingAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameLabelMatchingPostRequest(
    evaluation_set_name='dolorem',
    workspace_name='sapiente',
)

res = s.evaluation_set.retrigger(req, operations.RetriggerLabelMatchingAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameLabelMatchingPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```
