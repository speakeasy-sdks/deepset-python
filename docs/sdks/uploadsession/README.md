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
), shared.CloseSession(
    status=shared.CloseSessionSessionCloseStatusEnum.CLOSED,
), 'e94764a3-e865-4e79-96f9-251a5a9da660', 'repellat')

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
), shared.CreateSession(
    write_mode=shared.CreateSessionFileWriteModeEnum.FAIL,
), 'ullam')

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
    after='7bfaad4f-9efc-41b4-912c-1032648dc2f6',
    before='15199ebf-d0e9-4fe6-8632-ca3aed011799',
    ingestion_status=operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetIngestionStatusFileIngestionStatusEnum.FAILED,
    limit=241557,
    page_number=96562,
    session_id='2fde0477-1778-4ff6-9d01-7476360a15db',
    workspace_name='aliquid',
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
), 'a660659a-1ade-4aab-9851-d6c645b08b61', 'voluptatum')

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
    after='91baa0fe-1ade-4008-a6f8-c5f350d8cdb5',
    before='a3418143-0104-4218-93d5-208ece7e253b',
    is_expired=False,
    limit=432984,
    page_number=426943,
    workspace_name='voluptatum',
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
