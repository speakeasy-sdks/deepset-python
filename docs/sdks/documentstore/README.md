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

req = operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetRequest(
    index_name='quidem',
    workspace_name='molestias',
)

res = s.document_store.check_connection(req, operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetSecurity(
    http_bearer="",
))

if res.document_store is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                              | [operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetRequest](../../models/operations/checkconnectionapiv1workspacesworkspacenameindexesindexnamegetrequest.md)   | :heavy_check_mark:                                                                                                                                                                     | The request object to use for the request.                                                                                                                                             |
| `security`                                                                                                                                                                             | [operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetSecurity](../../models/operations/checkconnectionapiv1workspacesworkspacenameindexesindexnamegetsecurity.md) | :heavy_check_mark:                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                      |


### Response

**[operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetResponse](../../models/operations/checkconnectionapiv1workspacesworkspacenameindexesindexnamegetresponse.md)**


## count_documents

Returns the number of documents for a pipeline. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostRequest(
    count_documents_params=shared.CountDocumentsParams(
        filters=shared.CountDocumentsParamsHaystackFilters(),
        only_documents_without_embedding=False,
        use_prefiltering=False,
    ),
    index_name='excepturi',
    workspace_name='pariatur',
)

res = s.document_store.count_documents(req, operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostSecurity(
    http_bearer="",
))

if res.dc_document_count is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                                      | [operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostRequest](../../models/operations/countdocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentscountpostrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                             | The request object to use for the request.                                                                                                                                                                                     |
| `security`                                                                                                                                                                                                                     | [operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostSecurity](../../models/operations/countdocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentscountpostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                                                              |


### Response

**[operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostResponse](../../models/operations/countdocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentscountpostresponse.md)**


## get

Displays the document content and its properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetRequest(
    document_id='modi',
    index_name='praesentium',
    workspace_name='rem',
)

res = s.document_store.get(req, operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetSecurity(
    http_bearer="",
))

if res.deepset_cloud_document is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                            | [operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetRequest](../../models/operations/getdocumentapiv1workspacesworkspacenameindexesindexnamedocumentsdocumentidgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                   | The request object to use for the request.                                                                                                                                                                           |
| `security`                                                                                                                                                                                                           | [operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetSecurity](../../models/operations/getdocumentapiv1workspacesworkspacenameindexesindexnamedocumentsdocumentidgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                   | The security requirements to use for the request.                                                                                                                                                                    |


### Response

**[operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetResponse](../../models/operations/getdocumentapiv1workspacesworkspacenameindexesindexnamedocumentsdocumentidgetresponse.md)**


## list_document_streams

Returns all documents created for a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostRequest(
    fetch_documents_params=shared.FetchDocumentsParams(
        filters=shared.FetchDocumentsParamsHaystackFilters(),
        return_embedding=False,
        use_prefiltering=False,
    ),
    index_name='voluptates',
    workspace_name='quasi',
)

res = s.document_store.list_document_streams(req, operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostSecurity(
    http_bearer="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                                          | [operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostRequest](../../models/operations/getalldocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsstreampostrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                                 | The request object to use for the request.                                                                                                                                                                                         |
| `security`                                                                                                                                                                                                                         | [operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostSecurity](../../models/operations/getalldocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsstreampostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                                                                  |


### Response

**[operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostResponse](../../models/operations/getalldocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsstreampostresponse.md)**


## list_documents

Displays all documents processed by the specified pipeline together with their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetRequest(
    index_name='repudiandae',
    return_embedding=False,
    workspace_name='sint',
)

res = s.document_store.list_documents(req, operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetSecurity(
    http_bearer="",
))

if res.deepset_cloud_documents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                | [operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetRequest](../../models/operations/getalldocumentsapiv1workspacesworkspacenameindexesindexnamedocumentsgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                       | The request object to use for the request.                                                                                                                                                               |
| `security`                                                                                                                                                                                               | [operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetSecurity](../../models/operations/getalldocumentsapiv1workspacesworkspacenameindexesindexnamedocumentsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                                        |


### Response

**[operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetResponse](../../models/operations/getalldocumentsapiv1workspacesworkspacenameindexesindexnamedocumentsgetresponse.md)**


## search

Searches the documents for the specified query.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostRequest(
    query_documents_params=shared.QueryDocumentsParams(
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
    ),
    index_name='quibusdam',
    workspace_name='explicabo',
)

res = s.document_store.search(req, operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostSecurity(
    http_bearer="",
))

if res.deepset_cloud_documents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                                      | [operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostRequest](../../models/operations/querydocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsquerypostrequest.md)   | :heavy_check_mark:                                                                                                                                                                                                             | The request object to use for the request.                                                                                                                                                                                     |
| `security`                                                                                                                                                                                                                     | [operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostSecurity](../../models/operations/querydocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsquerypostsecurity.md) | :heavy_check_mark:                                                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                                                              |


### Response

**[operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostResponse](../../models/operations/querydocumentsstreamapiv1workspacesworkspacenameindexesindexnamedocumentsquerypostresponse.md)**

