"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from ..shared import userpagination as shared_userpagination
from typing import Optional



@dataclasses.dataclass
class ListUsersAPIV1UsersGetSecurity:
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    




@dataclasses.dataclass
class ListUsersAPIV1UsersGetRequest:
    after: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after', 'style': 'form', 'explode': True }})
    r"""Enter an ID if you want to see all entries after this ID."""
    before: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before', 'style': 'form', 'explode': True }})
    r"""Enter an ID if you want to see all entries before this ID."""
    include_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include_deleted', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""How many entries do you want to display? Leaving this field empty keeps the default and max 10 results are returned."""
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page_number', 'style': 'form', 'explode': True }})
    r"""Which page do you want to see? Type the number."""
    




@dataclasses.dataclass
class ListUsersAPIV1UsersGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    user_pagination: Optional[shared_userpagination.UserPagination] = dataclasses.field(default=None)
    r"""Successful Response"""
    

