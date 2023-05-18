"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from deepset_cloud.models import operations, shared
from typing import Any, Optional

class Organization:
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
        
    
    def get(self, security: operations.GetOrganizationAPIV1OrganizationGetSecurity) -> operations.GetOrganizationAPIV1OrganizationGetResponse:
        r"""Get Organization [private]
        Returns the name of the organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/api/v1/organization'
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrganizationAPIV1OrganizationGetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OrganizationName])
                res.organization_name = out

        return res

    
    def invite(self, request: operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostRequest, security: operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostSecurity) -> operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostResponse:
        r"""Invite User To Organization [private]
        Sends an email to the user inviting them to your deepset Cloud organization. This is an endpoint we use internally. This means it can change anytime so bear this in mind if you want to use it.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostRequest, base_url, '/api/v1/organization/{organization_id}/invitation', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.InviteUserToOrganizationAPIV1OrganizationOrganizationIDInvitationPostResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.invite_user_to_organization_api_v1_organization_organization_id_invitation_post_201_application_json_any = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HTTPValidationError])
                res.http_validation_error = out

        return res

    