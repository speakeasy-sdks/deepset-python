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
    session_id='e94764a3-e865-4e79-96f9-251a5a9da660',
    workspace_name='repellat',
)

res = s.upload_session.close(req, operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutSecurity(
    http_bearer="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                      | Type                                                                                                                                                                                           | Required                                                                                                                                                                                       | Description                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                      | [operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutRequest](../../models/operations/closesessionapiv1workspacesworkspacenameuploadsessionssessionidputrequest.md)   | :heavy_check_mark:                                                                                                                                                                             | The request object to use for the request.                                                                                                                                                     |
| `security`                                                                                                                                                                                     | [operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutSecurity](../../models/operations/closesessionapiv1workspacesworkspacenameuploadsessionssessionidputsecurity.md) | :heavy_check_mark:                                                                                                                                                                             | The security requirements to use for the request.                                                                                                                                              |


### Response

**[operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutResponse](../../models/operations/closesessionapiv1workspacesworkspacenameuploadsessionssessionidputresponse.md)**


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
    workspace_name='ullam',
)

res = s.upload_session.create(req, operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostSecurity(
    http_bearer="",
))

if res.upload_session is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                    | [operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostRequest](../../models/operations/createuploadsessionapiv1workspacesworkspacenameuploadsessionspostrequest.md)   | :heavy_check_mark:                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                   |
| `security`                                                                                                                                                                                   | [operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostSecurity](../../models/operations/createuploadsessionapiv1workspacesworkspacenameuploadsessionspostsecurity.md) | :heavy_check_mark:                                                                                                                                                                           | The security requirements to use for the request.                                                                                                                                            |


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

req = operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetRequest(
    session_id='a660659a-1ade-4aab-9851-d6c645b08b61',
    workspace_name='voluptatum',
)

res = s.upload_session.get_status(req, operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetSecurity(
    http_bearer="",
))

if res.session_detail is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                              | [operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetRequest](../../models/operations/getsessionstatusapiv1workspacesworkspacenameuploadsessionssessionidgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                                     | The request object to use for the request.                                                                                                                                                             |
| `security`                                                                                                                                                                                             | [operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetSecurity](../../models/operations/getsessionstatusapiv1workspacesworkspacenameuploadsessionssessionidgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                                      |


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

