"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from typing import Any, Optional


@dataclasses.dataclass
class CreateWorkspaceAPIV1WorkspacesPostSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class CreateWorkspaceAPIV1WorkspacesPostResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_workspace_api_v1_workspaces_post_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful Response"""
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    