"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from enum import Enum
from typing import Any, Optional


@dataclasses.dataclass
class GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    
class GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetFieldFieldEnum(str, Enum):
    r"""The name of the field you want to sort by."""
    CREATED_AT = 'created_at'
    SEARCH_RESULT_RANK = 'search_result/rank'
    SEARCH_RESULT_SCORE = 'search_result/score'
    SEARCH_RESULT_SEARCH_CREATED_AT = 'search_result/search/created_at'
    SEARCH_RESULT_SEARCH_QUERY = 'search_result/search/query'

class GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetOrderOrderEnum(str, Enum):
    r"""Choose how you want to sort the results."""
    ASC = 'ASC'
    DESC = 'DESC'


@dataclasses.dataclass
class GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetRequest:
    
    pipeline_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pipeline_name', 'style': 'simple', 'explode': False }})
    r"""The name of the pipeline whose files you want to display."""
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    accept: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'accept', 'style': 'simple', 'explode': False }})
    r"""Type 'text/csv' to download the feedback as a CSV file or 'application/json' to get the feedback as JSONs."""
    after: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    r"""Enter an ID if you want to see all entries after this ID."""
    before: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before', 'style': 'form', 'explode': True }})
    r"""Enter an ID if you want to see all entries before this ID."""
    field: Optional[GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetFieldFieldEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'field', 'style': 'form', 'explode': True }})
    r"""The name of the field you want to sort by."""
    filter: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter', 'style': 'form', 'explode': True }})
    r"""The OData filter you want to use to in your query. It supports exact match and `AND` operations. For example, to filter for a metadata `category:news`, here's what the URL could look like: 'url = \\"https://api.cloud.deepset.ai/api/v1/workspaces/production/files?limit=10&filter=category eq 'news'\\"'. OData filters only work with cursor-based pagination (leave the `page_number` field blank to enable it).To learn more about the OData filter syntax, see: [Querying Data](https://www.odata.org/getting-started/basic-tutorial/#queryData)."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""How many entries do you want to display? Leaving this field empty keeps the default and max 10 results are returned."""
    order: Optional[GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetOrderOrderEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    r"""Choose how you want to sort the results."""
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_number', 'style': 'form', 'explode': True }})
    r"""Which page do you want to see? Type the number."""
    select: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'select', 'style': 'form', 'explode': True }})
    r"""Partial implementation of the OData $select operator. It currently only supports selecting fields from the root entity or a child entity. Selecting fields from children's children is not supported. If you use this parameter, the API answer is always a flat list of distinct JSON objects with the selected properties, for example, '[{\\"given_name\\": \\"user1\\", \\"user_id\\": \\"...\\"}, ...]' for 'select=created_by/given_name, created_by/user_id'. The results are ordered by the first selected attribute. To learn more about the OData filter syntax, see: [Querying Data](https://www.odata.org/getting-started/basic-tutorial/#queryData)."""
    

@dataclasses.dataclass
class GetPipelineFeedbackAPIV1WorkspacesWorkspaceNamePipelinesPipelineNameFeedbackGetResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    response_200_get_pipeline_feedback_api_v1_workspaces_workspace_name_pipelines_pipeline_name_feedback_get: Optional[Any] = dataclasses.field(default=None)
    r"""The CSV file with the collected feedback"""
    