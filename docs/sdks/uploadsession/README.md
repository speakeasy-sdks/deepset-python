# UploadSession
(*upload_session*)

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

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.upload_session.close(close_session=shared.CloseSession(), session_id='858bd1fe-535f-4534-856e-5d2a350c163f', workspace_name='lightly')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `close_session`                                            | [shared.CloseSession](../../models/shared/closesession.md) | :heavy_check_mark:                                         | N/A                                                        |
| `session_id`                                               | *str*                                                      | :heavy_check_mark:                                         | The ID of the session.                                     |
| `workspace_name`                                           | *str*                                                      | :heavy_check_mark:                                         | Type the name of the workspace.                            |


### Response

**[operations.CloseSessionAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDPutResponse](../../models/operations/closesessionapiv1workspacesworkspacenameuploadsessionssessionidputresponse.md)**


## create

Creates a session for uploading files and file metadata. The session remains active for 24 hours. You can upload up to 10 000 files in a session.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.upload_session.create(create_session=shared.CreateSession(), workspace_name='online')

if res.upload_session is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `create_session`                                             | [shared.CreateSession](../../models/shared/createsession.md) | :heavy_check_mark:                                           | N/A                                                          |
| `workspace_name`                                             | *str*                                                        | :heavy_check_mark:                                           | Type the name of the workspace.                              |


### Response

**[operations.CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostResponse](../../models/operations/createuploadsessionapiv1workspacesworkspacenameuploadsessionspostresponse.md)**


## get_files

Displays the file details of a session. Use this endpoint to check the status of the files in a session or the session expiration date.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetRequest(
    session_id='a693fbb2-e996-4d93-8cbc-082b8e9824c8',
    workspace_name='Northeast Samoa',
)

res = s.upload_session.get_files(req)

if res.paginated_session_file is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                                                    | Type                                                                                                                                                                                                         | Required                                                                                                                                                                                                     | Description                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                                                    | [operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetRequest](../../models/operations/getsessionfilesapiv1workspacesworkspacenameuploadsessionssessionidfilesgetrequest.md) | :heavy_check_mark:                                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                                   |


### Response

**[operations.GetSessionFilesAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDFilesGetResponse](../../models/operations/getsessionfilesapiv1workspacesworkspacenameuploadsessionssessionidfilesgetresponse.md)**


## get_status

Displays the details of a session. Use this endpoint to check the status of the files in a session or the session expiration date.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)


res = s.upload_session.get_status(session_id='7b8c13f1-f508-4288-9a9d-4f095d2fd2e9', workspace_name='worth')

if res.session_detail is not None:
    # handle response
    pass
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `session_id`                    | *str*                           | :heavy_check_mark:              | The ID of the session.          |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.GetSessionStatusAPIV1WorkspacesWorkspaceNameUploadSessionsSessionIDGetResponse](../../models/operations/getsessionstatusapiv1workspacesworkspacenameuploadsessionssessionidgetresponse.md)**


## list

Returns a list of all active upload sessions.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    http_bearer="",
)

req = operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetRequest(
    workspace_name='Northeast Metal Canada',
)

res = s.upload_session.list(req)

if res.paginated_session is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                              | [operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetRequest](../../models/operations/listuploadsessionsapiv1workspacesworkspacenameuploadsessionsgetrequest.md) | :heavy_check_mark:                                                                                                                                                                     | The request object to use for the request.                                                                                                                                             |


### Response

**[operations.ListUploadSessionsAPIV1WorkspacesWorkspaceNameUploadSessionsGetResponse](../../models/operations/listuploadsessionsapiv1workspacesworkspacenameuploadsessionsgetresponse.md)**

