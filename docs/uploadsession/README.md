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
    session_id='e3ab8845-f059-47a6-8ff2-a54a31e94764',
    workspace_name='culpa',
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
        write_mode=shared.CreateSessionFileWriteModeEnumEnum.KEEP,
    ),
    workspace_name='debitis',
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
    after='865e7956-f925-41a5-a9da-660ff57bfaad',
    before='4f9efc1b-4512-4c10-b264-8dc2f615199e',
    ingestion_status=operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetIngestionStatusFileIngestionStatusEnumEnum.FINISHED,
    limit=940782,
    page_number=848151,
    session_id='0e9fe6c6-32ca-43ae-9011-7996312fde04',
    workspace_name='nihil',
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
    session_id='71778ff6-1d01-4747-a360-a15db6a66065',
    workspace_name='iste',
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
    after='a1adeaab-5851-4d6c-a45b-08b61891baa0',
    before='fe1ade00-8e6f-48c5-b350-d8cdb5a34181',
    is_expired=False,
    limit=274575,
    page_number=221396,
    workspace_name='consequatur',
)

res = s.upload_session.list(req, operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.paginated_session is not None:
    # handle response
```
