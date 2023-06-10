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
        result_id='2e9817ee-17cb-4e61-a6b7-b95bc0ab3c20',
        tags=[
            'quaerat',
            'sapiente',
            'consectetur',
            'esse',
        ],
    ),
    pipeline_name='blanditiis',
    workspace_name='provident',
)

res = s.pipeline.add_feedback(req, operations.AddFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackPostSecurity(
    http_bearer="",
))

if res.add_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_post_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                  | Type                                                                                                                                                                                                       | Required                                                                                                                                                                                                   | Description                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                  | [operations.AddFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackPostRequest](../../models/operations/addfeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackpostrequest.md)   | :heavy_check_mark:                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                 |
| `security`                                                                                                                                                                                                 | [operations.AddFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackPostSecurity](../../models/operations/addfeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                         | The security requirements to use for the request.                                                                                                                                                          |


### Response

**[operations.AddFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackPostResponse](../../models/operations/addfeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackpostresponse.md)**


## create

Creates a pipeline YAML file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.CreatePipelineAPIV1WorkspacesWorkspaceNamePipelinesPostRequest(
    dry_run=False,
    workspace_name='a',
)

res = s.pipeline.create(req, operations.CreatePipelineAPIV1WorkspacesWorkspaceNamePipelinesPostSecurity(
    http_bearer="",
))

if res.pipeline_name is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                | [operations.CreatePipelineAPIV1WorkspacesWorkspaceNamePipelinesPostRequest](../../models/operations/createpipelineapiv1workspacesworkspacenamepipelinespostrequest.md)   | :heavy_check_mark:                                                                                                                                                       | The request object to use for the request.                                                                                                                               |
| `security`                                                                                                                                                               | [operations.CreatePipelineAPIV1WorkspacesWorkspaceNamePipelinesPostSecurity](../../models/operations/createpipelineapiv1workspacesworkspacenamepipelinespostsecurity.md) | :heavy_check_mark:                                                                                                                                                       | The security requirements to use for the request.                                                                                                                        |


### Response

**[operations.CreatePipelineAPIV1WorkspacesWorkspaceNamePipelinesPostResponse](../../models/operations/createpipelineapiv1workspacesworkspacenamepipelinespostresponse.md)**


## delete

Deletes a pipeline from deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeletePipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeleteRequest(
    pipeline_name='nulla',
    workspace_name='quas',
)

res = s.pipeline.delete(req, operations.DeletePipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeleteSecurity(
    http_bearer="",
))

if res.delete_pipeline_api_v1_workspaces_workspace_name_pipelines_pipeline_name_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                            | [operations.DeletePipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeleteRequest](../../models/operations/deletepipelineapiv1workspacesworkspacenamepipelinespipelinenamedeleterequest.md)   | :heavy_check_mark:                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                           |
| `security`                                                                                                                                                                                           | [operations.DeletePipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeleteSecurity](../../models/operations/deletepipelineapiv1workspacesworkspacenamepipelinespipelinenamedeletesecurity.md) | :heavy_check_mark:                                                                                                                                                                                   | The security requirements to use for the request.                                                                                                                                                    |


### Response

**[operations.DeletePipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeleteResponse](../../models/operations/deletepipelineapiv1workspacesworkspacenamepipelinespipelinenamedeleteresponse.md)**


## deploy

Deploys a pipeline in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeployPostRequest(
    pipeline_name='esse',
    workspace_name='quasi',
)

res = s.pipeline.deploy(req, operations.DeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeployPostSecurity(
    http_bearer="",
))

if res.pipeline_indexing is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.DeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeployPostRequest](../../models/operations/deploypipelineapiv1workspacesworkspacenamepipelinespipelinenamedeploypostrequest.md)   | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |
| `security`                                                                                                                                                                                                   | [operations.DeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeployPostSecurity](../../models/operations/deploypipelineapiv1workspacesworkspacenamepipelinespipelinenamedeploypostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                           | The security requirements to use for the request.                                                                                                                                                            |


### Response

**[operations.DeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDeployPostResponse](../../models/operations/deploypipelineapiv1workspacesworkspacenamepipelinespipelinenamedeploypostresponse.md)**


## get

Returns a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameGetRequest(
    pipeline_name='a',
    workspace_name='error',
)

res = s.pipeline.get(req, operations.GetPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameGetSecurity(
    http_bearer="",
))

if res.pipeline_indexing is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                | [operations.GetPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameGetRequest](../../models/operations/getpipelineapiv1workspacesworkspacenamepipelinespipelinenamegetrequest.md)   | :heavy_check_mark:                                                                                                                                                                       | The request object to use for the request.                                                                                                                                               |
| `security`                                                                                                                                                                               | [operations.GetPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameGetSecurity](../../models/operations/getpipelineapiv1workspacesworkspacenamepipelinespipelinenamegetsecurity.md) | :heavy_check_mark:                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                        |


### Response

**[operations.GetPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameGetResponse](../../models/operations/getpipelineapiv1workspacesworkspacenamepipelinespipelinenamegetresponse.md)**


## get_feedback

Returns the feedback in JSON or CSV format.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetRequest(
    after='9dd2efd1-21aa-46f1-a674-bdb04f157560',
    before='82d68ea1-9f1d-4170-9133-9d08086a1840',
    field=operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetFieldField.SEARCH_RESULT_RANK,
    filter='occaecati',
    limit=253191,
    order=operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetOrderOrder.DESC,
    page_number=131055,
    pipeline_name='voluptas',
    select='aut',
    workspace_name='dignissimos',
)

res = s.pipeline.get_feedback(req, operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetSecurity(
    http_bearer="",
))

if res.response_200_get_pipeline_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                | Type                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                 | Description                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                                | [operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetRequest](../../models/operations/getpipelinefeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                       | The request object to use for the request.                                                                                                                                                                               |
| `security`                                                                                                                                                                                                               | [operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetSecurity](../../models/operations/getpipelinefeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                                                        |


### Response

**[operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetResponse](../../models/operations/getpipelinefeedbackapiv1workspacesworkspacenamepipelinespipelinenamefeedbackgetresponse.md)**


## get_files

Returns IDs of all files with a specific status.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetRequest(
    pipeline_name='dicta',
    status=operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetStatusFileIndexingStatusQuery.INDEXED_NO_DOCUMENTS,
    workspace_name='natus',
)

res = s.pipeline.get_files(req, operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetSecurity(
    http_bearer="",
))

if res.get_pipeline_files_api_v1_workspaces_workspace_name_pipelines_pipeline_name_files_get_200_application_json_uuid_strings is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetRequest](../../models/operations/getpipelinefilesapiv1workspacesworkspacenamepipelinespipelinenamefilesgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |
| `security`                                                                                                                                                                                                   | [operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetSecurity](../../models/operations/getpipelinefilesapiv1workspacesworkspacenamepipelinespipelinenamefilesgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                           | The security requirements to use for the request.                                                                                                                                                            |


### Response

**[operations.GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetResponse](../../models/operations/getpipelinefilesapiv1workspacesworkspacenamepipelinespipelinenamefilesgetresponse.md)**


## get_indexing

Returns the indexing information for a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineIndexingAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameIndexingGetRequest(
    pipeline_name='velit',
    workspace_name='voluptatibus',
)

res = s.pipeline.get_indexing(req, operations.GetPipelineIndexingAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameIndexingGetSecurity(
    http_bearer="",
))

if res.pipeline_indexing_status_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                | Type                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                 | Description                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                                | [operations.GetPipelineIndexingAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameIndexingGetRequest](../../models/operations/getpipelineindexingapiv1workspacesworkspacenamepipelinespipelinenameindexinggetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                       | The request object to use for the request.                                                                                                                                                                               |
| `security`                                                                                                                                                                                                               | [operations.GetPipelineIndexingAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameIndexingGetSecurity](../../models/operations/getpipelineindexingapiv1workspacesworkspacenamepipelinespipelinenameindexinggetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                                                        |


### Response

**[operations.GetPipelineIndexingAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameIndexingGetResponse](../../models/operations/getpipelineindexingapiv1workspacesworkspacenamepipelinespipelinenameindexinggetresponse.md)**


## get_json

Returns the pipeline in the JSON format.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetRequest(
    pipeline_name='voluptas',
    workspace_name='asperiores',
)

res = s.pipeline.get_json(req, operations.GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetSecurity(
    http_bearer="",
))

if res.response_get_pipeline_yaml_as_json_api_v1_workspaces_workspace_name_pipelines_pipeline_name_json_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                            | [operations.GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetRequest](../../models/operations/getpipelineyamlasjsonapiv1workspacesworkspacenamepipelinespipelinenamejsongetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                                           |
| `security`                                                                                                                                                                                                           | [operations.GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetSecurity](../../models/operations/getpipelineyamlasjsonapiv1workspacesworkspacenamepipelinespipelinenamejsongetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                   | The security requirements to use for the request.                                                                                                                                                                    |


### Response

**[operations.GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetResponse](../../models/operations/getpipelineyamlasjsonapiv1workspacesworkspacenamepipelinespipelinenamejsongetresponse.md)**


## get_metadata

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineIndexMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaGetRequest(
    pipeline_name='aperiam',
    workspace_name='ea',
)

res = s.pipeline.get_metadata(req, operations.GetPipelineIndexMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaGetSecurity(
    http_bearer="",
))

if res.response_200_get_pipeline_index_metadata_api_v1_workspaces_workspace_name_pipelines_pipeline_name_meta_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                  | [operations.GetPipelineIndexMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaGetRequest](../../models/operations/getpipelineindexmetadataapiv1workspacesworkspacenamepipelinespipelinenamemetagetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                                 |
| `security`                                                                                                                                                                                                                 | [operations.GetPipelineIndexMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaGetSecurity](../../models/operations/getpipelineindexmetadataapiv1workspacesworkspacenamepipelinespipelinenamemetagetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                         | The security requirements to use for the request.                                                                                                                                                                          |


### Response

**[operations.GetPipelineIndexMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaGetResponse](../../models/operations/getpipelineindexmetadataapiv1workspacesworkspacenamepipelinespipelinenamemetagetresponse.md)**


## get_metadata_field_values

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetRequest(
    after=310067,
    field_name='consequuntur',
    limit=831520,
    pipeline_name='officia',
    query='maxime',
    workspace_name='dignissimos',
)

res = s.pipeline.get_metadata_field_values(req, operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetSecurity(
    http_bearer="",
))

if res.pipeline_field_search_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                                                | [operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetRequest](../../models/operations/getpipelinemetadatafieldvaluesapiv1workspacesworkspacenamepipelinespipelinenamemetafieldnamegetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                                                       | The request object to use for the request.                                                                                                                                                                                                               |
| `security`                                                                                                                                                                                                                                               | [operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetSecurity](../../models/operations/getpipelinemetadatafieldvaluesapiv1workspacesworkspacenamepipelinespipelinenamemetafieldnamegetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                                                                                        |


### Response

**[operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetResponse](../../models/operations/getpipelinemetadatafieldvaluesapiv1workspacesworkspacenamepipelinespipelinenamemetafieldnamegetresponse.md)**


## get_min_max_aggregation_metadata

This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineMinMaxAggregationMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaMetaFieldAggregationGetRequest(
    meta_field='officia',
    pipeline_name='asperiores',
    workspace_name='nemo',
)

res = s.pipeline.get_min_max_aggregation_metadata(req, operations.GetPipelineMinMaxAggregationMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaMetaFieldAggregationGetSecurity(
    http_bearer="",
))

if res.pipeline_metadata_aggregation is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                                                                                                  | [operations.GetPipelineMinMaxAggregationMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaMetaFieldAggregationGetRequest](../../models/operations/getpipelineminmaxaggregationmetadataapiv1workspacesworkspacenamepipelinespipelinenamemetametafieldaggregationgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                                                                                         | The request object to use for the request.                                                                                                                                                                                                                                                 |
| `security`                                                                                                                                                                                                                                                                                 | [operations.GetPipelineMinMaxAggregationMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaMetaFieldAggregationGetSecurity](../../models/operations/getpipelineminmaxaggregationmetadataapiv1workspacesworkspacenamepipelinespipelinenamemetametafieldaggregationgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                                                                         | The security requirements to use for the request.                                                                                                                                                                                                                                          |


### Response

**[operations.GetPipelineMinMaxAggregationMetadataAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaMetaFieldAggregationGetResponse](../../models/operations/getpipelineminmaxaggregationmetadataapiv1workspacesworkspacenamepipelinespipelinenamemetametafieldaggregationgetresponse.md)**


## get_stats

Returns a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetRequest(
    pipeline_name='quae',
    workspace_name='quaerat',
)

res = s.pipeline.get_stats(req, operations.GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetSecurity(
    http_bearer="",
))

if res.pipeline_statistics is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetRequest](../../models/operations/getpipelinestatsapiv1workspacesworkspacenamepipelinespipelinenamestatsgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |
| `security`                                                                                                                                                                                                   | [operations.GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetSecurity](../../models/operations/getpipelinestatsapiv1workspacesworkspacenamepipelinespipelinenamestatsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                           | The security requirements to use for the request.                                                                                                                                                            |


### Response

**[operations.GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetResponse](../../models/operations/getpipelinestatsapiv1workspacesworkspacenamepipelinespipelinenamestatsgetresponse.md)**


## get_yaml

Displays the pipeline as a YAML.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetPipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlGetRequest(
    pipeline_name='porro',
    workspace_name='quod',
)

res = s.pipeline.get_yaml(req, operations.GetPipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlGetSecurity(
    http_bearer="",
))

if res.pipeline_yaml is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                | [operations.GetPipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlGetRequest](../../models/operations/getpipelineyamlapiv1workspacesworkspacenamepipelinespipelinenameyamlgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                       | The request object to use for the request.                                                                                                                                                               |
| `security`                                                                                                                                                                                               | [operations.GetPipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlGetSecurity](../../models/operations/getpipelineyamlapiv1workspacesworkspacenamepipelinespipelinenameyamlgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                                        |


### Response

**[operations.GetPipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlGetResponse](../../models/operations/getpipelineyamlapiv1workspacesworkspacenamepipelinespipelinenameyamlgetresponse.md)**


## list

Lists all the pipelines in the workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetRequest(
    after='413aa63a-ae8d-4678-a4db-b675fd5e60b3',
    before='75ed4f6f-bee4-41f3-b317-fe35b60eb1ea',
    deleted=False,
    desired_status='tempora',
    limit=132815,
    page_number=379057,
    pipeline_name='voluptas',
    status='voluptas',
    workspace_name='minima',
)

res = s.pipeline.list(req, operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetSecurity(
    http_bearer="",
))

if res.pipeline_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetRequest](../../models/operations/listpipelinesapiv1workspacesworkspacenamepipelinesgetrequest.md)   | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |
| `security`                                                                                                                                                           | [operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetSecurity](../../models/operations/listpipelinesapiv1workspacesworkspacenamepipelinesgetsecurity.md) | :heavy_check_mark:                                                                                                                                                   | The security requirements to use for the request.                                                                                                                    |


### Response

**[operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetResponse](../../models/operations/listpipelinesapiv1workspacesworkspacenamepipelinesgetresponse.md)**


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
        filters=shared.PipelineQueryHaystackFilters(),
        params=shared.PipelineQueryPipelineParameters(),
        queries=[
            'dolorum',
            'adipisci',
            'minus',
        ],
    ),
    pipeline_name='dolores',
    workspace_name='blanditiis',
)

res = s.pipeline.search(req, operations.SearchAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchPostSecurity(
    http_bearer="",
))

if res.search_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                    | [operations.SearchAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchPostRequest](../../models/operations/searchapiv1workspacesworkspacenamepipelinespipelinenamesearchpostrequest.md)   | :heavy_check_mark:                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                   |
| `security`                                                                                                                                                                                   | [operations.SearchAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchPostSecurity](../../models/operations/searchapiv1workspacesworkspacenamepipelinespipelinenamesearchpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                           | The security requirements to use for the request.                                                                                                                                            |


### Response

**[operations.SearchAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchPostResponse](../../models/operations/searchapiv1workspacesworkspacenamepipelinespipelinenamesearchpostresponse.md)**


## search_history

Returns the search history which includes information such as the query, the answer, the pipeline used, and more. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetRequest(
    after='744ed53b-88f3-4a8d-8f5c-0b2f2fb7b194',
    before='a276b269-16fe-41f0-8f42-94e3698f447f',
    limit=401713,
    page_number=25497,
    pipeline_name='non',
    workspace_name='officiis',
)

res = s.pipeline.search_history(req, operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetSecurity(
    http_bearer="",
))

if res.search_history_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                              | [operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetRequest](../../models/operations/pipelinesearchhistoryapiv1workspacesworkspacenamepipelinespipelinenamesearchhistorygetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                                                             |
| `security`                                                                                                                                                                                                                             | [operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetSecurity](../../models/operations/pipelinesearchhistoryapiv1workspacesworkspacenamepipelinespipelinenamesearchhistorygetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                                                                      |


### Response

**[operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetResponse](../../models/operations/pipelinesearchhistoryapiv1workspacesworkspacenamepipelinespipelinenamesearchhistorygetresponse.md)**


## set_default

Sets a pipeline as the default pipeline for search.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.SetDefaultPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDefaultPostRequest(
    pipeline_name='praesentium',
    workspace_name='facilis',
)

res = s.pipeline.set_default(req, operations.SetDefaultPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDefaultPostSecurity(
    http_bearer="",
))

if res.set_default_pipeline_api_v1_workspaces_workspace_name_pipelines_pipeline_name_default_post_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                              | Type                                                                                                                                                                                                                   | Required                                                                                                                                                                                                               | Description                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                              | [operations.SetDefaultPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDefaultPostRequest](../../models/operations/setdefaultpipelineapiv1workspacesworkspacenamepipelinespipelinenamedefaultpostrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                                             |
| `security`                                                                                                                                                                                                             | [operations.SetDefaultPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDefaultPostSecurity](../../models/operations/setdefaultpipelineapiv1workspacesworkspacenamepipelinespipelinenamedefaultpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                                                      |


### Response

**[operations.SetDefaultPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameDefaultPostResponse](../../models/operations/setdefaultpipelineapiv1workspacesworkspacenamepipelinespipelinenamedefaultpostresponse.md)**


## undeploy

Undeploys a pipeline in deepset Cloud.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.UndeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameUndeployPostRequest(
    pipeline_name='quaerat',
    workspace_name='incidunt',
)

res = s.pipeline.undeploy(req, operations.UndeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameUndeployPostSecurity(
    http_bearer="",
))

if res.pipeline_indexing is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                            | [operations.UndeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameUndeployPostRequest](../../models/operations/undeploypipelineapiv1workspacesworkspacenamepipelinespipelinenameundeploypostrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                                           |
| `security`                                                                                                                                                                                                           | [operations.UndeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameUndeployPostSecurity](../../models/operations/undeploypipelineapiv1workspacesworkspacenamepipelinespipelinenameundeploypostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                   | The security requirements to use for the request.                                                                                                                                                                    |


### Response

**[operations.UndeployPipelineAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameUndeployPostResponse](../../models/operations/undeploypipelineapiv1workspacesworkspacenamepipelinespipelinenameundeploypostresponse.md)**


## update_yaml

Updates the pipeline YAML file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutRequest(
    pipeline_name='ipsam',
    workspace_name='debitis',
)

res = s.pipeline.update_yaml(req, operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutSecurity(
    http_bearer="",
))

if res.pipeline_name is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                      | [operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutRequest](../../models/operations/updatepipelineyamlapiv1workspacesworkspacenamepipelinespipelinenameyamlputrequest.md)   | :heavy_check_mark:                                                                                                                                                                                             | The request object to use for the request.                                                                                                                                                                     |
| `security`                                                                                                                                                                                                     | [operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutSecurity](../../models/operations/updatepipelineyamlapiv1workspacesworkspacenamepipelinespipelinenameyamlputsecurity.md) | :heavy_check_mark:                                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                                              |


### Response

**[operations.UpdatePipelineYamlAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameYamlPutResponse](../../models/operations/updatepipelineyamlapiv1workspacesworkspacenamepipelinespipelinenameyamlputresponse.md)**

