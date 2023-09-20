# EvalRun

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

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.create_eval_run(operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostSecurity(
    http_bearer="",
), eval_run_post=shared.EvalRunPost(
    comment='quibusdam',
    debug=False,
    evaluation_set_name='explicabo',
    name='Rudy Spencer',
    pipeline_name='qui',
    tags=[
        'aliquid',
    ],
), workspace_name='cupiditate')

if res.eval_run_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                           | [operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostSecurity](../../models/operations/createevalrunapiv1workspacesworkspacenameevalrunspostsecurity.md) | :heavy_check_mark:                                                                                                                                                   | The security requirements to use for the request.                                                                                                                    |
| `eval_run_post`                                                                                                                                                      | [shared.EvalRunPost](../../models/shared/evalrunpost.md)                                                                                                             | :heavy_check_mark:                                                                                                                                                   | N/A                                                                                                                                                                  |
| `workspace_name`                                                                                                                                                     | *str*                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                   | Type the name of the workspace.                                                                                                                                      |


### Response

**[operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostResponse](../../models/operations/createevalrunapiv1workspacesworkspacenameevalrunspostresponse.md)**


## create_tag

Creates a tag for your evaluation run. Tags can help you order and find your evaluation runs later. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.create_tag(operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostSecurity(
    http_bearer="",
), request_body=operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostCreateTag(
    name='Christopher Cummerata',
), workspace_name='alias')

if res.create_tag_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                             | [operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostSecurity](../../models/operations/createtagapiv1workspacesworkspacenametagspostsecurity.md)   | :heavy_check_mark:                                                                                                                                     | The security requirements to use for the request.                                                                                                      |
| `request_body`                                                                                                                                         | [operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostCreateTag](../../models/operations/createtagapiv1workspacesworkspacenametagspostcreatetag.md) | :heavy_check_mark:                                                                                                                                     | N/A                                                                                                                                                    |
| `workspace_name`                                                                                                                                       | *str*                                                                                                                                                  | :heavy_check_mark:                                                                                                                                     | Type the name of the workspace.                                                                                                                        |


### Response

**[operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostResponse](../../models/operations/createtagapiv1workspacesworkspacenametagspostresponse.md)**


## delete

Removes an evaluation run from deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.delete(operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteSecurity(
    http_bearer="",
), eval_run_name='fugit', workspace_name='dolorum')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                      | Type                                                                                                                                                                                           | Required                                                                                                                                                                                       | Description                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                     | [operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteSecurity](../../models/operations/deleteevalrunapiv1workspacesworkspacenameevalrunsevalrunnamedeletesecurity.md) | :heavy_check_mark:                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                              |
| `eval_run_name`                                                                                                                                                                                | *str*                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                             | Which evaluation run do you want to delete? Type its name here.                                                                                                                                |
| `workspace_name`                                                                                                                                                                               | *str*                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                             | Type the name of the workspace.                                                                                                                                                                |


### Response

**[operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteResponse](../../models/operations/deleteevalrunapiv1workspacesworkspacenameevalrunsevalrunnamedeleteresponse.md)**


## delete_tag

Removes a tag from the workspace. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.delete_tag(operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteSecurity(
    http_bearer="",
), tag_name='excepturi', workspace_name='tempora')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                             | [operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteSecurity](../../models/operations/deletetagapiv1workspacesworkspacenametagstagnamedeletesecurity.md) | :heavy_check_mark:                                                                                                                                                     | The security requirements to use for the request.                                                                                                                      |
| `tag_name`                                                                                                                                                             | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Which tag do you want to delete? Type its name here.                                                                                                                   |
| `workspace_name`                                                                                                                                                       | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Type the name of the workspace.                                                                                                                                        |


### Response

**[operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteResponse](../../models/operations/deletetagapiv1workspacesworkspacenametagstagnamedeleteresponse.md)**


## get

Returns the evaluation run you indicate.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.get(operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetSecurity(
    http_bearer="",
), eval_run_name='facilis', workspace_name='tempore')

if res.single_eval_run_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                         | [operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetSecurity](../../models/operations/getevalrunapiv1workspacesworkspacenameevalrunsevalrunnamegetsecurity.md) | :heavy_check_mark:                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                  |
| `eval_run_name`                                                                                                                                                                    | *str*                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                 | Which evaluation run do you want to display? Type its name here.                                                                                                                   |
| `workspace_name`                                                                                                                                                                   | *str*                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                 | Type the name of the workspace.                                                                                                                                                    |


### Response

**[operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetResponse](../../models/operations/getevalrunapiv1workspacesworkspacenameevalrunsevalrunnamegetresponse.md)**


## get_node_eval_predictions

Returns the predicted answers for the pipeline nodes as a JSON or a CSV file

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetRequest(
    after='4f63c969-e9a3-4efa-b7df-b14cd66ae395',
    before='efb9ba88-f3a6-4699-b074-ba4469b6e214',
    eval_run_name='et',
    field=operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetFieldField.F1_CONTEXT_SCOPE,
    filter='ullam',
    limit=590873,
    node_name='quos',
    order=operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetOrderOrder.DESC,
    page_number=33625,
    select='mollitia',
    workspace_name='reiciendis',
)

res = s.eval_run.get_node_eval_predictions(req, operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetSecurity(
    http_bearer="",
))

if res.response_200_get_node_eval_predictions_api_v1_workspaces_workspace_name_eval_runs_eval_run_name_nodes_node_name_predictions_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                                                  | [operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetRequest](../../models/operations/getnodeevalpredictionsapiv1workspacesworkspacenameevalrunsevalrunnamenodesnodenamepredictionsgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                                                                 |
| `security`                                                                                                                                                                                                                                                 | [operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetSecurity](../../models/operations/getnodeevalpredictionsapiv1workspacesworkspacenameevalrunsevalrunnamenodesnodenamepredictionsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                                         | The security requirements to use for the request.                                                                                                                                                                                                          |


### Response

**[operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetResponse](../../models/operations/getnodeevalpredictionsapiv1workspacesworkspacenameevalrunsevalrunnamenodesnodenamepredictionsgetresponse.md)**


## list

Returns all the evaluation runs created in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListEvalRunsRequest(
    after='a563e251-6fe4-4c8b-b11e-5b7fd2ed0289',
    before='21cddc69-2601-4fb5-b6b0-d5f0d30c5fbb',
    field=operations.Field.CREATED_BY,
    filter='quis',
    limit=521037,
    order=operations.Order.ASC,
    page_number=54338,
    select='quis',
    workspace_name='nesciunt',
)

res = s.eval_run.list(req, operations.ListEvalRunsSecurity(
    http_bearer="",
))

if res.eval_runs_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListEvalRunsRequest](../../models/operations/listevalrunsrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.ListEvalRunsSecurity](../../models/operations/listevalrunssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.ListEvalRunsResponse](../../models/operations/listevalrunsresponse.md)**


## list_tags

Lists all the tags in the workspace you choose. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.list_tags(operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetSecurity(
    http_bearer="",
), workspace_name='eos', filter='perferendis')

if res.get_tags is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetSecurity](../../models/operations/gettagsapiv1workspacesworkspacenametagsgetsecurity.md)                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `workspace_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type the name of the workspace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `filter`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The OData filter you want to use to in your query. It supports exact match and `AND` operations. For example, to filter for a metadata `category:news`, here's what the URL could look like: 'url = "https://api.cloud.deepset.ai/api/v1/workspaces/production/files?limit=10&filter=category eq 'news'"'. OData filters only work with cursor-based pagination (leave the `page_number` field blank to enable it).To learn more about the OData filter syntax, see: [Querying Data](https://www.odata.org/getting-started/basic-tutorial/#queryData). |


### Response

**[operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetResponse](../../models/operations/gettagsapiv1workspacesworkspacenametagsgetresponse.md)**


## start

Starts a draft evaluation run.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.start(operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostSecurity(
    http_bearer="",
), eval_run_name='dolores', workspace_name='minus')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                         | [operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostSecurity](../../models/operations/startevalrunapiv1workspacesworkspacenameevalrunsevalrunnamestartpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                                  |
| `eval_run_name`                                                                                                                                                                                    | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | Which evaluation run do you want to start? Type its name here.                                                                                                                                     |
| `workspace_name`                                                                                                                                                                                   | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | Type the name of the workspace.                                                                                                                                                                    |


### Response

**[operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostResponse](../../models/operations/startevalrunapiv1workspacesworkspacenameevalrunsevalrunnamestartpostresponse.md)**


## update

Updates these properties of an evaluation run: name, tags, pipeline, file corpus, and evaluation set.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.update(operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchSecurity(
    http_bearer="",
), eval_run_patch=shared.EvalRunPatch(
    comment='quam',
    evaluation_set_name='dolor',
    pipeline_name='vero',
    tags=[
        'nostrum',
    ],
), eval_run_name='hic', workspace_name='recusandae')

if res.eval_run_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                               | [operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchSecurity](../../models/operations/editevalrunapiv1workspacesworkspacenameevalrunsevalrunnamepatchsecurity.md) | :heavy_check_mark:                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                        |
| `eval_run_patch`                                                                                                                                                                         | [shared.EvalRunPatch](../../models/shared/evalrunpatch.md)                                                                                                                               | :heavy_check_mark:                                                                                                                                                                       | N/A                                                                                                                                                                                      |
| `eval_run_name`                                                                                                                                                                          | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | Which evaluation run do you want to update? Type its name here.                                                                                                                          |
| `workspace_name`                                                                                                                                                                         | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | Type the name of the workspace.                                                                                                                                                          |


### Response

**[operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchResponse](../../models/operations/editevalrunapiv1workspacesworkspacenameevalrunsevalrunnamepatchresponse.md)**


## update_tag

Changes the name of the tag you choose. Type the new tag name in the `name` field of the BODY PARAMS section. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.eval_run.update_tag(operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchSecurity(
    http_bearer="",
), request_body=operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchUpdateTag(
    name='Miss Cesar Metz',
), tag_name='blanditiis', workspace_name='error')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                             | [operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchSecurity](../../models/operations/updatetagapiv1workspacesworkspacenametagstagnamepatchsecurity.md)   | :heavy_check_mark:                                                                                                                                                     | The security requirements to use for the request.                                                                                                                      |
| `request_body`                                                                                                                                                         | [operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchUpdateTag](../../models/operations/updatetagapiv1workspacesworkspacenametagstagnamepatchupdatetag.md) | :heavy_check_mark:                                                                                                                                                     | N/A                                                                                                                                                                    |
| `tag_name`                                                                                                                                                             | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Which tag do you want to update? Type its name here.                                                                                                                   |
| `workspace_name`                                                                                                                                                       | *str*                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                     | Type the name of the workspace.                                                                                                                                        |


### Response

**[operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchResponse](../../models/operations/updatetagapiv1workspacesworkspacenametagstagnamepatchresponse.md)**

