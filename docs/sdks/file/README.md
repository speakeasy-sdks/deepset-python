# file

### Available Operations

* [delete_multi](#delete_multi) - Delete Files
* [delete_single](#delete_single) - Delete File
* [get](#get) - Get File
* [get_document](#get_document) - Get Document
* [get_meta_data](#get_meta_data) - Get File Meta
* [list](#list) - List Files
* [update_meta_data](#update_meta_data) - Update File Meta
* [upload](#upload) - Upload File

## delete_multi

Deletes files in a workspace. Deletes all files if no file_names provided.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteRequest(
    request_body=operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteFileNames(
        names=[
            'harum',
            'iusto',
        ],
    ),
    workspace_name='ipsum',
)

res = s.file.delete_multi(req, operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteSecurity(
    http_bearer="",
))

if res.delete_files_api_v1_workspaces_workspace_name_files_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteRequest](../../models/operations/deletefilesapiv1workspacesworkspacenamefilesdeleterequest.md)   | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |
| `security`                                                                                                                                                     | [operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteSecurity](../../models/operations/deletefilesapiv1workspacesworkspacenamefilesdeletesecurity.md) | :heavy_check_mark:                                                                                                                                             | The security requirements to use for the request.                                                                                                              |


### Response

**[operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteResponse](../../models/operations/deletefilesapiv1workspacesworkspacenamefilesdeleteresponse.md)**


## delete_single

Removes the file from the workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteRequest(
    file_id='cf3be453-f870-4b32-ab5a-73429cdb1a84',
    workspace_name='aspernatur',
)

res = s.file.delete_single(req, operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteSecurity(
    http_bearer="",
))

if res.delete_file_api_v1_workspaces_workspace_name_files_file_id_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                | [operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteRequest](../../models/operations/deletefileapiv1workspacesworkspacenamefilesfileiddeleterequest.md)   | :heavy_check_mark:                                                                                                                                                       | The request object to use for the request.                                                                                                                               |
| `security`                                                                                                                                                               | [operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteSecurity](../../models/operations/deletefileapiv1workspacesworkspacenamefilesfileiddeletesecurity.md) | :heavy_check_mark:                                                                                                                                                       | The security requirements to use for the request.                                                                                                                        |


### Response

**[operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteResponse](../../models/operations/deletefileapiv1workspacesworkspacenamefilesfileiddeleteresponse.md)**


## get

Retrieves the file contents.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetRequest(
    file_id='2bb679d2-3227-415b-b0cb-b1e31b8b90f3',
    workspace_name='dolore',
)

res = s.file.get(req, operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetSecurity(
    http_bearer="",
))

if res.get_file_api_v1_workspaces_workspace_name_files_file_id_get_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetRequest](../../models/operations/getfileapiv1workspacesworkspacenamefilesfileidgetrequest.md)   | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |
| `security`                                                                                                                                                   | [operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetSecurity](../../models/operations/getfileapiv1workspacesworkspacenamefilesfileidgetsecurity.md) | :heavy_check_mark:                                                                                                                                           | The security requirements to use for the request.                                                                                                            |


### Response

**[operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetResponse](../../models/operations/getfileapiv1workspacesworkspacenamefilesfileidgetresponse.md)**


## get_document

Returns all documents generated for a file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetRequest(
    file_id='43a1108e-0adc-4f4b-9218-79fce953f73e',
    workspace_name='tenetur',
)

res = s.file.get_document(req, operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetSecurity(
    http_bearer="",
))

if res.documents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                              | [operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetRequest](../../models/operations/getdocumentapiv1workspacesworkspacenamefilesfileiddocumentsgetrequest.md)   | :heavy_check_mark:                                                                                                                                                                     | The request object to use for the request.                                                                                                                                             |
| `security`                                                                                                                                                                             | [operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetSecurity](../../models/operations/getdocumentapiv1workspacesworkspacenamefilesfileiddocumentsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                      |


### Response

**[operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetResponse](../../models/operations/getdocumentapiv1workspacesworkspacenamefilesfileiddocumentsgetresponse.md)**


## get_meta_data

Displays the metadata of a file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetRequest(
    file_id='7fbc7abd-74dd-439c-8f5d-2cff7c70a456',
    workspace_name='aspernatur',
)

res = s.file.get_meta_data(req, operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetSecurity(
    http_bearer="",
))

if res.response_get_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetRequest](../../models/operations/getfilemetaapiv1workspacesworkspacenamefilesfileidmetagetrequest.md)   | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |
| `security`                                                                                                                                                                   | [operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetSecurity](../../models/operations/getfilemetaapiv1workspacesworkspacenamefilesfileidmetagetsecurity.md) | :heavy_check_mark:                                                                                                                                                           | The security requirements to use for the request.                                                                                                                            |


### Response

**[operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetResponse](../../models/operations/getfilemetaapiv1workspacesworkspacenamefilesfileidmetagetresponse.md)**


## list

List files in a workspace. This endpoint supports pagination and filtering by name and metadata.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest(
    after_file_id='6d436813-f16d-49f5-bce6-c556146c3e25',
    after_value='eaque',
    content='a',
    field=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetFieldField.NAME,
    filter='aut',
    limit=11427,
    meta_key='deleniti',
    meta_value='impedit',
    name='Mrs. Denise Tillman MD',
    order=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetOrderOrder.DESC,
    page_number=810424,
    workspace_name='velit',
)

res = s.file.list(req, operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetSecurity(
    http_bearer="",
))

if res.file_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                            | Type                                                                                                                                                 | Required                                                                                                                                             | Description                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                            | [operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest](../../models/operations/listfilesapiv1workspacesworkspacenamefilesgetrequest.md)   | :heavy_check_mark:                                                                                                                                   | The request object to use for the request.                                                                                                           |
| `security`                                                                                                                                           | [operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetSecurity](../../models/operations/listfilesapiv1workspacesworkspacenamefilesgetsecurity.md) | :heavy_check_mark:                                                                                                                                   | The security requirements to use for the request.                                                                                                    |


### Response

**[operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetResponse](../../models/operations/listfilesapiv1workspacesworkspacenamefilesgetresponse.md)**


## update_meta_data

Updates the metadata of a file. You can modify existing metadata or add new ones. The metadata of the documents that were created
from this file will also be updated.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutRequest(
    request_body=operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutMeta(),
    file_id='66c8dd6b-1442-4907-8747-78a7bd466d28',
    workspace_name='quisquam',
)

res = s.file.update_meta_data(req, operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutSecurity(
    http_bearer="",
))

if res.update_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_put_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                          | [operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutRequest](../../models/operations/updatefilemetaapiv1workspacesworkspacenamefilesfileidmetaputrequest.md)   | :heavy_check_mark:                                                                                                                                                                 | The request object to use for the request.                                                                                                                                         |
| `security`                                                                                                                                                                         | [operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutSecurity](../../models/operations/updatefilemetaapiv1workspacesworkspacenamefilesfileidmetaputsecurity.md) | :heavy_check_mark:                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                  |


### Response

**[operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutResponse](../../models/operations/updatefilemetaapiv1workspacesworkspacenamefilesfileidmetaputresponse.md)**


## upload

Uploads a file into the workspace. You can also use this endpoint to create a text file. To do that, enter the file name and text as its contents.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()

req = operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostRequest(
    body_upload_file_api_v1_workspaces_workspace_name_files_post=shared.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPost(
        file=shared.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPostFile(
            file='veritatis',
            content='ipsa'.encode(),
        ),
        meta='id',
        text='quidem',
    ),
    file_name='neque',
    workspace_name='quo',
    write_mode=operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostWriteModeFileWriteModeEnum.FAIL,
)

res = s.file.upload(req, operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostSecurity(
    http_bearer="",
))

if res.response_upload_file_api_v1_workspaces_workspace_name_files_post is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostRequest](../../models/operations/uploadfileapiv1workspacesworkspacenamefilespostrequest.md)   | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |
| `security`                                                                                                                                               | [operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostSecurity](../../models/operations/uploadfileapiv1workspacesworkspacenamefilespostsecurity.md) | :heavy_check_mark:                                                                                                                                       | The security requirements to use for the request.                                                                                                        |


### Response

**[operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostResponse](../../models/operations/uploadfileapiv1workspacesworkspacenamefilespostresponse.md)**

