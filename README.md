# Deepset Cloud Python SDK

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/deepset-python.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example 1

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListEvalRunsRequest(
    workspace_name='string',
)

res = s.eval_run.list(req)

if res.eval_runs_response is not None:
    # handle response
    pass
```

### Example 2

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.evaluation_set.delete(evaluation_set_name='string', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Example 3

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.evaluation_set.get(evaluation_set_name='string', workspace_name='string')

if res.label_list is not None:
    # handle response
    pass
```

### Example 4

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.evaluation_set.get_csv(evaluation_set_name='string', workspace_name='string')

if res.two_hundred_application_json_any is not None:
    # handle response
    pass
```

### Example 5

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.evaluation_set.import_evaluation_set(body_import_evaluation_set_api_v1_workspaces_workspace_name_evaluation_sets_import_post=components.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPost(
    file=components.BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostFile(
        content='0xe0a9E4eDCB'.encode(),
        file_name='forward.jpeg',
    ),
), workspace_name='string')

if res.evaluation_set_import is not None:
    # handle response
    pass
```

### Example 6

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListEvaluationSetsAPIV1WorkspacesWorkspaceNameEvaluationSetsGetRequest(
    workspace_name='string',
)

res = s.evaluation_set.list(req)

if res.evaluation_set_pagination is not None:
    # handle response
    pass
```

### Example 7

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.evaluation_set.retrigger(evaluation_set_name='string', workspace_name='string')

if res.status_code == 200:
    # handle response
    pass
```

### Example 8

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.file.delete_multi(workspace_name='string', request_body=operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteFileNames(
    names=[
        'string',
    ],
))

if res.any is not None:
    # handle response
    pass
```

### Example 9

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.file.delete_single(file_id='b655849d-609b-4e06-9c6c-7a066adc84ee', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Example 10

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.file.get(file_id='b18d8d81-fd7b-4764-a31e-475cb1f36591', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Example 11

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.file.get_document(file_id='873d3623-7b2a-4a5d-9317-57cc835bc671', workspace_name='string')

if res.documents is not None:
    # handle response
    pass
```

### Example 12

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.file.get_meta_data(file_id='ca54c4ff-7683-4387-b133-9ade3a8c3660', workspace_name='string')

if res.response_get_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_get is not None:
    # handle response
    pass
```

### Example 13

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest(
    workspace_name='string',
)

res = s.file.list(req)

if res.file_pagination is not None:
    # handle response
    pass
```

### Example 14

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.file.update_meta_data(request_body=operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutMeta(), file_id='c21bf6a8-ed89-4437-a617-505b3da68dfd', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Example 15

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.file.upload(workspace_name='string', body_upload_file_api_v1_workspaces_workspace_name_files_post=components.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPost(
    file=components.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPostFile(
        content='0x87cbca97eC'.encode(),
        file_name='ullam.wav',
    ),
), file_name='string', write_mode=operations.FileWriteModeEnum.KEEP)

if res.response_upload_file_api_v1_workspaces_workspace_name_files_post is not None:
    # handle response
    pass
```

### Example 16

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.document_store.check_connection(index_name='string', workspace_name='string')

if res.document_store is not None:
    # handle response
    pass
```

### Example 17

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.document_store.count_documents(count_documents_params=components.CountDocumentsParams(
    filters=components.HaystackFilters(),
), index_name='string', workspace_name='string')

if res.dc_document_count is not None:
    # handle response
    pass
```

### Example 18

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.document_store.get(document_id='string', index_name='string', workspace_name='string')

if res.deepset_cloud_document is not None:
    # handle response
    pass
```

### Example 19

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.document_store.list_document_streams(fetch_documents_params=components.FetchDocumentsParams(
    filters=components.FetchDocumentsParamsHaystackFilters(),
), index_name='string', workspace_name='string')

if res.status_code == 200:
    # handle response
    pass
```

### Example 20

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.document_store.list_documents(index_name='string', workspace_name='string', return_embedding=False)

if res.response_get_all_documents_api_v1_workspaces_workspace_name_indexes_index_name_documents_get is not None:
    # handle response
    pass
```

### Example 21

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.document_store.search(query_documents_params=components.QueryDocumentsParams(
    filters=components.QueryDocumentsParamsHaystackFilters(),
    query_emb=[
        3076.31,
    ],
), index_name='string', workspace_name='string')

if res.response_query_documents_stream_api_v1_workspaces_workspace_name_indexes_index_name_documents_query_post is not None:
    # handle response
    pass
```

### Example 22

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.add_feedback(post_pipeline_feedback=components.PostPipelineFeedback(
    is_correct_answer=False,
    is_correct_document=False,
    result_id='ed8b6158-4f3d-4250-92ce-685935248904',
    tags=[
        'string',
    ],
), pipeline_name='string', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Example 23

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.create(workspace_name='string', dry_run=False)

if res.pipeline_name is not None:
    # handle response
    pass
```

### Example 24

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.delete(pipeline_name='string', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Example 25

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.deploy(pipeline_name='string', workspace_name='string')

if res.pipeline_indexing is not None:
    # handle response
    pass
```

### Example 26

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.get(pipeline_name='string', workspace_name='string')

if res.pipeline_indexing is not None:
    # handle response
    pass
```

### Example 27

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetRequest(
    pipeline_name='string',
    workspace_name='string',
)

res = s.pipeline.get_feedback(req)

if res.response_200_get_pipeline_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_get is not None:
    # handle response
    pass
```

### Example 28

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.get_files(pipeline_name='string', workspace_name='string', status=operations.FileIndexingStatusQuery.INDEXED_NO_DOCUMENTS)

if res.response_get_pipeline_files_api_v1_workspaces_workspace_name_pipelines_pipeline_name_files_get is not None:
    # handle response
    pass
```

### Example 29

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.get_indexing(pipeline_name='string', workspace_name='string')

if res.pipeline_indexing_status_detail is not None:
    # handle response
    pass
```

### Example 30

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.get_json(pipeline_name='string', workspace_name='string')

if res.response_get_pipeline_yaml_as_json_api_v1_workspaces_workspace_name_pipelines_pipeline_name_json_get is not None:
    # handle response
    pass
```

### Example 31

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.get_metadata(pipeline_name='string', workspace_name='string')

if res.response_200_get_pipeline_index_metadata_api_v1_workspaces_workspace_name_pipelines_pipeline_name_meta_get is not None:
    # handle response
    pass
```

### Example 32

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetRequest(
    field_name='string',
    pipeline_name='string',
    workspace_name='string',
)

res = s.pipeline.get_metadata_field_values(req)

if res.pipeline_field_search_result is not None:
    # handle response
    pass
```

### Example 33

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.get_min_max_aggregation_metadata(meta_field='string', pipeline_name='string', workspace_name='string')

if res.pipeline_metadata_aggregation is not None:
    # handle response
    pass
```

### Example 34

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.get_stats(pipeline_name='string', workspace_name='string')

if res.pipeline_statistics is not None:
    # handle response
    pass
```

### Example 35

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.get_yaml(pipeline_name='string', workspace_name='string')

if res.pipeline_yaml is not None:
    # handle response
    pass
```

### Example 36

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListPipelinesAPIV1WorkspacesWorkspaceNamePipelinesGetRequest(
    workspace_name='string',
)

res = s.pipeline.list(req)

if res.pipeline_pagination is not None:
    # handle response
    pass
```

### Example 37

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.search(pipeline_query=components.PipelineQuery(
    filters=components.PipelineQueryHaystackFilters(),
    params=components.PipelineQueryPipelineParameters(),
    queries=[
        'string',
    ],
), pipeline_name='string', workspace_name='string')

if res.search_result is not None:
    # handle response
    pass
```

### Example 38

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.PipelineSearchHistoryAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameSearchHistoryGetRequest(
    pipeline_name='string',
    workspace_name='string',
)

res = s.pipeline.search_history(req)

if res.search_history_pagination is not None:
    # handle response
    pass
```

### Example 39

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.set_default(pipeline_name='string', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Example 40

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.undeploy(pipeline_name='string', workspace_name='string')

if res.pipeline_indexing is not None:
    # handle response
    pass
```

### Example 41

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.pipeline.update_yaml(pipeline_name='string', workspace_name='string')

if res.pipeline_name is not None:
    # handle response
    pass
```

### Example 42

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.search_session.create(workspace_name='string')

if res.search_session_post_response is not None:
    # handle response
    pass
```

### Example 43

```python
import dateutil.parser
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.create(post_shared_prototype=components.PostSharedPrototype(
    expiration_date=dateutil.parser.isoparse('2022-06-17T19:34:14.348Z'),
    pipeline_names=[
        'string',
    ],
), workspace_name='string')

if res.shared_prototype is not None:
    # handle response
    pass
```

### Example 44

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.create_external_user(workspace_name='string', existing_user_id='cb14aeb0-f38a-4ede-8206-c6a3a8239cb0')

if res.external_user_information is not None:
    # handle response
    pass
```

### Example 45

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.get(shared_prototype_id='b18d8d81-fd7b-4764-a31e-475cb1f36591', workspace_name='string')

if res.shared_prototype is not None:
    # handle response
    pass
```

### Example 46

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest(
    workspace_name='string',
)

res = s.shared_prototype.list(req)

if res.paginated_shared_prototypes is not None:
    # handle response
    pass
```

### Example 47

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.revoke(shared_prototype_id='db021625-f680-4f7d-9078-89cd3534dba0', workspace_name='string')

if res.any is not None:
    # handle response
    pass
```

### Example 48

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.shared_prototype.update(patch_shared_prototype=components.PatchSharedPrototype(), shared_prototype_id='d0905bf4-aa77-4f20-8e77-54c352acfe54', workspace_name='string')

if res.shared_prototype is not None:
    # handle response
    pass
```

### Example 49

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.upload_session.close(close_session=components.CloseSession(), session_id='858bd1fe-535f-4534-856e-5d2a350c163f', workspace_name='string')

if res.status_code == 200:
    # handle response
    pass
```

### Example 50

```python
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.upload_session.create(create_session=components.CreateSession(), workspace_name='string')

if res.upload_session is not None:
    # handle response
    pass
```

### Example 51

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetRequest(
    session_id='a693fbb2-e996-4d93-8cbc-082b8e9824c8',
    workspace_name='string',
)

res = s.upload_session.get_files(req)

if res.paginated_session_file is not None:
    # handle response
    pass
```

### Example 52

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.upload_session.get_status(session_id='7b8c13f1-f508-4288-9a9d-4f095d2fd2e9', workspace_name='string')

if res.session_detail is not None:
    # handle response
    pass
```

### Example 53

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetRequest(
    workspace_name='string',
)

res = s.upload_session.list(req)

if res.paginated_session is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [health](docs/sdks/health/README.md)

* [check](docs/sdks/health/README.md#check) - Health
* [get_openapi](docs/sdks/health/README.md#get_openapi) - Redirect

### [user](docs/sdks/user/README.md)

* [delete](docs/sdks/user/README.md#delete) - Delete User [private]
* [get](docs/sdks/user/README.md#get) - Get User [private]
* [list](docs/sdks/user/README.md#list) - Get Users [private]
* [me](docs/sdks/user/README.md#me) - Read Users Me [private]
* [update_permission](docs/sdks/user/README.md#update_permission) - Update User Permission [private]

### [models](docs/sdks/models/README.md)

* [list](docs/sdks/models/README.md#list) - Get Model [private]

### [model_registry_token](docs/sdks/modelregistrytoken/README.md)

* [get](docs/sdks/modelregistrytoken/README.md#get) - Get Token [private]
* [~~get_token_deprecated~~](docs/sdks/modelregistrytoken/README.md#get_token_deprecated) - Get Token Deprecated [private] :warning: **Deprecated**
* [list](docs/sdks/modelregistrytoken/README.md#list) - Get Tokens [private]
* [remove](docs/sdks/modelregistrytoken/README.md#remove) - Remove Token [private]
* [~~remove_token_deprecated~~](docs/sdks/modelregistrytoken/README.md#remove_token_deprecated) - Remove Token Deprecated [private] :warning: **Deprecated**
* [save](docs/sdks/modelregistrytoken/README.md#save) - Save Token [private]
* [~~save_token_deprecated~~](docs/sdks/modelregistrytoken/README.md#save_token_deprecated) - Save Token Deprecated [private] :warning: **Deprecated**
* [update](docs/sdks/modelregistrytoken/README.md#update) - Update Token [private]
* [~~update_token_deprecated~~](docs/sdks/modelregistrytoken/README.md#update_token_deprecated) - Update Token Deprecated [private] :warning: **Deprecated**

### [notebook](docs/sdks/notebook/README.md)

* [create](docs/sdks/notebook/README.md#create) - Post Notebook [private]
* [get_server_state](docs/sdks/notebook/README.md#get_server_state) - Get Jupyter Lab [private]
* [start](docs/sdks/notebook/README.md#start) - Start Jupyter Lab [private]

### [organization](docs/sdks/organization/README.md)

* [get](docs/sdks/organization/README.md#get) - Get Organization [private]
* [invite](docs/sdks/organization/README.md#invite) - Invite User To Organization [private]

### [api_token](docs/sdks/apitoken/README.md)

* [create_token](docs/sdks/apitoken/README.md#create_token) - Create Token
* [list](docs/sdks/apitoken/README.md#list) - Get Tokens [private]
* [remove](docs/sdks/apitoken/README.md#remove) - Remove Token [private]

### [workspace](docs/sdks/workspace/README.md)

* [create](docs/sdks/workspace/README.md#create) - Create Workspace [private]
* [delete](docs/sdks/workspace/README.md#delete) - Delete Workspace [private]
* [get](docs/sdks/workspace/README.md#get) - Get Workspace [private]
* [get_stats](docs/sdks/workspace/README.md#get_stats) - Get Workspace Stats [private]
* [list](docs/sdks/workspace/README.md#list) - List Workspaces [private]
* [search_count](docs/sdks/workspace/README.md#search_count) - Search Count [private]
* [search_history](docs/sdks/workspace/README.md#search_history) - Search History [private]

### [eval_run](docs/sdks/evalrun/README.md)

* [create_eval_run](docs/sdks/evalrun/README.md#create_eval_run) - Create Eval Run
* [create_tag](docs/sdks/evalrun/README.md#create_tag) - Create Tag [private]
* [delete](docs/sdks/evalrun/README.md#delete) - Delete Eval Run
* [delete_tag](docs/sdks/evalrun/README.md#delete_tag) - Delete Tag [private]
* [get](docs/sdks/evalrun/README.md#get) - Get Eval Run
* [get_node_eval_predictions](docs/sdks/evalrun/README.md#get_node_eval_predictions) - Get Node Eval Predictions
* [list](docs/sdks/evalrun/README.md#list) - Get Eval Runs
* [list_tags](docs/sdks/evalrun/README.md#list_tags) - Get Tags [private]
* [start](docs/sdks/evalrun/README.md#start) - Start Eval Run
* [update](docs/sdks/evalrun/README.md#update) - Edit Eval Run
* [update_tag](docs/sdks/evalrun/README.md#update_tag) - Update Tag [private]

### [evaluation_set](docs/sdks/evaluationset/README.md)

* [delete](docs/sdks/evaluationset/README.md#delete) - Delete Evaluation Set
* [get](docs/sdks/evaluationset/README.md#get) - Get Evaluation Set
* [get_csv](docs/sdks/evaluationset/README.md#get_csv) - Get Evaluation Set Csv File
* [import_evaluation_set](docs/sdks/evaluationset/README.md#import_evaluation_set) - Import Evaluation Set
* [list](docs/sdks/evaluationset/README.md#list) - Get Evaluation Sets
* [retrigger](docs/sdks/evaluationset/README.md#retrigger) - Retrigger Label Matching

### [file](docs/sdks/file/README.md)

* [delete_multi](docs/sdks/file/README.md#delete_multi) - Delete Files
* [delete_single](docs/sdks/file/README.md#delete_single) - Delete File
* [get](docs/sdks/file/README.md#get) - Get File
* [get_document](docs/sdks/file/README.md#get_document) - Get Document
* [get_meta_data](docs/sdks/file/README.md#get_meta_data) - Get File Meta
* [list](docs/sdks/file/README.md#list) - List Files
* [update_meta_data](docs/sdks/file/README.md#update_meta_data) - Update File Meta
* [upload](docs/sdks/file/README.md#upload) - Upload File

### [document_store](docs/sdks/documentstore/README.md)

* [check_connection](docs/sdks/documentstore/README.md#check_connection) - Check Connection [private]
* [count_documents](docs/sdks/documentstore/README.md#count_documents) - Count Documents Stream [private]
* [get](docs/sdks/documentstore/README.md#get) - Get Document [private]
* [list_document_streams](docs/sdks/documentstore/README.md#list_document_streams) - Get All Documents Stream
* [list_documents](docs/sdks/documentstore/README.md#list_documents) - Get All Documents [private]
* [search](docs/sdks/documentstore/README.md#search) - Query Documents Stream

### [pipeline](docs/sdks/pipeline/README.md)

* [add_feedback](docs/sdks/pipeline/README.md#add_feedback) - Add Feedback
* [create](docs/sdks/pipeline/README.md#create) - Create Pipeline
* [delete](docs/sdks/pipeline/README.md#delete) - Delete Pipeline
* [deploy](docs/sdks/pipeline/README.md#deploy) - Deploy Pipeline
* [get](docs/sdks/pipeline/README.md#get) - Get Pipeline
* [get_feedback](docs/sdks/pipeline/README.md#get_feedback) - Get Pipeline Feedback
* [get_files](docs/sdks/pipeline/README.md#get_files) - Get Pipeline Files
* [get_indexing](docs/sdks/pipeline/README.md#get_indexing) - Get Pipeline Indexing
* [get_json](docs/sdks/pipeline/README.md#get_json) - Get Pipeline Yaml As Json
* [get_metadata](docs/sdks/pipeline/README.md#get_metadata) - Get Pipeline Index Metadata [private]
* [get_metadata_field_values](docs/sdks/pipeline/README.md#get_metadata_field_values) - Get Pipeline Metadata Field Values [private]
* [get_min_max_aggregation_metadata](docs/sdks/pipeline/README.md#get_min_max_aggregation_metadata) - Get Pipeline Min Max Aggregation Metadata [private]
* [get_stats](docs/sdks/pipeline/README.md#get_stats) - Get Pipeline Stats
* [get_yaml](docs/sdks/pipeline/README.md#get_yaml) - Get Pipeline Yaml
* [list](docs/sdks/pipeline/README.md#list) - List Pipelines
* [search](docs/sdks/pipeline/README.md#search) - Search
* [search_history](docs/sdks/pipeline/README.md#search_history) - Pipeline Search History [private]
* [set_default](docs/sdks/pipeline/README.md#set_default) - Set Default Pipeline
* [undeploy](docs/sdks/pipeline/README.md#undeploy) - Undeploy Pipeline
* [update_yaml](docs/sdks/pipeline/README.md#update_yaml) - Update Pipeline Yaml

### [search_session](docs/sdks/searchsession/README.md)

* [create](docs/sdks/searchsession/README.md#create) - Create Search Session [private]

### [shared_prototype](docs/sdks/sharedprototype/README.md)

* [create](docs/sdks/sharedprototype/README.md#create) - Create Prototype [private]
* [create_external_user](docs/sdks/sharedprototype/README.md#create_external_user) - Create External User [private]
* [get](docs/sdks/sharedprototype/README.md#get) - Get Shared Prototype [private]
* [list](docs/sdks/sharedprototype/README.md#list) - List Prototypes [private]
* [revoke](docs/sdks/sharedprototype/README.md#revoke) - Revoke Shared Prototype [private]
* [update](docs/sdks/sharedprototype/README.md#update) - Edit Shared Prototype [private]

### [upload_session](docs/sdks/uploadsession/README.md)

* [close](docs/sdks/uploadsession/README.md#close) - Close Session
* [create](docs/sdks/uploadsession/README.md#create) - Create Upload Session
* [get_files](docs/sdks/uploadsession/README.md#get_files) - Get Session Files
* [get_status](docs/sdks/uploadsession/README.md#get_status) - Get Session Status
* [list](docs/sdks/uploadsession/README.md#list) - Get Upload Sessions
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

### Example

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = None
try:
    res = s.user.delete(user_id='8db863f6-ef9b-413a-8a70-cb816b33de6b')
except errors.HTTPValidationError as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.any is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.cloud.deepset.ai` | None |

#### Example

```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    server_idx=0,
    http_bearer="",
)


res = s.health.check()

if res.response_health_health_get is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    server_url="https://api.cloud.deepset.ai",
    http_bearer="",
)


res = s.health.check()

if res.response_health_health_get is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import deepset_cloud
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = deepset_cloud.DeepsetCloud(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `http_bearer` | http          | HTTP Bearer   |

To authenticate with the API the `http_bearer` parameter must be set when initializing the SDK client instance. For example:
```python
import deepset_cloud

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.health.check()

if res.response_health_health_get is not None:
    # handle response
    pass
```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import dateutil.parser
import deepset_cloud
from deepset_cloud.models import components, operations

s = deepset_cloud.DeepsetCloud()

req = components.CreateToken()

res = s.api_token.create_token(req, operations.CreateTokenAPIV1TokenPostSecurity(
    http_bearer="",
))

if res.api_token_result is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
