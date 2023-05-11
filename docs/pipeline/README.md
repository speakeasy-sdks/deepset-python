# pipeline

### Available Operations

* [add_feedback](#add_feedback) - Add Feedback
* [create](#create) - Create Pipeline
* [delete](#delete) - Delete Pipeline
* [deploy](#deploy) - Deploy Pipeline
* [get](#get) - Get Pipeline
* [get_feedback](#get_feedback) - Get Pipeline Feedback
* [get_files](#get_files) - Get Pipeline Files
* [get_indexing](#get_indexing) - Get Pipeline Indexing
* [get_json](#get_json) - Get Pipeline Yaml As Json
* [get_metadata](#get_metadata) - Get Pipeline Index Metadata [private]
* [get_metadata_field_values](#get_metadata_field_values) - Get Pipeline Metadata Field Values [private]
* [get_min_max_aggregation_metadata](#get_min_max_aggregation_metadata) - Get Pipeline Min Max Aggregation Metadata [private]
* [get_stats](#get_stats) - Get Pipeline Stats
* [get_yaml](#get_yaml) - Get Pipeline Yaml
* [list](#list) - List Pipelines
* [search](#search) - Search
* [search_history](#search_history) - Pipeline Search History [private]
* [set_default](#set_default) - Set Default Pipeline
* [undeploy](#undeploy) - Undeploy Pipeline
* [update_yaml](#update_yaml) - Update Pipeline Yaml

## add_feedback

Adds feedback to search results.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.AddFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackPostRequest(
    post_pipeline_feedback=shared.PostPipelineFeedback(
        is_correct_answer=False,
        is_correct_document=False,
        result_id='3c7e0bc7-178e-4479-af2a-70c688282aa4',
        tags=[
            'explicabo',
            'minima',
            'nisi',
        ],
    ),
    pipeline_name='fugit',
    workspace_name='sapiente',
)

res = s.pipeline.add_feedback(req, operations.AddFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.add_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_post_200_application_json_any is not None:
    # handle response
```

## create

Creates a pipeline YAML file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.CreatePipelineAPIV1WorkspacesWorkspaceNamePipelinesPostRequest(
    dry_run=False,
    workspace_name='consequuntur',
)

res = s.pipeline.create(req, operations.CreatePipelineAPIV1WorkspacesWorkspaceNamePipelinesPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_name is not None:
    # handle response
```

## delete

Deletes a pipeline from deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeletePipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeleteRequest(
    pipeline_name='ratione',
    workspace_name='explicabo',
)

res = s.pipeline.delete(req, operations.DeletePipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.delete_pipeline_api_v1_workspaces_workspace_name_pipelines_pipeline_name_delete_200_application_json_any is not None:
    # handle response
```

## deploy

Deploys a pipeline in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeployPostRequest(
    pipeline_name='saepe',
    workspace_name='occaecati',
)

res = s.pipeline.deploy(req, operations.DeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeployPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_indexing is not None:
    # handle response
```

## get

Returns a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameGetRequest(
    pipeline_name='atque',
    workspace_name='et',
)

res = s.pipeline.get(req, operations.GetPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_indexing is not None:
    # handle response
```

## get_feedback

Returns the feedback in JSON or CSV format.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetRequest(
    accept='esse',
    after='ee17cbe6-1e6b-47b9-9bc0-ab3c20c4f378',
    before='9fd871f9-9dd2-4efd-921a-a6f1e674bdb0',
    field=operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetFieldFieldEnum.SEARCH_RESULT_RANK,
    filter='sapiente',
    limit=119771,
    order=operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetOrderOrderEnum.ASC,
    page_number=443879,
    pipeline_name='ullam',
    select='nisi',
    workspace_name='aut',
)

res = s.pipeline.get_feedback(req, operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.response_200_get_pipeline_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_get is not None:
    # handle response
```

## get_files

Returns IDs of all files with a specific status.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetRequest(
    pipeline_name='voluptatum',
    status=operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetStatusFileIndexingStatusQueryEnum.FAILED,
    workspace_name='quibusdam',
)

res = s.pipeline.get_files(req, operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.get_pipeline_files_api_v1_workspaces_workspace_name_pipelines_pipeline_name_files_get_200_application_json_uuid_strings is not None:
    # handle response
```

## get_indexing

Returns the indexing information for a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineIndexingAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameIndexingGetRequest(
    pipeline_name='ex',
    workspace_name='deleniti',
)

res = s.pipeline.get_indexing(req, operations.GetPipelineIndexingAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameIndexingGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_indexing_status_detail is not None:
    # handle response
```

## get_json

Returns the pipeline in the JSON format.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetRequest(
    pipeline_name='itaque',
    workspace_name='dolorum',
)

res = s.pipeline.get_json(req, operations.GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.response_get_pipeline_yaml_as_json_api_v1_workspaces_workspace_name_pipelines_pipeline_name_json_get is not None:
    # handle response
```

## get_metadata

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineIndexMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaGetRequest(
    pipeline_name='architecto',
    workspace_name='omnis',
)

res = s.pipeline.get_metadata(req, operations.GetPipelineIndexMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.response_200_get_pipeline_index_metadata_api_v1_workspaces_workspace_name_pipelines_pipeline_name_meta_get is not None:
    # handle response
```

## get_metadata_field_values

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetRequest(
    after=945302,
    field_name='quasi',
    limit=869489,
    pipeline_name='et',
    query='voluptate',
    workspace_name='ipsa',
)

res = s.pipeline.get_metadata_field_values(req, operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_field_search_result is not None:
    # handle response
```

## get_min_max_aggregation_metadata

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineMinMaxAggregationMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaMetaFieldAggregationGetRequest(
    meta_field='minima',
    pipeline_name='veritatis',
    workspace_name='consectetur',
)

res = s.pipeline.get_min_max_aggregation_metadata(req, operations.GetPipelineMinMaxAggregationMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaMetaFieldAggregationGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_metadata_aggregation is not None:
    # handle response
```

## get_stats

Returns a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetRequest(
    pipeline_name='adipisci',
    workspace_name='iste',
)

res = s.pipeline.get_stats(req, operations.GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_statistics is not None:
    # handle response
```

## get_yaml

Displays the pipeline as a YAML.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlGetRequest(
    pipeline_name='temporibus',
    workspace_name='accusantium',
)

res = s.pipeline.get_yaml(req, operations.GetPipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_yaml is not None:
    # handle response
```

## list

Lists all the pipelines in the workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetRequest(
    after='8086a184-0394-4c26-871f-93f5f0642dac',
    before='7af515cc-413a-4a63-aae8-d67864dbb675',
    deleted=False,
    desired_status='reiciendis',
    limit=828657,
    page_number=363161,
    pipeline_name='recusandae',
    status='aliquid',
    workspace_name='aperiam',
)

res = s.pipeline.list(req, operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_pagination is not None:
    # handle response
```

## search

Run a search using a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.SearchAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchPostRequest(
    pipeline_query=shared.PipelineQuery(
        debug=False,
        filters={
            "consectetur": 'in',
            "exercitationem": 'earum',
            "facere": 'numquam',
        },
        params={
            "suscipit": 'reiciendis',
            "quidem": 'saepe',
            "necessitatibus": 'dolore',
            "sunt": 'asperiores',
        },
        queries=[
            'non',
        ],
    ),
    pipeline_name='amet',
    workspace_name='beatae',
)

res = s.pipeline.search(req, operations.SearchAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.search_result is not None:
    # handle response
```

## search_history

Returns the search history which includes information such as the query, the answer, the pipeline used, and more. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetRequest(
    after='7fe35b60-eb1e-4a42-a555-ba3c28744ed5',
    before='3b88f3a8-d8f5-4c0b-af2f-b7b194a276b2',
    limit=378326,
    page_number=604118,
    pipeline_name='architecto',
    workspace_name='suscipit',
)

res = s.pipeline.search_history(req, operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.search_history_pagination is not None:
    # handle response
```

## set_default

Sets a pipeline as the default pipeline for search.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.SetDefaultPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDefaultPostRequest(
    pipeline_name='sapiente',
    workspace_name='debitis',
)

res = s.pipeline.set_default(req, operations.SetDefaultPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDefaultPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.set_default_pipeline_api_v1_workspaces_workspace_name_pipelines_pipeline_name_default_post_200_application_json_any is not None:
    # handle response
```

## undeploy

Undeploys a pipeline in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.UndeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameUndeployPostRequest(
    pipeline_name='illo',
    workspace_name='reiciendis',
)

res = s.pipeline.undeploy(req, operations.UndeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameUndeployPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_indexing is not None:
    # handle response
```

## update_yaml

Updates the pipeline YAML file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutRequest(
    pipeline_name='perferendis',
    workspace_name='corrupti',
)

res = s.pipeline.update_yaml(req, operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_name is not None:
    # handle response
```
