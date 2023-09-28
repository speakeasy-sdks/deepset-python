# File
(*file*)

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
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.file.delete_multi(workspace_name='cupiditate', request_body=operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteFileNames(
    names=[
        'aperiam',
    ],
))

if res.delete_files_api_v1_workspaces_workspace_name_files_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `workspace_name`                                                                                                                                                           | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | Type the name of the workspace.                                                                                                                                            |
| `request_body`                                                                                                                                                             | [Optional[operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteFileNames]](../../models/operations/deletefilesapiv1workspacesworkspacenamefilesdeletefilenames.md) | :heavy_minus_sign:                                                                                                                                                         | N/A                                                                                                                                                                        |


### Response

**[operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteResponse](../../models/operations/deletefilesapiv1workspacesworkspacenamefilesdeleteresponse.md)**


## delete_single

Removes the file from the workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.file.delete_single(file_id='f3443a11-08e0-4adc-b4b9-21879fce953f', workspace_name='voluptate')

if res.delete_file_api_v1_workspaces_workspace_name_files_file_id_delete_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `file_id`                       | *str*                           | :heavy_check_mark:              | N/A                             |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteResponse](../../models/operations/deletefileapiv1workspacesworkspacenamefilesfileiddeleteresponse.md)**


## get

Retrieves the file contents.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.file.get(file_id='3ef7fbc7-abd7-44dd-b9c0-f5d2cff7c70a', workspace_name='tempora')

if res.get_file_api_v1_workspaces_workspace_name_files_file_id_get_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `file_id`                       | *str*                           | :heavy_check_mark:              | N/A                             |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetResponse](../../models/operations/getfileapiv1workspacesworkspacenamefilesfileidgetresponse.md)**


## get_document

Returns all documents generated for a file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.file.get_document(file_id='5626d436-813f-416d-9f5f-ce6c556146c3', workspace_name='recusandae')

if res.documents is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `file_id`                       | *str*                           | :heavy_check_mark:              | N/A                             |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetResponse](../../models/operations/getdocumentapiv1workspacesworkspacenamefilesfileiddocumentsgetresponse.md)**


## get_meta_data

Displays the metadata of a file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.file.get_meta_data(file_id='250fb008-c42e-4141-aac3-66c8dd6b1442', workspace_name='provident')

if res.response_get_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_get is not None:
    # handle response
```

### Parameters

| Parameter                       | Type                            | Required                        | Description                     |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `file_id`                       | *str*                           | :heavy_check_mark:              | N/A                             |
| `workspace_name`                | *str*                           | :heavy_check_mark:              | Type the name of the workspace. |


### Response

**[operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetResponse](../../models/operations/getfilemetaapiv1workspacesworkspacenamefilesfileidmetagetresponse.md)**


## list

List files in a workspace. This endpoint supports pagination and filtering by name and metadata.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)

req = operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest(
    after_file_id='07474778-a7bd-4466-928c-10ab3cdca425',
    after_value='ab',
    content='cupiditate',
    field=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetFieldField.CREATED_AT,
    filter='tempora',
    limit=892050,
    meta_key='ipsam',
    meta_value='aspernatur',
    name='Angelica Koelpin MD',
    order=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetOrderOrder.DESC,
    page_number=490819,
    workspace_name='inventore',
)

res = s.file.list(req)

if res.file_pagination is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest](../../models/operations/listfilesapiv1workspacesworkspacenamefilesgetrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetResponse](../../models/operations/listfilesapiv1workspacesworkspacenamefilesgetresponse.md)**


## update_meta_data

Updates the metadata of a file. You can modify existing metadata or add new ones. The metadata of the documents that were created
from this file will also be updated.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.file.update_meta_data(request_body=operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutMeta(), file_id='78e4796f-2a70-4c68-8282-aa482562f222', workspace_name='saepe')

if res.update_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_put_200_application_json_any is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                                             | [operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutMeta](../../models/operations/updatefilemetaapiv1workspacesworkspacenamefilesfileidmetaputmeta.md) | :heavy_check_mark:                                                                                                                                                         | N/A                                                                                                                                                                        |
| `file_id`                                                                                                                                                                  | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | N/A                                                                                                                                                                        |
| `workspace_name`                                                                                                                                                           | *str*                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                         | Type the name of the workspace.                                                                                                                                            |


### Response

**[operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutResponse](../../models/operations/updatefilemetaapiv1workspacesworkspacenamefilesfileidmetaputresponse.md)**


## upload

Uploads a file into the workspace. You can also use this endpoint to create a text file. To do that, enter the file name and text as its contents.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations, shared

s = deepset_cloud.DeepsetCloud(
    security=shared.Security(
        http_bearer="",
    ),
)


res = s.file.upload(workspace_name='occaecati', body_upload_file_api_v1_workspaces_workspace_name_files_post=shared.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPost(
    file=shared.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPostFile(
        file='atque',
        content='et'.encode(),
    ),
    meta='esse',
    text='eveniet',
), file_name='accusamus', write_mode=operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostWriteModeFileWriteModeEnum.KEEP)

if res.response_upload_file_api_v1_workspaces_workspace_name_files_post is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                          | Type                                                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `workspace_name`                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                                                 | Type the name of the workspace.                                                                                                                                                                                                                                                                                    |
| `body_upload_file_api_v1_workspaces_workspace_name_files_post`                                                                                                                                                                                                                                                     | [Optional[shared.BodyUploadFileAPIV1WorkspacesWorkspaceNameFilesPost]](../../models/shared/bodyuploadfileapiv1workspacesworkspacenamefilespost.md)                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                                                |
| `file_name`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                 | How do you want to call your file? Use this field only if you're creating a file to upload. If you're uploading a ready file, leave this field empty.                                                                                                                                                              |
| `write_mode`                                                                                                                                                                                                                                                                                                       | [Optional[operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostWriteModeFileWriteModeEnum]](../../models/operations/uploadfileapiv1workspacesworkspacenamefilespostwritemodefilewritemodeenum.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                 | The write mode determines how to handle uploading a file if it's already in the workspace. Your options are: keep the file with the same name, make the request fail if a file with the same name already exists, or overwrite the file. If you choose to overwrite, all files with the same name are overwritten. |


### Response

**[operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostResponse](../../models/operations/uploadfileapiv1workspacesworkspacenamefilespostresponse.md)**

