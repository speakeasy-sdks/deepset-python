"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import httpvalidationerror as shared_httpvalidationerror
from ..shared import notebook as shared_notebook
from typing import Any, Optional


@dataclasses.dataclass
class PostNotebookAPIV1NotebookPostSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class PostNotebookAPIV1NotebookPostRequest:
    
    pipeline_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pipeline_id', 'style': 'form', 'explode': True }})
    r"""A unique identifier of a pipeline. You can obtain it from the List Pipelines endpoint."""
    request_body: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PostNotebookAPIV1NotebookPostResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    notebook: Optional[shared_notebook.Notebook] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    