"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import countdocumentsparams as shared_countdocumentsparams
from ..shared import dcdocumentcount as shared_dcdocumentcount
from ..shared import httpvalidationerror as shared_httpvalidationerror
from typing import Optional


@dataclasses.dataclass
class CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostRequest:
    
    count_documents_params: shared_countdocumentsparams.CountDocumentsParams = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    index_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'index_name', 'style': 'simple', 'explode': False }})
    r"""The name of the pipeline."""
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    

@dataclasses.dataclass
class CountDocumentsStreamAPIV1WorkspacesWorkspaceNameIndexesIndexNameDocumentsCountPostResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dc_document_count: Optional[shared_dcdocumentcount.DCDocumentCount] = dataclasses.field(default=None)
    r"""Successful Response"""
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    