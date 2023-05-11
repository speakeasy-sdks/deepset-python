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
    evaluation_set_name='qui',
    workspace_name='ipsum',
)

res = s.evaluation_set.delete(req, operations.DeleteEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    evaluation_set_name='hic',
    workspace_name='excepturi',
)

res = s.evaluation_set.get(req, operations.GetEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    evaluation_set_name='cum',
    workspace_name='voluptate',
)

res = s.evaluation_set.get_csv(req, operations.GetEvaluationSetCsvFileAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameCsvGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
            file='dignissimos',
            content='reiciendis'.encode(),
        ),
    ),
    workspace_name='amet',
)

res = s.evaluation_set.import_evaluation_set(req, operations.ImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    after='a4100674-ebf6-4928-8d1b-a77a89ebf737',
    before='ae4203ce-5e6a-495d-8a0d-446ce2af7a73',
    limit=788740,
    name='Marvin Renner',
    page_number=313692,
    workspace_name='dolorem',
)

res = s.evaluation_set.list(req, operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    evaluation_set_name='sapiente',
    workspace_name='totam',
)

res = s.evaluation_set.retrigger(req, operations.RetriggerLabelMatchingAPIV1WorkspacesWorkspaceNameEvaluationSetsEvaluationSetNameLabelMatchingPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```
