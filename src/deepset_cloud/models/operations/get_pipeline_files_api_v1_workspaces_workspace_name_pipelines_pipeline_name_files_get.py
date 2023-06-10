"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from enum import Enum
from typing import Optional



@dataclasses.dataclass
class GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetSecurity:
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    


class GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetStatusFileIndexingStatusQuery(str, Enum):
    r"""An enumeration."""
    FAILED = 'FAILED'
    INDEXED_NO_DOCUMENTS = 'INDEXED_NO_DOCUMENTS'



@dataclasses.dataclass
class GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetRequest:
    pipeline_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pipeline_name', 'style': 'simple', 'explode': False }})
    r"""The name of the pipeline whose files you want to display."""
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    status: Optional[GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetStatusFileIndexingStatusQuery] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    r"""The status of the pipeline whose files you want to display."""
    




@dataclasses.dataclass
class GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_pipeline_files_api_v1_workspaces_workspace_name_pipelines_pipeline_name_files_get_200_application_json_uuid_strings: Optional[list[str]] = dataclasses.field(default=None)
    r"""Successful Response"""
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

