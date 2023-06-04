# upload_session

### Available Operations

* [close](#close) - Close Session
* [create](#create) - Create Upload Session
* [get_files](#get_files) - Get Session Files
* [get_status](#get_status) - Get Session Status
* [list](#list) - Get Upload Sessions

## close

Closes the session and starts the ingestion process.
If the session is not closed explicitly, the session will be automatically closed after 24 hours.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutRequest(
    close_session=shared.CloseSession(
        status=shared.CloseSessionSessionCloseStatusEnum.CLOSED,
    ),
    session_id='ad4f9efc-1b45-412c-9032-648dc2f61519',
    workspace_name='provident',
)

res = s.upload_session.close(req, operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.status_code == 200:
    # handle response
```

## create

Creates a session for uploading files and file metadata. The session remains active for 24 hours. You can upload up to 10 000 files in a session.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostRequest(
    create_session=shared.CreateSession(
        write_mode=shared.CreateSessionFileWriteModeEnum.FAIL,
    ),
    workspace_name='soluta',
)

res = s.upload_session.create(req, operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.upload_session is not None:
    # handle response
```

## get_files

Displays the file details of a session. Use this endpoint to check the status of the files in a session or the session expiration date.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetRequest(
    after='fd0e9fe6-c632-4ca3-aed0-117996312fde',
    before='04771778-ff61-4d01-b476-360a15db6a66',
    ingestion_status=operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetIngestionStatusFileIngestionStatusEnum.PENDING,
    limit=431760,
    page_number=374753,
    session_id='9a1adeaa-b585-41d6-8645-b08b61891baa',
    workspace_name='voluptatem',
)

res = s.upload_session.get_files(req, operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.paginated_session_file is not None:
    # handle response
```

## get_status

Displays the details of a session. Use this endpoint to check the status of the files in a session or the session expiration date.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetRequest(
    session_id='fe1ade00-8e6f-48c5-b350-d8cdb5a34181',
    workspace_name='tempora',
)

res = s.upload_session.get_status(req, operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.session_detail is not None:
    # handle response
```

## list

Returns a list of all active upload sessions.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetRequest(
    after='30104218-13d5-4208-ace7-e253b668451c',
    before='6c6e205e-16de-4ab3-bec9-578a64584273',
    is_expired=False,
    limit=681740,
    page_number=514054,
    workspace_name='incidunt',
)

res = s.upload_session.list(req, operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetSecurity(
    http_bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.paginated_session is not None:
    # handle response
```
