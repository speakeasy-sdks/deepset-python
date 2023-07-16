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


res = s.file.delete_multi(operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteSecurity(
    http_bearer="",
), 'esse', operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteFileNames(
    names=[
        'iusto',
        'ipsum',
        'quisquam',
    ],
))

if res.delete_files_api_v1_workspaces_workspace_name_files_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                 | [operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteSecurity](../../models/operations/deletefilesapiv1workspacesworkspacenamefilesdeletesecurity.md)             | :heavy_check_mark:                                                                                                                                                         | The security requirements to use for the request.                                                                                                                          |
| `workspace_name`                                                                                                                                                           | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | Type the name of the workspace.                                                                                                                                            |
| `request_body`                                                                                                                                                             | [Optional[operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteFileNames]](../../models/operations/deletefilesapiv1workspacesworkspacenamefilesdeletefilenames.md) | :heavy_minus_sign:                                                                                                                                                         | N/A                                                                                                                                                                        |


### Response

**[operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteResponse](../../models/operations/deletefilesapiv1workspacesworkspacenamefilesdeleteresponse.md)**


## delete_single

Removes the file from the workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.file.delete_single(operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteSecurity(
    http_bearer="",
), 'f3be453f-870b-4326-b5a7-3429cdb1a842', 'dolores')

if res.delete_file_api_v1_workspaces_workspace_name_files_file_id_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                               | [operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteSecurity](../../models/operations/deletefileapiv1workspacesworkspacenamefilesfileiddeletesecurity.md) | :heavy_check_mark:                                                                                                                                                       | The security requirements to use for the request.                                                                                                                        |
| `file_id`                                                                                                                                                                | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | N/A                                                                                                                                                                      |
| `workspace_name`                                                                                                                                                         | *str*                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                       | Type the name of the workspace.                                                                                                                                          |


### Response

**[operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteResponse](../../models/operations/deletefileapiv1workspacesworkspacenamefilesfileiddeleteresponse.md)**


## get

Retrieves the file contents.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.file.get(operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetSecurity(
    http_bearer="",
), 'bb679d23-2271-45bf-8cbb-1e31b8b90f34', 'labore')

if res.get_file_api_v1_workspaces_workspace_name_files_file_id_get_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                   | [operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetSecurity](../../models/operations/getfileapiv1workspacesworkspacenamefilesfileidgetsecurity.md) | :heavy_check_mark:                                                                                                                                           | The security requirements to use for the request.                                                                                                            |
| `file_id`                                                                                                                                                    | *str*                                                                                                                                                        | :heavy_check_mark:                                                                                                                                           | N/A                                                                                                                                                          |
| `workspace_name`                                                                                                                                             | *str*                                                                                                                                                        | :heavy_check_mark:                                                                                                                                           | Type the name of the workspace.                                                                                                                              |


### Response

**[operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetResponse](../../models/operations/getfileapiv1workspacesworkspacenamefilesfileidgetresponse.md)**


## get_document

Returns all documents generated for a file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.file.get_document(operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetSecurity(
    http_bearer="",
), '3a1108e0-adcf-44b9-a187-9fce953f73ef', 'dignissimos')

if res.documents is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                             | [operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetSecurity](../../models/operations/getdocumentapiv1workspacesworkspacenamefilesfileiddocumentsgetsecurity.md) | :heavy_check_mark:                                                                                                                                                                     | The security requirements to use for the request.                                                                                                                                      |
| `file_id`                                                                                                                                                                              | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | N/A                                                                                                                                                                                    |
| `workspace_name`                                                                                                                                                                       | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | Type the name of the workspace.                                                                                                                                                        |


### Response

**[operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetResponse](../../models/operations/getdocumentapiv1workspacesworkspacenamefilesfileiddocumentsgetresponse.md)**


## get_meta_data

Displays the metadata of a file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()


res = s.file.get_meta_data(operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetSecurity(
    http_bearer="",
), 'fbc7abd7-4dd3-49c0-b5d2-cff7c70a4562', 'vel')

if res.response_get_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                   | [operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetSecurity](../../models/operations/getfilemetaapiv1workspacesworkspacenamefilesfileidmetagetsecurity.md) | :heavy_check_mark:                                                                                                                                                           | The security requirements to use for the request.                                                                                                                            |
| `file_id`                                                                                                                                                                    | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | N/A                                                                                                                                                                          |
| `workspace_name`                                                                                                                                                             | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | Type the name of the workspace.                                                                                                                                              |


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
    after_file_id='d436813f-16d9-4f5f-8e6c-556146c3e250',
    after_value='a',
    content='libero',
    field=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetFieldField.CREATED_AT,
    filter='aut',
    limit=533466,
    meta_key='impedit',
    meta_value='aliquam',
    name='Eloise Block MD',
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


res = s.file.update_meta_data(operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutSecurity(
    http_bearer="",
), operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutMeta(), '66c8dd6b-1442-4907-8747-78a7bd466d28', 'quisquam')

if res.update_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_put_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                         | [operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutSecurity](../../models/operations/updatefilemetaapiv1workspacesworkspacenamefilesfileidmetaputsecurity.md) | :heavy_check_mark:                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                  |
| `request_body`                                                                                                                                                                     | [operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutMeta](../../models/operations/updatefilemetaapiv1workspacesworkspacenamefilesfileidmetaputmeta.md)         | :heavy_check_mark:                                                                                                                                                                 | N/A                                                                                                                                                                                |
| `file_id`                                                                                                                                                                          | *str*                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                 | N/A                                                                                                                                                                                |
| `workspace_name`                                                                                                                                                                   | *str*                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                 | Type the name of the workspace.                                                                                                                                                    |


### Response

**[operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutResponse](../../models/operations/updatefilemetaapiv1workspacesworkspacenamefilesfileidmetaputresponse.md)**


## upload

Uploads a file into the workspace. You can also use this endpoint to create a text file. To do that, enter the file name and text as its contents.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud()


res = s.file.upload(operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostSecurity(
    http_bearer="",
), 'veritatis', shared.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPost(
    file=shared.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPostFile(
        file='ipsa',
        content='id'.encode(),
    ),
    meta='quidem',
    text='neque',
), 'quo', operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostWriteModeFileWriteModeEnum.FAIL)

if res.response_upload_file_api_v1_workspaces_workspace_name_files_post is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                                                                                                                                                                                                         | [operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostSecurity](../../models/operations/uploadfileapiv1workspacesworkspacenamefilespostsecurity.md)                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                 | The security requirements to use for the request.                                                                                                                                                                                                                                                                  |
| `workspace_name`                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                 | Type the name of the workspace.                                                                                                                                                                                                                                                                                    |
| `body_upload_file_api_v1_workspaces_workspace_name_files_post`                                                                                                                                                                                                                                                     | [Optional[shared.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPost]](../../models/shared/bodyuploadfileapiv1workspacesworkspacenamefilespost.md)                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                |
| `file_name`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                 | How do you want to call your file? Use this field only if you're creating a file to upload. If you're uploading a ready file, leave this field empty.                                                                                                                                                              |
| `write_mode`                                                                                                                                                                                                                                                                                                       | [Optional[operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostWriteModeFileWriteModeEnum]](../../models/operations/uploadfileapiv1workspacesworkspacenamefilespostwritemodefilewritemodeenum.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                 | The write mode determines how to handle uploading a file if it's already in the workspace. Your options are: keep the file with the same name, make the request fail if a file with the same name already exists, or overwrite the file. If you choose to overwrite, all files with the same name are overwritten. |


### Response

**[operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostResponse](../../models/operations/uploadfileapiv1workspacesworkspacenamefilespostresponse.md)**

