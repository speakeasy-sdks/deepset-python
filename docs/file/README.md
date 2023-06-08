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
            'nihil',
            'sit',
            'expedita',
        ],
    ),
    workspace_name='neque',
)

res = s.file.delete_multi(req, operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteSecurity(
    http_bearer="",
))

if res.delete_files_api_v1_workspaces_workspace_name_files_delete_200_application_json_any is not None:
    # handle response
```

## delete_single

Removes the file from the workspace.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteRequest(
    file_id='26b5a734-29cd-4b1a-8422-bb679d232271',
    workspace_name='ullam',
)

res = s.file.delete_single(req, operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteSecurity(
    http_bearer="",
))

if res.delete_file_api_v1_workspaces_workspace_name_files_file_id_delete_200_application_json_any is not None:
    # handle response
```

## get

Retrieves the file contents.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetRequest(
    file_id='bf0cbb1e-31b8-4b90-b344-3a1108e0adcf',
    workspace_name='ut',
)

res = s.file.get(req, operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetSecurity(
    http_bearer="",
))

if res.get_file_api_v1_workspaces_workspace_name_files_file_id_get_200_application_json_any is not None:
    # handle response
```

## get_document

Returns all documents generated for a file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetRequest(
    file_id='b921879f-ce95-43f7-bef7-fbc7abd74dd3',
    workspace_name='natus',
)

res = s.file.get_document(req, operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetSecurity(
    http_bearer="",
))

if res.documents is not None:
    # handle response
```

## get_meta_data

Displays the metadata of a file.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetRequest(
    file_id='c0f5d2cf-f7c7-40a4-9626-d436813f16d9',
    workspace_name='voluptatibus',
)

res = s.file.get_meta_data(req, operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetSecurity(
    http_bearer="",
))

if res.response_get_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_get is not None:
    # handle response
```

## list

List files in a workspace. This endpoint supports pagination and filtering by name and metadata.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest(
    after_file_id='5fce6c55-6146-4c3e-a50f-b008c42e141a',
    after_value='laborum',
    content='placeat',
    field=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetFieldField.CREATED_AT,
    filter='eum',
    limit=420539,
    meta_key='nobis',
    meta_value='quas',
    name='Drew Hoeger I',
    order=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetOrderOrder.ASC,
    page_number=131482,
    workspace_name='provident',
)

res = s.file.list(req, operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetSecurity(
    http_bearer="",
))

if res.file_pagination is not None:
    # handle response
```

## update_meta_data

Updates the metadata of a file. You can modify existing metadata or add new ones. The metadata of the documents that were created
from this file will also be updated.

### Example Usage

```python
import deepset_cloud
from deepset_cloud.models import operations

s = deepset_cloud.DeepsetCloud()

req = operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutRequest(
    request_body={
        "molestiae": 'magnam',
    },
    file_id='74778a7b-d466-4d28-810a-b3cdca425190',
    workspace_name='tempora',
)

res = s.file.update_meta_data(req, operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutSecurity(
    http_bearer="",
))

if res.update_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_put_200_application_json_any is not None:
    # handle response
```

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
            file='debitis',
            content='ipsam'.encode(),
        ),
        meta='aspernatur',
        text='sequi',
    ),
    file_name='quo',
    workspace_name='esse',
    write_mode=operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostWriteModeFileWriteModeEnum.FAIL,
)

res = s.file.upload(req, operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostSecurity(
    http_bearer="",
))

if res.response_upload_file_api_v1_workspaces_workspace_name_files_post is not None:
    # handle response
```
