"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from deepset_cloud.models import operations, shared
from typing import Any, Optional

class SharedPrototype:
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
        
    
    def create(self, request: operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostRequest, security: operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostSecurity) -> operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostResponse:
        r"""Create Prototype [private]
        This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostRequest, base_url, '/api/v1/workspaces/{workspace_name}/shared_prototypes', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "post_shared_prototype", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SharedPrototype])
                res.shared_prototype = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def create_external_user(self, request: operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostRequest, security: operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostSecurity) -> operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostResponse:
        r"""Create External User [private]
        This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostRequest, base_url, '/api/v1/workspaces/{workspace_name}/shared_prototype_users', request)
        headers = {}
        query_params = utils.get_query_params(operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateExternalUserAPIV1WorkspacesWorkspaceNameSharedPrototypeUsersPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [200, 201]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ExternalUserInformation])
                res.external_user_information = out
        elif http_res.status_code in [400, 404]:
            pass
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def get(self, request: operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetRequest, security: operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetSecurity) -> operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetResponse:
        r"""Get Shared Prototype [private]
        This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/shared_prototypes/{shared_prototype_id}', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SharedPrototype])
                res.shared_prototype = out
        elif http_res.status_code == 404:
            pass
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def list(self, request: operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest, security: operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetSecurity) -> operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetResponse:
        r"""List Prototypes [private]
        This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest, base_url, '/api/v1/workspaces/{workspace_name}/shared_prototypes', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetRequest, request)
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListPrototypesAPIV1WorkspacesWorkspaceNameSharedPrototypesGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PaginatedSharedPrototypes])
                res.paginated_shared_prototypes = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def revoke(self, request: operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteRequest, security: operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteSecurity) -> operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteResponse:
        r"""Revoke Shared Prototype [private]
        This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteRequest, base_url, '/api/v1/workspaces/{workspace_name}/shared_prototypes/{shared_prototype_id}', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RevokeSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDDeleteResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.revoke_shared_prototype_api_v1_workspaces_workspace_name_shared_prototypes_shared_prototype_id_delete_200_application_json_any = out
        elif http_res.status_code == 404:
            pass
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    
    def update(self, request: operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchRequest, security: operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchSecurity) -> operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchResponse:
        r"""Edit Shared Prototype [private]
        This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchRequest, base_url, '/api/v1/workspaces/{workspace_name}/shared_prototypes/{shared_prototype_id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "patch_shared_prototype", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SharedPrototype])
                res.shared_prototype = out
        elif http_res.status_code == 404:
            pass
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    