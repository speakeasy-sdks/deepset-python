"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from typing import Any, Optional


@dataclasses.dataclass
class GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetRequest:
    
    pipeline_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pipeline_name', 'style': 'simple', 'explode': False }})
    r"""The name of the pipeline that you want to return as JSON."""
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    

@dataclasses.dataclass
class GetPipelineYamlAsJSONAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameJSONGetResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    response_get_pipeline_yaml_as_json_api_v1_workspaces_workspace_name_pipelines_pipeline_name_json_get: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""Returns the pipeline as JSON."""
    