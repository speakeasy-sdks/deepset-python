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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.create_eval_run(eval_run_post=shared.EvalRunPost(
    comment='perferendis',
    debug=False,
    evaluation_set_name='nihil',
    name='Verna Olson',
    pipeline_name='suscipit',
    tags=[
        'natus',
    ],
), workspace_name='nobis')

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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.create_tag(request_body=operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostCreateTag(
    name='Mrs. Meghan Collins V',
), workspace_name='ullam')

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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.delete(eval_run_name='provident', workspace_name='quos')

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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.delete_tag(tag_name='sint', workspace_name='accusantium')

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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.get(eval_run_name='mollitia', workspace_name='reiciendis')

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
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetRequest(
    after='a563e251-6fe4-4c8b-b11e-5b7fd2ed0289',
    before='21cddc69-2601-4fb5-b6b0-d5f0d30c5fbb',
    eval_run_name='dolores',
    field=operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetFieldField.RANK,
    filter='totam',
    limit=489549,
    node_name='eaque',
    order=operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetOrderOrder.ASC,
    page_number=199996,
    select='eos',
    workspace_name='perferendis',
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
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.ListEvalRunsRequest(
    after='2c73d5fe-9b90-4c28-909b-3fe49a8d9cbf',
    before='48633323-f9b7-47f3-a410-0674ebf69280',
    field=operations.Field.INTEGRATED_RECALL_MULTI_HIT,
    filter='ab',
    limit=743835,
    order=operations.Order.DESC,
    page_number=478596,
    select='voluptate',
    workspace_name='dolorum',
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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.list_tags(workspace_name='deleniti', filter='omnis')

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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.start(eval_run_name='necessitatibus', workspace_name='distinctio')

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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.update(eval_run_patch=shared.EvalRunPatch(
    comment='asperiores',
    evaluation_set_name='nihil',
    pipeline_name='ipsum',
    tags=[
        'voluptate',
    ],
), eval_run_name='id', workspace_name='saepe')

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
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.eval_run.update_tag(request_body=operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchUpdateTag(
    name='Judy Aufderhar',
), tag_name='accusamus', workspace_name='ad')

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

