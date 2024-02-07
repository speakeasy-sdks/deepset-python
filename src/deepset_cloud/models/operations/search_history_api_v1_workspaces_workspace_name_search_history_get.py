"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import searchhistorypagination as components_searchhistorypagination
from typing import Optional


@dataclasses.dataclass
class SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetRequest:
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    after: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    r"""Enter an ID if you want to see all entries after this ID."""
    before: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before', 'style': 'form', 'explode': True }})
    r"""Enter an ID if you want to see all entries before this ID."""
    limit: Optional[int] = dataclasses.field(default=10, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""How many entries do you want to display? Leaving this field empty keeps the default and max 10 results are returned."""
    page_number: Optional[int] = dataclasses.field(default=1, metadata={'query_param': { 'field_name': 'page_number', 'style': 'form', 'explode': True }})
    r"""Which page do you want to see? Type the number."""
    



@dataclasses.dataclass
class SearchHistoryAPIV1WorkspacesWorkspaceNameSearchHistoryGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    search_history_pagination: Optional[components_searchhistorypagination.SearchHistoryPagination] = dataclasses.field(default=None)
    r"""Successful Response"""
    

