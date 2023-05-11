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
        result_id='0ab3c20c-4f37-489f-9871-f99dd2efd121',
        tags=[
            'culpa',
            'aliquid',
            'tenetur',
        ],
    ),
    pipeline_name='quae',
    workspace_name='earum',
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
    workspace_name='vel',
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
    pipeline_name='in',
    workspace_name='eius',
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
    pipeline_name='libero',
    workspace_name='illum',
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
    pipeline_name='soluta',
    workspace_name='accusantium',
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
    accept='aliquam',
    after='f1575608-2d68-4ea1-9f1d-17051339d080',
    before='86a18403-94c2-4607-9f93-f5f0642dac7a',
    field=operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetFieldFieldEnum.SEARCH_RESULT_SEARCH_QUERY,
    filter='nemo',
    limit=65304,
    order=operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetOrderOrderEnum.ASC,
    page_number=783235,
    pipeline_name='quod',
    select='labore',
    workspace_name='ab',
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
    pipeline_name='adipisci',
    status=operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetStatusFileIndexingStatusQueryEnum.INDEXED_NO_DOCUMENTS,
    workspace_name='id',
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
    pipeline_name='suscipit',
    workspace_name='velit',
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
    pipeline_name='culpa',
    workspace_name='est',
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
    pipeline_name='recusandae',
    workspace_name='totam',
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
    after=853940,
    field_name='vel',
    limit=497678,
    pipeline_name='quos',
    query='vel',
    workspace_name='labore',
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
    meta_field='possimus',
    pipeline_name='facilis',
    workspace_name='cum',
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
    pipeline_name='commodi',
    workspace_name='in',
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
    pipeline_name='corporis',
    workspace_name='reiciendis',
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
    after='d5e60b37-5ed4-4f6f-bee4-1f33317fe35b',
    before='60eb1ea4-2655-45ba-bc28-744ed53b88f3',
    deleted=False,
    desired_status='culpa',
    limit=548519,
    page_number=867290,
    pipeline_name='totam',
    status='hic',
    workspace_name='exercitationem',
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
            "sit": 'rerum',
            "sed": 'reiciendis',
            "explicabo": 'asperiores',
            "facilis": 'voluptate',
        },
        params={
            "ab": 'iste',
            "dolore": 'laborum',
            "sed": 'in',
        },
        queries=[
            'quidem',
            'explicabo',
        ],
    ),
    pipeline_name='voluptas',
    workspace_name='unde',
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
    after='16fe1f08-f429-44e3-a98f-447f603e8b44',
    before='5e80ca55-efd2-40e4-97e1-858b6a89fbe3',
    limit=677115,
    page_number=341698,
    pipeline_name='officia',
    workspace_name='dolorum',
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
    pipeline_name='corrupti',
    workspace_name='accusamus',
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
    pipeline_name='tempora',
    workspace_name='atque',
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
    pipeline_name='fugit',
    workspace_name='ut',
)

res = s.pipeline.update_yaml(req, operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.pipeline_name is not None:
    # handle response
```
