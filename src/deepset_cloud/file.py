"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from deepset_cloud.models import operations, shared
from typing import Any, Optional

class File:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def delete_multi(self, request: operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteRequest, security: operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteSecurity) -> operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteResponse:
        r"""Delete Files
        Deletes files in a workspace. Deletes all files if no file_names provided.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteRequest, base_url, '/api/v1/workspaces/{workspace_name}/files', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteFilesAPIV1WorkspacesWorkspaceNameFilesDeleteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_files_api_v1_workspaces_workspace_name_files_delete_200_application_json_any = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def delete_single(self, request: operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteRequest, security: operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteSecurity) -> operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteResponse:
        r"""Delete File
        Removes the file from the workspace.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteRequest, base_url, '/api/v1/workspaces/{workspace_name}/files/{file_id}', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteFileAPIV1WorkspacesWorkspaceNameFilesFileIDDeleteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.delete_file_api_v1_workspaces_workspace_name_files_file_id_delete_200_application_json_any = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def get(self, request: operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetRequest, security: operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetSecurity) -> operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetResponse:
        r"""Get File
        Retrieves the file contents.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/files/{file_id}', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetFileAPIV1WorkspacesWorkspaceNameFilesFileIDGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.get_file_api_v1_workspaces_workspace_name_files_file_id_get_200_application_json_any = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def get_document(self, request: operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetRequest, security: operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetSecurity) -> operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetResponse:
        r"""Get Document
        Returns all documents generated for a file.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/files/{file_id}/documents', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDocumentAPIV1WorkspacesWorkspaceNameFilesFileIDDocumentsGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Documents])
                res.documents = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def get_meta_data(self, request: operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetRequest, security: operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetSecurity) -> operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetResponse:
        r"""Get File Meta
        Displays the metadata of a file.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/files/{file_id}/meta', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.response_get_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_get = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def list(self, request: operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest, security: operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetSecurity) -> operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetResponse:
        r"""List Files
        List files in a workspace. This endpoint supports pagination and filtering by name and metadata.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/files', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListFilesAPIV1WorkspacesWorkspaceNameFilesGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.FilePagination])
                res.file_pagination = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def update_meta_data(self, request: operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutRequest, security: operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutSecurity) -> operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutResponse:
        r"""Update File Meta
        Updates the metadata of a file. You can modify existing metadata or add new ones. The metadata of the documents that were created
        from this file will also be updated.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutRequest, base_url, '/api/v1/workspaces/{workspace_name}/files/{file_id}/meta', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.update_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_put_200_application_json_any = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def upload(self, request: operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostRequest, security: operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostSecurity) -> operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostResponse:
        r"""Upload File
        Uploads a file into the workspace. You can also use this endpoint to create a text file. To do that, enter the file name and text as its contents.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostRequest, base_url, '/api/v1/workspaces/{workspace_name}/files', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "body_upload_file_api_v1_workspaces_workspace_name_files_post", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UploadFileAPIV1WorkspacesWorkspaceNameFilesPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, str]])
                res.response_upload_file_api_v1_workspaces_workspace_name_files_post = out
        elif http_res.status_code in [400, 409, 413, 415]:
            pass
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    