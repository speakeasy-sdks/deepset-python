"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from deepsetcloud.models import operations, shared
from typing import Any, Optional

class Notebook:
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
        
    
    def create(self, request: operations.PostNotebookAPIV1NotebookPostRequest, security: operations.PostNotebookAPIV1NotebookPostSecurity) -> operations.PostNotebookAPIV1NotebookPostResponse:
        r"""Post Notebook [private]
        Creates a Jupyter notebook on the Jupyter server. You must have a server ready to create a notebook. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/v1/notebook'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.PostNotebookAPIV1NotebookPostRequest, request)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostNotebookAPIV1NotebookPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Notebook])
                res.notebook = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def get_server_state(self, security: operations.GetJupyterLabAPIV1NotebookServerGetSecurity) -> operations.GetJupyterLabAPIV1NotebookServerGetResponse:
        r"""Get Jupyter Lab [private]
        Returns the state of the Jupyter lab server. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/v1/notebook-server'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetJupyterLabAPIV1NotebookServerGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Server])
                res.server = out

        return res

    
    def start(self, request: shared.NotebookServerPost, security: operations.StartJupyterLabAPIV1NotebookServerPostSecurity) -> operations.StartJupyterLabAPIV1NotebookServerPostResponse:
        r"""Start Jupyter Lab [private]
        Opens the Jupyter lab. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/v1/notebook-server'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.StartJupyterLabAPIV1NotebookServerPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.start_jupyter_lab_api_v1_notebook_server_post_200_application_json_any = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    