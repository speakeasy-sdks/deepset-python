<!-- Start SDK Example Usage [usage] -->
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