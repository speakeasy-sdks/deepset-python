"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createsession as shared_createsession
from ..shared import httpvalidationerror as shared_httpvalidationerror
from ..shared import uploadsession as shared_uploadsession
from typing import Optional


@dataclasses.dataclass
class CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostRequest:
    
    create_session: shared_createsession.CreateSession = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    

@dataclasses.dataclass
class CreateUploadSessionAPIV1WorkspacesWorkspaceNameUploadSessionsPostResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    upload_session: Optional[shared_uploadsession.UploadSession] = dataclasses.field(default=None)
    r"""Your session is created."""
    