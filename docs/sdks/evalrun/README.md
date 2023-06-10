# eval_run

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

req = operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostRequest(
    eval_run_post=shared.EvalRunPost(
        comment='deserunt',
        debug=False,
        evaluation_set_name='distinctio',
        name='Francisco Gleason',
        pipeline_name='cupiditate',
        tags=[
            'perferendis',
            'magni',
            'assumenda',
        ],
    ),
    workspace_name='ipsam',
)

res = s.eval_run.create_eval_run(req, operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostSecurity(
    http_bearer="",
))

if res.eval_run_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostRequest](../../models/operations/createevalrunapiv1workspacesworkspacenameevalrunspostrequest.md)   | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |
| `security`                                                                                                                                                           | [operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostSecurity](../../models/operations/createevalrunapiv1workspacesworkspacenameevalrunspostsecurity.md) | :heavy_check_mark:                                                                                                                                                   | The security requirements to use for the request.                                                                                                                    |


### Response

**[operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostResponse](../../models/operations/createevalrunapiv1workspacesworkspacenameevalrunspostresponse.md)**


## create_tag

Creates a tag for your evaluation run. Tags can help you order and find your evaluation runs later. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostRequest(
    request_body=operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostCreateTag(
        name='Denise Pagac',
    ),
    workspace_name='facilis',
)

res = s.eval_run.create_tag(req, operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostSecurity(
    http_bearer="",
))

if res.create_tag_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostRequest](../../models/operations/createtagapiv1workspacesworkspacenametagspostrequest.md)   | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `security`                                                                                                                                           | [operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostSecurity](../../models/operations/createtagapiv1workspacesworkspacenametagspostsecurity.md) | :heavy_check_mark:                                                                                                                                   | The security requirements to use for the request.                                                                                                    |


### Response

**[operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostResponse](../../models/operations/createtagapiv1workspacesworkspacenametagspostresponse.md)**


## delete

Removes an evaluation run from deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteRequest(
    eval_run_name='tempore',
    workspace_name='labore',
)

res = s.eval_run.delete(req, operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteSecurity(
    http_bearer="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                      | Type                                                                                                                                                                                           | Required                                                                                                                                                                                       | Description                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                      | [operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteRequest](../../models/operations/deleteevalrunapiv1workspacesworkspacenameevalrunsevalrunnamedeleterequest.md)   | :heavy_check_mark:                                                                                                                                                                             | The request object to use for the request.                                                                                                                                                     |
| `security`                                                                                                                                                                                     | [operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteSecurity](../../models/operations/deleteevalrunapiv1workspacesworkspacenameevalrunsevalrunnamedeletesecurity.md) | :heavy_check_mark:                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                              |


### Response

**[operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteResponse](../../models/operations/deleteevalrunapiv1workspacesworkspacenameevalrunsevalrunnamedeleteresponse.md)**


## delete_tag

Removes a tag from the workspace. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteRequest(
    tag_name='delectus',
    workspace_name='eum',
)

res = s.eval_run.delete_tag(req, operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteSecurity(
    http_bearer="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteRequest](../../models/operations/deletetagapiv1workspacesworkspacenametagstagnamedeleterequest.md)   | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |
| `security`                                                                                                                                                             | [operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteSecurity](../../models/operations/deletetagapiv1workspacesworkspacenametagstagnamedeletesecurity.md) | :heavy_check_mark:                                                                                                                                                     | The security requirements to use for the request.                                                                                                                      |


### Response

**[operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteResponse](../../models/operations/deletetagapiv1workspacesworkspacenametagstagnamedeleteresponse.md)**


## get

Returns the evaluation run you indicate.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetRequest(
    eval_run_name='non',
    workspace_name='eligendi',
)

res = s.eval_run.get(req, operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetSecurity(
    http_bearer="",
))

if res.single_eval_run_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                          | [operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetRequest](../../models/operations/getevalrunapiv1workspacesworkspacenameevalrunsevalrunnamegetrequest.md)   | :heavy_check_mark:                                                                                                                                                                 | The request object to use for the request.                                                                                                                                         |
| `security`                                                                                                                                                                         | [operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetSecurity](../../models/operations/getevalrunapiv1workspacesworkspacenameevalrunsevalrunnamegetsecurity.md) | :heavy_check_mark:                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                  |


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
    after='969e9a3e-fa77-4dfb-94cd-66ae395efb9b',
    before='a88f3a66-9970-474b-a446-9b6e21419598',
    eval_run_name='sint',
    field=operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetFieldField.QUERY,
    filter='mollitia',
    limit=968962,
    node_name='mollitia',
    order=operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetOrderOrder.ASC,
    page_number=431418,
    select='dolor',
    workspace_name='necessitatibus',
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
    after='2516fe4c-8b71-41e5-b7fd-2ed028921cdd',
    before='c692601f-b576-4b0d-9f0d-30c5fbb25870',
    field=operations.Field.INTEGRATED_EXACT_MATCH,
    filter='nesciunt',
    limit=179490,
    order=operations.Order.ASC,
    page_number=170986,
    select='minus',
    workspace_name='quam',
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

req = operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetRequest(
    filter='dolor',
    workspace_name='vero',
)

res = s.eval_run.list_tags(req, operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetSecurity(
    http_bearer="",
))

if res.get_tags is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetRequest](../../models/operations/gettagsapiv1workspacesworkspacenametagsgetrequest.md)   | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |
| `security`                                                                                                                                     | [operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetSecurity](../../models/operations/gettagsapiv1workspacesworkspacenametagsgetsecurity.md) | :heavy_check_mark:                                                                                                                             | The security requirements to use for the request.                                                                                              |


### Response

**[operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetResponse](../../models/operations/gettagsapiv1workspacesworkspacenametagsgetresponse.md)**


## start

Starts a draft evaluation run.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostRequest(
    eval_run_name='nostrum',
    workspace_name='hic',
)

res = s.eval_run.start(req, operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostSecurity(
    http_bearer="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                          | [operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostRequest](../../models/operations/startevalrunapiv1workspacesworkspacenameevalrunsevalrunnamestartpostrequest.md)   | :heavy_check_mark:                                                                                                                                                                                 | The request object to use for the request.                                                                                                                                                         |
| `security`                                                                                                                                                                                         | [operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostSecurity](../../models/operations/startevalrunapiv1workspacesworkspacenameevalrunsevalrunnamestartpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                                  |


### Response

**[operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostResponse](../../models/operations/startevalrunapiv1workspacesworkspacenameevalrunsevalrunnamestartpostresponse.md)**


## update

Updates these properties of an evaluation run: name, tags, pipeline, file corpus, and evaluation set.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchRequest(
    eval_run_patch=shared.EvalRunPatch(
        comment='recusandae',
        evaluation_set_name='omnis',
        pipeline_name='facilis',
        tags=[
            'voluptatem',
            'porro',
            'consequuntur',
        ],
    ),
    eval_run_name='blanditiis',
    workspace_name='error',
)

res = s.eval_run.update(req, operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchSecurity(
    http_bearer="",
))

if res.eval_run_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                | [operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchRequest](../../models/operations/editevalrunapiv1workspacesworkspacenameevalrunsevalrunnamepatchrequest.md)   | :heavy_check_mark:                                                                                                                                                                       | The request object to use for the request.                                                                                                                                               |
| `security`                                                                                                                                                                               | [operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchSecurity](../../models/operations/editevalrunapiv1workspacesworkspacenameevalrunsevalrunnamepatchsecurity.md) | :heavy_check_mark:                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                        |


### Response

**[operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchResponse](../../models/operations/editevalrunapiv1workspacesworkspacenameevalrunsevalrunnamepatchresponse.md)**


## update_tag

Changes the name of the tag you choose. Type the new tag name in the `name` field of the BODY PARAMS section. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchRequest(
    request_body=operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchUpdateTag(
        name='Violet Price',
    ),
    tag_name='earum',
    workspace_name='modi',
)

res = s.eval_run.update_tag(req, operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchSecurity(
    http_bearer="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchRequest](../../models/operations/updatetagapiv1workspacesworkspacenametagstagnamepatchrequest.md)   | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |
| `security`                                                                                                                                                           | [operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchSecurity](../../models/operations/updatetagapiv1workspacesworkspacenametagstagnamepatchsecurity.md) | :heavy_check_mark:                                                                                                                                                   | The security requirements to use for the request.                                                                                                                    |


### Response

**[operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchResponse](../../models/operations/updatetagapiv1workspacesworkspacenametagstagnamepatchresponse.md)**

