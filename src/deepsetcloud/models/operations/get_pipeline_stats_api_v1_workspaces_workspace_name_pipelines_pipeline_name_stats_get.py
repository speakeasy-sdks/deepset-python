"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from ..shared import pipelinestatistics as shared_pipelinestatistics
from typing import Optional


@dataclasses.dataclass
class GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetRequest:
    
    pipeline_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pipeline_name', 'style': 'simple', 'explode': False }})
    r"""The name of the pipeline you want to fetch."""
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    

@dataclasses.dataclass
class GetPipelineStatsAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameStatsGetResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    pipeline_statistics: Optional[shared_pipelinestatistics.PipelineStatistics] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    