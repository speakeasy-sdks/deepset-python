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
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.document_store is not None:
    # handle response
```

## count_documents

Returns the number of documents for a pipeline. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostRequest(
    count_documents_params=shared.CountDocumentsParams(
        filters={
            "pariatur": 'modi',
            "praesentium": 'rem',
            "voluptates": 'quasi',
        },
        only_documents_without_embedding=False,
        use_prefiltering=False,
    ),
    index_name='repudiandae',
    workspace_name='sint',
)

res = s.document_store.count_documents(req, operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.dc_document_count is not None:
    # handle response
```

## get

Displays the document content and its properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetRequest(
    document_id='veritatis',
    index_name='itaque',
    workspace_name='incidunt',
)

res = s.document_store.get(req, operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.deepset_cloud_document is not None:
    # handle response
```

## list_document_streams

Returns all documents created for a pipeline.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostRequest(
    fetch_documents_params=shared.FetchDocumentsParams(
        filters={
            "consequatur": 'est',
            "quibusdam": 'explicabo',
        },
        return_embedding=False,
        use_prefiltering=False,
    ),
    index_name='deserunt',
    workspace_name='distinctio',
)

res = s.document_store.list_document_streams(req, operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## list_documents

Displays all documents processed by the specified pipeline together with their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetRequest(
    index_name='quibusdam',
    return_embedding=False,
    workspace_name='labore',
)

res = s.document_store.list_documents(req, operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.deepset_cloud_documents is not None:
    # handle response
```

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
        custom_query='modi',
        filters={
            "aliquid": 'cupiditate',
        },
        query='quos',
        query_emb=[
            1649.4,
        ],
        return_embedding=False,
        top_k=828940,
        use_prefiltering=False,
    ),
    index_name='ipsam',
    workspace_name='alias',
)

res = s.document_store.search(req, operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.deepset_cloud_documents is not None:
    # handle response
```
