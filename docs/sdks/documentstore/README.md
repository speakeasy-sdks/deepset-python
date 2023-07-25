# document_store

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

s = deepset_cloud.DeepsetCloud()


res = s.document_store.check_connection(operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetSecurity(
    http_bearer="",
), 'quidem', 'molestias')

if res.document_store is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                             | [operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetSecurity](../../models/operations/checkconnectionapiv1workspacesworkspacenameindexesindexnamegetsecurity.md) | :heavy_check_mark:                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                      |
| `index_name`                                                                                                                                                                           | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The name of the pipeline.                                                                                                                                                              |
| `workspace_name`                                                                                                                                                                       | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Type the name of the workspace.                                                                                                                                                        |


### Response

**[operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetResponse](../../models/operations/checkconnectionapiv1workspacesworkspacenameindexesindexnamegetresponse.md)**


## count_documents

Returns the number of documents for a pipeline. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.document_store.count_documents(operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostSecurity(
    http_bearer="",
), shared.CountDocumentsParams(
    filters=shared.CountDocumentsParamsHaystackFilters(),
    only_documents_without_embedding=False,
    use_prefiltering=False,
), 'excepturi', 'pariatur')

if res.dc_document_count is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                     | [operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostSecurity](../../models/operations/countdocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentscountpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                                                              |
| `count_documents_params`                                                                                                                                                                                                       | [shared.CountDocumentsParams](../../models/shared/countdocumentsparams.md)                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                            |
| `index_name`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                             | The name of the pipeline.                                                                                                                                                                                                      |
| `workspace_name`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                             | Type the name of the workspace.                                                                                                                                                                                                |


### Response

**[operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostResponse](../../models/operations/countdocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentscountpostresponse.md)**


## get

Displays the document content and its properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.document_store.get(operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetSecurity(
    http_bearer="",
), 'modi', 'praesentium', 'rem')

if res.deepset_cloud_document is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                           | [operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetSecurity](../../models/operations/getdocumentapiv1workspacesworkspacenameindexesindexnamedocumentsdocumentidgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                   | The security requirements to use for the request.                                                                                                                                                                    |
| `document_id`                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The identifier of the document. To obtain the ID, you can run the Get All Documents endpoint.                                                                                                                        |
| `index_name`                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The name of the pipeline used to process the documents.                                                                                                                                                              |
| `workspace_name`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | Type the name of the workspace.                                                                                                                                                                                      |


### Response

**[operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetResponse](../../models/operations/getdocumentapiv1workspacesworkspacenameindexesindexnamedocumentsdocumentidgetresponse.md)**


## list_document_streams

Returns all documents created for a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.document_store.list_document_streams(operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostSecurity(
    http_bearer="",
), shared.FetchDocumentsParams(
    filters=shared.FetchDocumentsParamsHaystackFilters(),
    return_embedding=False,
    use_prefiltering=False,
), 'voluptates', 'quasi')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                                                         | [operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostSecurity](../../models/operations/getalldocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsstreampostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                                                                  |
| `fetch_documents_params`                                                                                                                                                                                                           | [shared.FetchDocumentsParams](../../models/shared/fetchdocumentsparams.md)                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                |
| `index_name`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                 | The name of the pipeline.                                                                                                                                                                                                          |
| `workspace_name`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                 | Type the name of the workspace.                                                                                                                                                                                                    |


### Response

**[operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostResponse](../../models/operations/getalldocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsstreampostresponse.md)**


## list_documents

Displays all documents processed by the specified pipeline together with their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.document_store.list_documents(operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetSecurity(
    http_bearer="",
), 'repudiandae', 'sint', False)

if res.deepset_cloud_documents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                               | [operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetSecurity](../../models/operations/getalldocumentsapiv1workspacesworkspacenameindexesindexnamedocumentsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                                        |
| `index_name`                                                                                                                                                                                             | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | The name of the pipeline used to process the documents.                                                                                                                                                  |
| `workspace_name`                                                                                                                                                                                         | *str*                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                       | Type the name of the workspace.                                                                                                                                                                          |
| `return_embedding`                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | N/A                                                                                                                                                                                                      |


### Response

**[operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetResponse](../../models/operations/getalldocumentsapiv1workspacesworkspacenameindexesindexnamedocumentsgetresponse.md)**


## search

Searches the documents for the specified query.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.document_store.search(operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostSecurity(
    http_bearer="",
), shared.QueryDocumentsParams(
    all_terms_must_match=False,
    custom_query='veritatis',
    filters=shared.QueryDocumentsParamsHaystackFilters(),
    query='itaque',
    query_emb=[
        3185.69,
        93.56,
    ],
    return_embedding=False,
    top_k=667411,
    use_prefiltering=False,
), 'quibusdam', 'explicabo')

if res.deepset_cloud_documents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                     | [operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostSecurity](../../models/operations/querydocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsquerypostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                                                              |
| `query_documents_params`                                                                                                                                                                                                       | [shared.QueryDocumentsParams](../../models/shared/querydocumentsparams.md)                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                            |
| `index_name`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                             | The name of the pipeline.                                                                                                                                                                                                      |
| `workspace_name`                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                             | Type the name of the workspace.                                                                                                                                                                                                |


### Response

**[operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostResponse](../../models/operations/querydocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsquerypostresponse.md)**

