"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import evalruncreateresponse as shared_evalruncreateresponse
from ..shared import evalrunpost as shared_evalrunpost
from ..shared import httpvalidationerror as shared_httpvalidationerror
from typing import Optional


@dataclasses.dataclass
class CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostRequest:
    
    eval_run_post: shared_evalrunpost.EvalRunPost = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    

@dataclasses.dataclass
class CreateEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsPostResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    eval_run_create_response: Optional[shared_evalruncreateresponse.EvalRunCreateResponse] = dataclasses.field(default=None)
    r"""Your experiment was created."""
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    