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
            'quidem',
            'voluptatibus',
            'voluptas',
            'natus',
        ],
    ),
    workspace_name='eos',
)

res = s.file.delete_multi(req, operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    file_id='80d1ba77-a89e-4bf7-b7ae-4203ce5e6a95',
    workspace_name='repellendus',
)

res = s.file.delete_single(req, operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    file_id='8a0d446c-e2af-47a7-bcf3-be453f870b32',
    workspace_name='vel',
)

res = s.file.get(req, operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    file_id='b5a73429-cdb1-4a84-a2bb-679d2322715b',
    workspace_name='hic',
)

res = s.file.get_document(req, operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    file_id='0cbb1e31-b8b9-40f3-843a-1108e0adcf4b',
    workspace_name='cupiditate',
)

res = s.file.get_meta_data(req, operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
    after_file_id='21879fce-953f-473e-b7fb-c7abd74dd39c',
    after_value='aut',
    content='voluptatibus',
    field=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetFieldFieldEnum.CREATED_AT,
    filter='nulla',
    limit=148141,
    meta_key='porro',
    meta_value='maiores',
    name='Ted Romaguera MD',
    order=operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetOrderOrderEnum.ASC,
    page_number=368584,
    workspace_name='ea',
)

res = s.file.list(req, operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
        "vel": 'possimus',
    },
    file_id='436813f1-6d9f-45fc-a6c5-56146c3e250f',
    workspace_name='libero',
)

res = s.file.update_meta_data(req, operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
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
            file='aut',
            content='aut'.encode(),
        ),
        meta='deleniti',
        text='impedit',
    ),
    file_name='aliquam',
    workspace_name='fugit',
    write_mode=operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostWriteModeFileWriteModeEnumEnum.FAIL,
)

res = s.file.upload(req, operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostSecurity(
    http_bearer="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.response_upload_file_api_v1_workspaces_workspace_name_files_post is not None:
    # handle response
```
