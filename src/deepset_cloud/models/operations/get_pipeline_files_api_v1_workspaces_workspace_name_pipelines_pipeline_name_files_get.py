"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum
from typing import List, Optional

class FileIndexingStatusQuery(str, Enum):
    r"""An enumeration."""
    FAILED = 'FAILED'
    INDEXED_NO_DOCUMENTS = 'INDEXED_NO_DOCUMENTS'


@dataclasses.dataclass
class GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetRequest:
    pipeline_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pipeline_name', 'style': 'simple', 'explode': False }})
    r"""The name of the pipeline whose files you want to display."""
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    status: Optional[FileIndexingStatusQuery] = dataclasses.field(default=FileIndexingStatusQuery.FAILED, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    r"""The status of the pipeline whose files you want to display."""
    



@dataclasses.dataclass
class GetPipelineFilesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFilesGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    response_get_pipeline_files_api_v1_workspaces_workspace_name_pipelines_pipeline_name_files_get: Optional[List[str]] = dataclasses.field(default=None)
    r"""Successful Response"""
    

