"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from deepsetcloud.models import operations, shared
from typing import Optional

class DocumentStore:
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
        
    
    def check_connection(self, request: operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetRequest, security: operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetSecurity) -> operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetResponse:
        r"""Check Connection [private]
        Checks the connection to the Opensearch document store and checks if the pipeline_name (index) exists. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/indexes/{index_name}', request)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CheckConnectionAPIV1WorkspacesWorkspaceNameIndexesIndexNameGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DocumentStore])
                res.document_store = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def count_documents(self, request: operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostRequest, security: operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostSecurity) -> operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostResponse:
        r"""Count Documents Stream [private]
        Returns the number of documents for a pipeline. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostRequest, base_url, '/api/v1/workspaces/{workspace_name}/indexes/{index_name}/documents-count', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "count_documents_params", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DCDocumentCount])
                res.dc_document_count = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def get(self, request: operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetRequest, security: operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetSecurity) -> operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetResponse:
        r"""Get Document [private]
        Displays the document content and its properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/indexes/{index_name}/documents/{document_id}', request)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDocumentAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsDocumentIDGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeepsetCloudDocument])
                res.deepset_cloud_document = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def list_document_streams(self, request: operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostRequest, security: operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostSecurity) -> operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostResponse:
        r"""Get All Documents Stream
        Returns all documents created for a pipeline.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostRequest, base_url, '/api/v1/workspaces/{workspace_name}/indexes/{index_name}/documents-stream', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "fetch_documents_params", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsStreamPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def list_documents(self, request: operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetRequest, security: operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetSecurity) -> operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetResponse:
        r"""Get All Documents [private]
        Displays all documents processed by the specified pipeline together with their properties. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/indexes/{index_name}/documents', request)
        
        query_params = utils.get_query_params(operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAllDocumentsAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.DeepsetCloudDocument]])
                res.deepset_cloud_documents = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def search(self, request: operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostRequest, security: operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostSecurity) -> operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostResponse:
        r"""Query Documents Stream
        Searches the documents for the specified query.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostRequest, base_url, '/api/v1/workspaces/{workspace_name}/indexes/{index_name}/documents-query', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "query_documents_params", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.QueryDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsQueryPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.DeepsetCloudDocument]])
                res.deepset_cloud_documents = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    