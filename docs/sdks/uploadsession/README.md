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


res = s.upload_session.close(operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutSecurity(
    http_bearer="",
), close_session=shared.CloseSession(
    status=shared.CloseSessionSessionCloseStatusEnum.CLOSED,
), session_id='845f0597-a60f-4f2a-94a3-1e94764a3e86', workspace_name='nemo')

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                      | Type                                                                                                                                                                                           | Required                                                                                                                                                                                       | Description                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                     | [operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutSecurity](../../models/operations/closesessionapiv1workspacesworkspacenameuploadsessionssessionidputsecurity.md) | :heavy_check_mark:                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                              |
| `close_session`                                                                                                                                                                                | [shared.CloseSession](../../models/shared/closesession.md)                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                             | N/A                                                                                                                                                                                            |
| `session_id`                                                                                                                                                                                   | *str*                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                             | The ID of the session.                                                                                                                                                                         |
| `workspace_name`                                                                                                                                                                               | *str*                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                             | Type the name of the workspace.                                                                                                                                                                |


### Response

**[operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutResponse](../../models/operations/closesessionapiv1workspacesworkspacenameuploadsessionssessionidputresponse.md)**


## create

Creates a session for uploading files and file metadata. The session remains active for 24 hours. You can upload up to 10 000 files in a session.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.upload_session.create(operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostSecurity(
    http_bearer="",
), create_session=shared.CreateSession(
    write_mode=shared.CreateSessionFileWriteModeEnum.FAIL,
), workspace_name='esse')

if res.upload_session is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                   | [operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostSecurity](../../models/operations/createuploadsessionapiv1workspacesworkspacenameuploadsessionspostsecurity.md) | :heavy_check_mark:                                                                                                                                                                           | The security requirements to use for the request.                                                                                                                                            |
| `create_session`                                                                                                                                                                             | [shared.CreateSession](../../models/shared/createsession.md)                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                           | N/A                                                                                                                                                                                          |
| `workspace_name`                                                                                                                                                                             | *str*                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                           | Type the name of the workspace.                                                                                                                                                              |


### Response

**[operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostResponse](../../models/operations/createuploadsessionapiv1workspacesworkspacenameuploadsessionspostresponse.md)**


## get_files

Displays the file details of a session. Use this endpoint to check the status of the files in a session or the session expiration date.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetRequest(
    after='956f9251-a5a9-4da6-a0ff-57bfaad4f9ef',
    before='c1b4512c-1032-4648-9c2f-615199ebfd0e',
    ingestion_status=operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetIngestionStatusFileIngestionStatusEnum.FAILED,
    limit=983427,
    page_number=891801,
    session_id='6c632ca3-aed0-4117-9963-12fde0477177',
    workspace_name='praesentium',
)

res = s.upload_session.get_files(req, operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetSecurity(
    http_bearer="",
))

if res.paginated_session_file is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                                      | [operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetRequest](../../models/operations/getsessionfilesapiv1workspacesworkspacenameuploadsessionssessionidfilesgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                             | The request object to use for the request.                                                                                                                                                                     |
| `security`                                                                                                                                                                                                     | [operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetSecurity](../../models/operations/getsessionfilesapiv1workspacesworkspacenameuploadsessionssessionidfilesgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                                              |


### Response

**[operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetResponse](../../models/operations/getsessionfilesapiv1workspacesworkspacenameuploadsessionssessionidfilesgetresponse.md)**


## get_status

Displays the details of a session. Use this endpoint to check the status of the files in a session or the session expiration date.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.upload_session.get_status(operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetSecurity(
    http_bearer="",
), session_id='ff61d017-4763-460a-95db-6a660659a1ad', workspace_name='voluptates')

if res.session_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                             | [operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetSecurity](../../models/operations/getsessionstatusapiv1workspacesworkspacenameuploadsessionssessionidgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                                      |
| `session_id`                                                                                                                                                                                           | *str*                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                     | The ID of the session.                                                                                                                                                                                 |
| `workspace_name`                                                                                                                                                                                       | *str*                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                     | Type the name of the workspace.                                                                                                                                                                        |


### Response

**[operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetResponse](../../models/operations/getsessionstatusapiv1workspacesworkspacenameuploadsessionssessionidgetresponse.md)**


## list

Returns a list of all active upload sessions.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetRequest(
    after='aab5851d-6c64-45b0-8b61-891baa0fe1ad',
    before='e008e6f8-c5f3-450d-8cdb-5a3418143010',
    is_expired=False,
    limit=265039,
    page_number=144286,
    workspace_name='ab',
)

res = s.upload_session.list(req, operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetSecurity(
    http_bearer="",
))

if res.paginated_session is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                | [operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetRequest](../../models/operations/listuploadsessionsapiv1workspacesworkspacenameuploadsessionsgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                       | The request object to use for the request.                                                                                                                                               |
| `security`                                                                                                                                                                               | [operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetSecurity](../../models/operations/listuploadsessionsapiv1workspacesworkspacenameuploadsessionsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                       | The security requirements to use for the request.                                                                                                                                        |


### Response

**[operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetResponse](../../models/operations/listuploadsessionsapiv1workspacesworkspacenameuploadsessionsgetresponse.md)**

