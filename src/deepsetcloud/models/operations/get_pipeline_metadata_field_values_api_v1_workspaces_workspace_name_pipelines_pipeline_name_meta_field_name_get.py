"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from ..shared import pipelinefieldsearchresult as shared_pipelinefieldsearchresult
from typing import Optional


@dataclasses.dataclass
class GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetRequest:
    
    field_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'field_name', 'style': 'simple', 'explode': False }})
    r"""The name of the field to search in."""
    pipeline_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pipeline_name', 'style': 'simple', 'explode': False }})
    r"""The name of the pipeline whose files you want to display."""
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    after: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    r"""Enter the offset for the pagination. Note that the results are 0-indexed which means that with 'after=0', you will skip the first element."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""How many entries do you want to display?"""
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""The query you want to use to search through metadata. You can use wildcards in the query, for example, '*query*' to list all values which contain the term 'query'."""
    

@dataclasses.dataclass
class GetPipelineMetadataFieldValuesAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameMetaFieldNameGetResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    pipeline_field_search_result: Optional[shared_pipelinefieldsearchresult.PipelineFieldSearchResult] = dataclasses.field(default=None)
    r"""Metadata for the pipeline's index."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    