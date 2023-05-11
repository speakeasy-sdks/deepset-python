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
        status=shared.CloseSessionSessionCloseStatusEnumEnum.CLOSED,
    ),
    session_id='d4f9efc1-b451-42c1-8326-48dc2f615199',
    workspace_name='earum',
)

res = s.upload_session.close(req, operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
        write_mode=shared.CreateSessionFileWriteModeEnumEnum.FAIL,
    ),
    workspace_name='hic',
)

res = s.upload_session.create(req, operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    after='d0e9fe6c-632c-4a3a-ad01-17996312fde0',
    before='4771778f-f61d-4017-8763-60a15db6a660',
    ingestion_status=operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetIngestionStatusFileIngestionStatusEnumEnum.FAILED,
    limit=374753,
    page_number=614528,
    session_id='a1adeaab-5851-4d6c-a45b-08b61891baa0',
    workspace_name='sapiente',
)

res = s.upload_session.get_files(req, operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    session_id='e1ade008-e6f8-4c5f-b50d-8cdb5a341814',
    workspace_name='dolor',
)

res = s.upload_session.get_status(req, operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    after='01042181-3d52-408e-8e7e-253b668451c6',
    before='c6e205e1-6dea-4b3f-ac95-78a64584273a',
    is_expired=False,
    limit=514054,
    page_number=277340,
    workspace_name='quasi',
)

res = s.upload_session.list(req, operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.paginated_session is not None:
    # handle response
```
