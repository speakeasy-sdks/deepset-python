"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from ..shared import user as shared_user
from typing import Optional


@dataclasses.dataclass
class GetUserAPIV1UsersUserIDGetSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetUserAPIV1UsersUserIDGetRequest:
    
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    r"""A unique identifier of the user. You can obtain it by running the Get Users endpoint."""
    

@dataclasses.dataclass
class GetUserAPIV1UsersUserIDGetResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    user: Optional[shared_user.User] = dataclasses.field(default=None)
    r"""Successful Response"""
    