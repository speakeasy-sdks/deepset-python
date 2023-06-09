"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import modelregistrytoken as shared_modelregistrytoken
from typing import Optional


@dataclasses.dataclass
class ListTokensAPIV1ModelRegistryTokensGetSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class ListTokensAPIV1ModelRegistryTokensGetResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_registry_tokens: Optional[list[shared_modelregistrytoken.ModelRegistryToken]] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    