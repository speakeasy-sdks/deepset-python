# DocumentStore
(*.document_store*)

### Available Operations

* [check_connection](#check_connection) - Check Connection [private]
* [count_documents](#count_documents) - Count Documents Stream [private]
* [get](#get) - Get Document [private]
* [list_document_streams](#list_document_streams) - Get All Documents Stream
* [list_documents](#list_documents) - Get All Documents [private]
* [search](#search) - Query Documents Stream

## check_connection

Checks the connection to the Opensearch document store and checks if the pipeline_name (index) exists. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

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

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `index_name`                    | *str*                           | :heavy_check_mark:              | The name of the pipeline.       |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetResponse](../../models/operations/checkconnectionapiv1workspacesworkspacenameindexesindexnamegetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## count_documents

Returns the number of documents for a pipeline. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

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

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `count_documents_params`                                                       | [components.CountDocumentsParams](../../models/shared/countdocumentsparams.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `index_name`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | The name of the pipeline.                                                      |
| `workspace_name`                                                               | *str*                                                                          | :heavy_check_mark:                                                             | Type the name of the workspace.                                                |


### Response

**[operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostResponse](../../models/operations/countdocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentscountpostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## get

Displays the document content and its properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

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

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `document_id`                                                                                 | *str*                                                                                         | :heavy_check_mark:                                                                            | The identifier of the document. To obtain the ID, you can run the Get All Documents endpoint. |
| `index_name`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | The name of the pipeline used to process the documents.                                       |
| `workspace_name`                                                                              | *str*                                                                                         | :heavy_check_mark:                                                                            | Type the name of the workspace.                                                               |


### Response

**[operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetResponse](../../models/operations/getdocumentapiv1workspacesworkspacenameindexesindexnamedocumentsdocumentidgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## list_document_streams

Returns all documents created for a pipeline.

### Example Usage

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

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `fetch_documents_params`                                                       | [components.FetchDocumentsParams](../../models/shared/fetchdocumentsparams.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `index_name`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | The name of the pipeline.                                                      |
| `workspace_name`                                                               | *str*                                                                          | :heavy_check_mark:                                                             | Type the name of the workspace.                                                |


### Response

**[operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostResponse](../../models/operations/getalldocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsstreampostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## list_documents

Displays all documents processed by the specified pipeline together with their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

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

### Parameters

| Parameter                                               | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `index_name`                                            | *str*                                                   | :heavy_check_mark:                                      | The name of the pipeline used to process the documents. |
| `workspace_name`                                        | *str*                                                   | :heavy_check_mark:                                      | Type the name of the workspace.                         |
| `return_embedding`                                      | *Optional[bool]*                                        | :heavy_minus_sign:                                      | N/A                                                     |


### Response

**[operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetResponse](../../models/operations/getalldocumentsapiv1workspacesworkspacenameindexesindexnamedocumentsgetresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

## search

Searches the documents for the specified query.

### Example Usage

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

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `query_documents_params`                                                       | [components.QueryDocumentsParams](../../models/shared/querydocumentsparams.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `index_name`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | The name of the pipeline.                                                      |
| `workspace_name`                                                               | *str*                                                                          | :heavy_check_mark:                                                             | Type the name of the workspace.                                                |


### Response

**[operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostResponse](../../models/operations/querydocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsquerypostresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |
