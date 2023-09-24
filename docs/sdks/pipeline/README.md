# Pipeline

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

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.add_feedback(post_pipeline_feedback=shared.PostPipelineFeedback(
    is_correct_answer=False,
    is_correct_document=False,
    result_id='e674bdb0-4f15-4756-882d-68ea19f1d170',
    tags=[
        'minima',
    ],
), pipeline_name='veritatis', workspace_name='consectetur')

if res.add_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_post_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `post_pipeline_feedback`                                                   | [shared.PostPipelineFeedback](../../models/shared/postpipelinefeedback.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `pipeline_name`                                                            | *str*                                                                      | :heavy_check_mark:                                                         | The name of the pipeline used for search.                                  |
| `workspace_name`                                                           | *str*                                                                      | :heavy_check_mark:                                                         | Type the name of the workspace.                                            |


### Response

**[operations.AddFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackPostResponse](../../models/operations/addfeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackpostresponse.md)**


## create

Creates a pipeline YAML file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.create(workspace_name='adipisci', dry_run=False)

if res.pipeline_name is not None:
    # handle response
```

### Parameters

| Parameter                                           | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `workspace_name`                                    | *str*                                               | :heavy_check_mark:                                  | Type the name of the workspace.                     |
| `dry_run`                                           | *Optional[bool]*                                    | :heavy_minus_sign:                                  | Validates the pipeline without actually storing it. |


### Response

**[operations.CreatePipelineAPIV1WorkspacesWorkspaceNamePipelinesPostResponse](../../models/operations/createpipelineapiv1workspacesworkspacenamepipelinespostresponse.md)**


## delete

Deletes a pipeline from deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.delete(pipeline_name='iste', workspace_name='temporibus')

if res.delete_pipeline_api_v1_workspaces_workspace_name_pipelines_pipeline_name_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `pipeline_name`                              | *str*                                        | :heavy_check_mark:                           | The name of the pipeline you want to delete. |
| `workspace_name`                             | *str*                                        | :heavy_check_mark:                           | Type the name of the workspace.              |


### Response

**[operations.DeletePipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeleteResponse](../../models/operations/deletepipelineapiv1workspacesworkspacenamepipelinespipelinenamedeleteresponse.md)**


## deploy

Deploys a pipeline in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.deploy(pipeline_name='accusantium', workspace_name='rem')

if res.pipeline_indexing is not None:
    # handle response
```

### Parameters

| Parameter                                         | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `pipeline_name`                                   | *str*                                             | :heavy_check_mark:                                | The name of the pipeline that you want to deploy. |
| `workspace_name`                                  | *str*                                             | :heavy_check_mark:                                | Type the name of the workspace.                   |


### Response

**[operations.DeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeployPostResponse](../../models/operations/deploypipelineapiv1workspacesworkspacenamepipelinespipelinenamedeploypostresponse.md)**


## get

Returns a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.get(pipeline_name='aut', workspace_name='laudantium')

if res.pipeline_indexing is not None:
    # handle response
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `pipeline_name`                             | *str*                                       | :heavy_check_mark:                          | The name of the pipeline you want to fetch. |
| `workspace_name`                            | *str*                                       | :heavy_check_mark:                          | Type the name of the workspace.             |


### Response

**[operations.GetPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameGetResponse](../../models/operations/getpipelineapiv1workspacesworkspacenamepipelinespipelinenamegetresponse.md)**


## get_feedback

Returns the feedback in JSON or CSV format.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetRequest(
    after='6a184039-4c26-4071-b93f-5f0642dac7af',
    before='515cc413-aa63-4aae-8d67-864dbb675fd5',
    field=operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetFieldField.SEARCH_RESULT_SEARCH_QUERY,
    filter='aliquid',
    limit=46007,
    order=operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetOrderOrder.DESC,
    page_number=232627,
    pipeline_name='in',
    select='exercitationem',
    workspace_name='earum',
)

res = s.pipeline.get_feedback(req)

if res.response_200_get_pipeline_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                              | Type                                                                                                                                                                                                                   | Required                                                                                                                                                                                                               | Description                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                              | [operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetRequest](../../models/operations/getpipelinefeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackgetrequest.md) | :heavy_check_mark:                                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                                             |


### Response

**[operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetResponse](../../models/operations/getpipelinefeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackgetresponse.md)**


## get_files

Returns IDs of all files with a specific status.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.get_files(pipeline_name='facere', workspace_name='numquam', status=operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetStatusFileIndexingStatusQuery.INDEXED_NO_DOCUMENTS)

if res.get_pipeline_files_api_v1_workspaces_workspace_name_pipelines_pipeline_name_files_get_200_application_json_uuid_strings is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pipeline_name`                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                               | The name of the pipeline whose files you want to display.                                                                                                                                                                                                        |
| `workspace_name`                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                               | Type the name of the workspace.                                                                                                                                                                                                                                  |
| `status`                                                                                                                                                                                                                                                         | [Optional[operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetStatusFileIndexingStatusQuery]](../../models/operations/getpipelinefilesapiv1workspacesworkspacenamepipelinespipelinenamefilesgetstatusfileindexingstatusquery.md) | :heavy_minus_sign:                                                                                                                                                                                                                                               | The status of the pipeline whose files you want to display.                                                                                                                                                                                                      |


### Response

**[operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetResponse](../../models/operations/getpipelinefilesapiv1workspacesworkspacenamepipelinespipelinenamefilesgetresponse.md)**


## get_indexing

Returns the indexing information for a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.get_indexing(pipeline_name='suscipit', workspace_name='reiciendis')

if res.pipeline_indexing_status_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `pipeline_name`                                                   | *str*                                                             | :heavy_check_mark:                                                | The name of the pipeline whose indexing status you want to fetch. |
| `workspace_name`                                                  | *str*                                                             | :heavy_check_mark:                                                | Type the name of the workspace.                                   |


### Response

**[operations.GetPipelineIndexingAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameIndexingGetResponse](../../models/operations/getpipelineindexingapiv1workspacesworkspacenamepipelinespipelinenameindexinggetresponse.md)**


## get_json

Returns the pipeline in the JSON format.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.get_json(pipeline_name='quidem', workspace_name='saepe')

if res.response_get_pipeline_yaml_as_json_api_v1_workspaces_workspace_name_pipelines_pipeline_name_json_get is not None:
    # handle response
```

### Parameters

| Parameter                                                 | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `pipeline_name`                                           | *str*                                                     | :heavy_check_mark:                                        | The name of the pipeline that you want to return as JSON. |
| `workspace_name`                                          | *str*                                                     | :heavy_check_mark:                                        | Type the name of the workspace.                           |


### Response

**[operations.GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetResponse](../../models/operations/getpipelineyamlasjsonapiv1workspacesworkspacenamepipelinespipelinenamejsongetresponse.md)**


## get_metadata

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.get_metadata(pipeline_name='necessitatibus', workspace_name='dolore')

if res.response_200_get_pipeline_index_metadata_api_v1_workspaces_workspace_name_pipelines_pipeline_name_meta_get is not None:
    # handle response
```

### Parameters

| Parameter                                                 | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `pipeline_name`                                           | *str*                                                     | :heavy_check_mark:                                        | The name of the pipeline whose files you want to display. |
| `workspace_name`                                          | *str*                                                     | :heavy_check_mark:                                        | Type the name of the workspace.                           |


### Response

**[operations.GetPipelineIndexMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaGetResponse](../../models/operations/getpipelineindexmetadataapiv1workspacesworkspacenamepipelinespipelinenamemetagetresponse.md)**


## get_metadata_field_values

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetRequest(
    after=121059,
    field_name='asperiores',
    limit=241545,
    pipeline_name='non',
    query='amet',
    workspace_name='beatae',
)

res = s.pipeline.get_metadata_field_values(req)

if res.pipeline_field_search_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                                                              | [operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetRequest](../../models/operations/getpipelinemetadatafieldvaluesapiv1workspacesworkspacenamepipelinespipelinenamemetafieldnamegetrequest.md) | :heavy_check_mark:                                                                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                                                                             |


### Response

**[operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetResponse](../../models/operations/getpipelinemetadatafieldvaluesapiv1workspacesworkspacenamepipelinespipelinenamemetafieldnamegetresponse.md)**


## get_min_max_aggregation_metadata

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.get_min_max_aggregation_metadata(meta_field='dignissimos', pipeline_name='a', workspace_name='debitis')

if res.pipeline_metadata_aggregation is not None:
    # handle response
```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `meta_field`                                                      | *str*                                                             | :heavy_check_mark:                                                | The name of the metadata field to get the min and max values for. |
| `pipeline_name`                                                   | *str*                                                             | :heavy_check_mark:                                                | The name of the pipeline whose files you want to display.         |
| `workspace_name`                                                  | *str*                                                             | :heavy_check_mark:                                                | Type the name of the workspace.                                   |


### Response

**[operations.GetPipelineMinMaxAggregationMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaMetaFieldAggregationGetResponse](../../models/operations/getpipelineminmaxaggregationmetadataapiv1workspacesworkspacenamepipelinespipelinenamemetametafieldaggregationgetresponse.md)**


## get_stats

Returns a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.get_stats(pipeline_name='consectetur', workspace_name='corporis')

if res.pipeline_statistics is not None:
    # handle response
```

### Parameters

| Parameter                                   | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `pipeline_name`                             | *str*                                       | :heavy_check_mark:                          | The name of the pipeline you want to fetch. |
| `workspace_name`                            | *str*                                       | :heavy_check_mark:                          | Type the name of the workspace.             |


### Response

**[operations.GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetResponse](../../models/operations/getpipelinestatsapiv1workspacesworkspacenamepipelinespipelinenamestatsgetresponse.md)**


## get_yaml

Displays the pipeline as a YAML.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.get_yaml(pipeline_name='harum', workspace_name='laboriosam')

if res.pipeline_yaml is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `pipeline_name`                                                    | *str*                                                              | :heavy_check_mark:                                                 | Specifies the name of the pipeline whose YAML you want to display. |
| `workspace_name`                                                   | *str*                                                              | :heavy_check_mark:                                                 | Type the name of the workspace.                                    |


### Response

**[operations.GetPipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlGetResponse](../../models/operations/getpipelineyamlapiv1workspacesworkspacenamepipelinespipelinenameyamlgetresponse.md)**


## list

Lists all the pipelines in the workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetRequest(
    after='0eb1ea42-6555-4ba3-8287-44ed53b88f3a',
    before='8d8f5c0b-2f2f-4b7b-994a-276b26916fe1',
    deleted=False,
    desired_status='reiciendis',
    limit=19300,
    page_number=546885,
    pipeline_name='maiores',
    status='incidunt',
    workspace_name='sed',
)

res = s.pipeline.list(req)

if res.pipeline_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetRequest](../../models/operations/listpipelinesapiv1workspacesworkspacenamepipelinesgetrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetResponse](../../models/operations/listpipelinesapiv1workspacesworkspacenamepipelinesgetresponse.md)**


## search

Run a search using a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.search(pipeline_query=shared.PipelineQuery(
    debug=False,
    filters=shared.PipelineQueryHaystackFilters(),
    params=shared.PipelineQueryPipelineParameters(),
    queries=[
        'provident',
    ],
), pipeline_name='eius', workspace_name='necessitatibus')

if res.search_result is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `pipeline_query`                                             | [shared.PipelineQuery](../../models/shared/pipelinequery.md) | :heavy_check_mark:                                           | N/A                                                          |
| `pipeline_name`                                              | *str*                                                        | :heavy_check_mark:                                           | The name of the pipeline that you want to use for search.    |
| `workspace_name`                                             | *str*                                                        | :heavy_check_mark:                                           | Type the name of the workspace.                              |


### Response

**[operations.SearchAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchPostResponse](../../models/operations/searchapiv1workspacesworkspacenamepipelinespipelinenamesearchpostresponse.md)**


## search_history

Returns the search history which includes information such as the query, the answer, the pipeline used, and more. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetRequest(
    after='3698f447-f603-4e8b-845e-80ca55efd20e',
    before='457e1858-b6a8-49fb-a3a5-aa8e4824d0ab',
    limit=299643,
    page_number=7884,
    pipeline_name='esse',
    workspace_name='ipsam',
)

res = s.pipeline.search_history(req)

if res.search_history_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                                            | [operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetRequest](../../models/operations/pipelinesearchhistoryapiv1workspacesworkspacenamepipelinespipelinenamesearchhistorygetrequest.md) | :heavy_check_mark:                                                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                                                           |


### Response

**[operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetResponse](../../models/operations/pipelinesearchhistoryapiv1workspacesworkspacenamepipelinespipelinenamesearchhistorygetresponse.md)**


## set_default

Sets a pipeline as the default pipeline for search.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.set_default(pipeline_name='sit', workspace_name='voluptatum')

if res.set_default_pipeline_api_v1_workspaces_workspace_name_pipelines_pipeline_name_default_post_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `pipeline_name`                 | *str*                           | :heavy_check_mark:              | The name of the pipeline.       |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.SetDefaultPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDefaultPostResponse](../../models/operations/setdefaultpipelineapiv1workspacesworkspacenamepipelinespipelinenamedefaultpostresponse.md)**


## undeploy

Undeploys a pipeline in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.undeploy(pipeline_name='quas', workspace_name='repudiandae')

if res.pipeline_indexing is not None:
    # handle response
```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `pipeline_name`                                             | *str*                                                       | :heavy_check_mark:                                          | The name of the pipeline that you want to use for undeploy. |
| `workspace_name`                                            | *str*                                                       | :heavy_check_mark:                                          | Type the name of the workspace.                             |


### Response

**[operations.UndeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameUndeployPostResponse](../../models/operations/undeploypipelineapiv1workspacesworkspacenamepipelinespipelinenameundeploypostresponse.md)**


## update_yaml

Updates the pipeline YAML file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.pipeline.update_yaml(pipeline_name='corporis', workspace_name='et')

if res.pipeline_name is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `pipeline_name`                 | *str*                           | :heavy_check_mark:              | N/A                             |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutResponse](../../models/operations/updatepipelineyamlapiv1workspacesworkspacenamepipelinespipelinenameyamlputresponse.md)**

