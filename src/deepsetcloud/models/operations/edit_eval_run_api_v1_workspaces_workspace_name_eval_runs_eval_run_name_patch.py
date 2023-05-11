"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import evalruncreateresponse as shared_evalruncreateresponse
from ..shared import evalrunpatch as shared_evalrunpatch
from ..shared import httpvalidationerror as shared_httpvalidationerror
from typing import Optional


@dataclasses.dataclass
class EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchRequest:
    
    eval_run_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'eval_run_name', 'style': 'simple', 'explode': False }})
    r"""Which evaluation run do you want to update? Type its name here."""
    eval_run_patch: shared_evalrunpatch.EvalRunPatch = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    

@dataclasses.dataclass
class EditEvalRunAPIV1WorkspacesWorkspaceNameEvalRunsEvalRunNamePatchResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    eval_run_create_response: Optional[shared_evalruncreateresponse.EvalRunCreateResponse] = dataclasses.field(default=None)
    r"""Successful Response"""
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    