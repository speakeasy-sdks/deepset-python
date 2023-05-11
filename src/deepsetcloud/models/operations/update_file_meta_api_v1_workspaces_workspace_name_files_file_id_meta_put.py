"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from typing import Any, Optional


@dataclasses.dataclass
class UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutRequest:
    
    file_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'file_id', 'style': 'simple', 'explode': False }})
    request_body: dict[str, Any] = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    

@dataclasses.dataclass
class UpdateFileMetaAPIV1WorkspacesWorkspaceNameFilesFileIDMetaPutResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_file_meta_api_v1_workspaces_workspace_name_files_file_id_meta_put_200_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful Response"""
    