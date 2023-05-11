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
        comment='error',
        debug=False,
        evaluation_set_name='temporibus',
        name='Ryan Witting',
        pipeline_name='nihil',
        tags=[
            'voluptatibus',
            'ipsa',
            'omnis',
        ],
    ),
    workspace_name='voluptate',
)

res = s.eval_run.create_eval_run(req, operations.CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.eval_run_create_response is not None:
    # handle response
```

## create_tag

Creates a tag for your evaluation run. Tags can help you order and find your evaluation runs later. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostRequest(
    request_body=operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostCreateTag(
        name='Thomas Batz',
    ),
    workspace_name='maiores',
)

res = s.eval_run.create_tag(req, operations.CreateTagAPIV1WorkspacesWorkspaceNameTagsPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.create_tag_response is not None:
    # handle response
```

## delete

Removes an evaluation run from deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteRequest(
    eval_run_name='dicta',
    workspace_name='corporis',
)

res = s.eval_run.delete(req, operations.DeleteEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## delete_tag

Removes a tag from the workspace. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteRequest(
    tag_name='dolore',
    workspace_name='iusto',
)

res = s.eval_run.delete_tag(req, operations.DeleteTagAPIV1WorkspacesWorkspaceNameTagsTagNameDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## get

Returns the evaluation run you indicate.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetRequest(
    eval_run_name='dicta',
    workspace_name='harum',
)

res = s.eval_run.get(req, operations.GetEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.single_eval_run_response is not None:
    # handle response
```

## get_node_eval_predictions

Returns the predicted answers for the pipeline nodes as a JSON or a CSV file

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetRequest(
    accept='enim',
    after='e6e13b99-d488-4e1e-91e4-50ad2abd4426',
    before='9802d502-a94b-4b4f-a3c9-69e9a3efa77d',
    eval_run_name='maiores',
    field=operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetFieldFieldEnum.F1_DOCUMENT_ID_SCOPE,
    filter='dicta',
    limit=297437,
    node_name='cumque',
    order=operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetOrderOrderEnum.DESC,
    page_number=411820,
    select='aliquid',
    workspace_name='laborum',
)

res = s.eval_run.get_node_eval_predictions(req, operations.GetNodeEvalPredictionsAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameNodesNodeNamePredictionsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.response_200_get_node_eval_predictions_api_v1_workspaces_workspace_name_eval_runs_eval_run_name_nodes_node_name_predictions_get is not None:
    # handle response
```

## list

Returns all the evaluation runs created in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListEvalRunsAPIV1WorkspacesWorkspaceNameEvalRunsGetRequest(
    after='e395efb9-ba88-4f3a-a699-7074ba4469b6',
    before='e2141959-890a-4fa5-a3e2-516fe4c8b711',
    field=operations.ListEvalRunsAPIV1WorkspacesWorkspaceNameEvalRunsGetFieldFieldEnum.INTEGRATED_NORMAL_DISCOUNTED_CUMULATIVE_GAIN,
    filter='ullam',
    limit=714242,
    order=operations.ListEvalRunsAPIV1WorkspacesWorkspaceNameEvalRunsGetOrderOrderEnum.ASC,
    page_number=998848,
    select='quibusdam',
    workspace_name='sed',
)

res = s.eval_run.list(req, operations.ListEvalRunsAPIV1WorkspacesWorkspaceNameEvalRunsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.eval_runs_response is not None:
    # handle response
```

## list_tags

Lists all the tags in the workspace you choose. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetRequest(
    filter='saepe',
    workspace_name='pariatur',
)

res = s.eval_run.list_tags(req, operations.GetTagsAPIV1WorkspacesWorkspaceNameTagsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.get_tags is not None:
    # handle response
```

## start

Starts a draft evaluation run.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostRequest(
    eval_run_name='accusantium',
    workspace_name='consequuntur',
)

res = s.eval_run.start(req, operations.StartEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNameStartPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## update

Updates these properties of an evaluation run: name, tags, pipeline, file corpus, and evaluation set.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchRequest(
    eval_run_patch=shared.EvalRunPatch(
        comment='praesentium',
        evaluation_set_name='natus',
        pipeline_name='magni',
        tags=[
            'quo',
        ],
    ),
    eval_run_name='illum',
    workspace_name='pariatur',
)

res = s.eval_run.update(req, operations.EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.eval_run_create_response is not None:
    # handle response
```

## update_tag

Changes the name of the tag you choose. Type the new tag name in the `name` field of the BODY PARAMS section. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchRequest(
    request_body=operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchUpdateTag(
        name='Nathaniel Marks',
    ),
    tag_name='accusantium',
    workspace_name='ab',
)

res = s.eval_run.update_tag(req, operations.UpdateTagAPIV1WorkspacesWorkspaceNameTagsTagNamePatchSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```