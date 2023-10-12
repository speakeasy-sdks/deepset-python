# EvalRun
(*eval_run*)

### Available Operations

* [create_eval_run](#create_eval_run) - Create Eval Run
* [create_tag](#create_tag) - Create Tag [private]
* [delete](#delete) - Delete Eval Run
* [delete_tag](#delete_tag) - Delete Tag [private]
* [get](#get) - Get Eval Run
* [get_node_eval_predictions](#get_node_eval_predictions) - Get Node Eval Predictions
* [list](#list) - Get Eval Runs
* [list_tags](#list_tags) - Get Tags [private]
* [start](#start) - Start Eval Run
* [update](#update) - Edit Eval Run
* [update_tag](#update_tag) - Update Tag [private]

## create_eval_run

Creates an evaluation run for pipeline experiments in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.create_eval_run(eval_run_post=shared.EvalRunPost(
    debug=False,
    evaluation_set_name='Roswell',
    name='Northwest female',
    pipeline_name='Concrete Virginia',
    tags=[
        'Latvian',
    ],
), workspace_name='Bicycle')

if res.eval_run_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `eval_run_post`                                          | [shared.EvalRunPost](../../models/shared/evalrunpost.md) | :heavy_check_mark:                                       | N/A                                                      |
| `workspace_name`                                         | *str*                                                    | :heavy_check_mark:                                       | Type the name of the workspace.                          |


### Response

**[operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostResponse](../../models/operations/createevalrunapiv1workspacesworkspacenameevalrunspostresponse.md)**


## create_tag

Creates a tag for your evaluation run. Tags can help you order and find your evaluation runs later. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.create_tag(request_body=operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostCreateTag(
    name='Niobium hacking Quality',
), workspace_name='traffic')

if res.create_tag_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request_body`                                                                                                                                         | [operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostCreateTag](../../models/operations/createtagapiv1workspacesworkspacenametagspostcreatetag.md) | :heavy_check_mark:                                                                                                                                     | N/A                                                                                                                                                    |
| `workspace_name`                                                                                                                                       | *str*                                                                                                                                                  | :heavy_check_mark:                                                                                                                                     | Type the name of the workspace.                                                                                                                        |


### Response

**[operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostResponse](../../models/operations/createtagapiv1workspacesworkspacenametagspostresponse.md)**


## delete

Removes an evaluation run from deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.delete(eval_run_name='program', workspace_name='Designer')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `eval_run_name`                                                 | *str*                                                           | :heavy_check_mark:                                              | Which evaluation run do you want to delete? Type its name here. |
| `workspace_name`                                                | *str*                                                           | :heavy_check_mark:                                              | Type the name of the workspace.                                 |


### Response

**[operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteResponse](../../models/operations/deleteevalrunapiv1workspacesworkspacenameevalrunsevalrunnamedeleteresponse.md)**


## delete_tag

Removes a tag from the workspace. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.delete_tag(tag_name='deposit', workspace_name='Gasoline')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `tag_name`                                           | *str*                                                | :heavy_check_mark:                                   | Which tag do you want to delete? Type its name here. |
| `workspace_name`                                     | *str*                                                | :heavy_check_mark:                                   | Type the name of the workspace.                      |


### Response

**[operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteResponse](../../models/operations/deletetagapiv1workspacesworkspacenametagstagnamedeleteresponse.md)**


## get

Returns the evaluation run you indicate.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.get(eval_run_name='female', workspace_name='program')

if res.single_eval_run_response is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `eval_run_name`                                                  | *str*                                                            | :heavy_check_mark:                                               | Which evaluation run do you want to display? Type its name here. |
| `workspace_name`                                                 | *str*                                                            | :heavy_check_mark:                                               | Type the name of the workspace.                                  |


### Response

**[operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetResponse](../../models/operations/getevalrunapiv1workspacesworkspacenameevalrunsevalrunnamegetresponse.md)**


## get_node_eval_predictions

Returns the predicted answers for the pipeline nodes as a JSON or a CSV file

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetRequest(
    eval_run_name='Southeast Technician Chips',
    node_name='partially unnecessarily',
    workspace_name='Chromium',
)

res = s.eval_run.get_node_eval_predictions(req)

if res.response_200_get_node_eval_predictions_api_v1_workspaces_workspace_name_eval_runs_eval_run_name_nodes_node_name_predictions_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                                                | [operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetRequest](../../models/operations/getnodeevalpredictionsapiv1workspacesworkspacenameevalrunsevalrunnamenodesnodenamepredictionsgetrequest.md) | :heavy_check_mark:                                                                                                                                                                                                                                       | The request object to use for the request.                                                                                                                                                                                                               |


### Response

**[operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetResponse](../../models/operations/getnodeevalpredictionsapiv1workspacesworkspacenameevalrunsevalrunnamenodesnodenamepredictionsgetresponse.md)**


## list

Returns all the evaluation runs created in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListEvalRunsRequest(
    workspace_name='Northeast Metal Canada',
)

res = s.eval_run.list(req)

if res.eval_runs_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListEvalRunsRequest](../../models/operations/listevalrunsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListEvalRunsResponse](../../models/operations/listevalrunsresponse.md)**


## list_tags

Lists all the tags in the workspace you choose. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.list_tags(workspace_name='Recycled', filter='deposit')

if res.get_tags is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `workspace_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type the name of the workspace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `filter`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The OData filter you want to use to in your query. It supports exact match and `AND` operations. For example, to filter for a metadata `category:news`, here's what the URL could look like: 'url = "https://api.cloud.deepset.ai/api/v1/workspaces/production/files?limit=10&filter=category eq 'news'"'. OData filters only work with cursor-based pagination (leave the `page_number` field blank to enable it).To learn more about the OData filter syntax, see: [Querying Data](https://www.odata.org/getting-started/basic-tutorial/#queryData). |


### Response

**[operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetResponse](../../models/operations/gettagsapiv1workspacesworkspacenametagsgetresponse.md)**


## start

Starts a draft evaluation run.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.start(eval_run_name='Turkmenistan', workspace_name='Boron')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `eval_run_name`                                                | *str*                                                          | :heavy_check_mark:                                             | Which evaluation run do you want to start? Type its name here. |
| `workspace_name`                                               | *str*                                                          | :heavy_check_mark:                                             | Type the name of the workspace.                                |


### Response

**[operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostResponse](../../models/operations/startevalrunapiv1workspacesworkspacenameevalrunsevalrunnamestartpostresponse.md)**


## update

Updates these properties of an evaluation run: name, tags, pipeline, file corpus, and evaluation set.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.update(eval_run_patch=shared.EvalRunPatch(
    tags=[
        'Van',
    ],
), eval_run_name='East', workspace_name='male')

if res.eval_run_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `eval_run_patch`                                                | [shared.EvalRunPatch](../../models/shared/evalrunpatch.md)      | :heavy_check_mark:                                              | N/A                                                             |
| `eval_run_name`                                                 | *str*                                                           | :heavy_check_mark:                                              | Which evaluation run do you want to update? Type its name here. |
| `workspace_name`                                                | *str*                                                           | :heavy_check_mark:                                              | Type the name of the workspace.                                 |


### Response

**[operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchResponse](../../models/operations/editevalrunapiv1workspacesworkspacenameevalrunsevalrunnamepatchresponse.md)**


## update_tag

Changes the name of the tag you choose. Type the new tag name in the `name` field of the BODY PARAMS section. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.eval_run.update_tag(request_body=operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchUpdateTag(
    name='TCP lumen',
), tag_name='meter', workspace_name='solution')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                                         | [operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchUpdateTag](../../models/operations/updatetagapiv1workspacesworkspacenametagstagnamepatchupdatetag.md) | :heavy_check_mark:                                                                                                                                                     | N/A                                                                                                                                                                    |
| `tag_name`                                                                                                                                                             | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Which tag do you want to update? Type its name here.                                                                                                                   |
| `workspace_name`                                                                                                                                                       | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Type the name of the workspace.                                                                                                                                        |


### Response

**[operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchResponse](../../models/operations/updatetagapiv1workspacesworkspacenametagstagnamepatchresponse.md)**

