"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createmodelregistrytoken as shared_createmodelregistrytoken
from ..shared import httpvalidationerror as shared_httpvalidationerror
from enum import Enum
from typing import Any, Optional


@dataclasses.dataclass
class SaveTokenAPIV1ModelRegistryTokensProviderPostSecurity:
    
    http_bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    
class SaveTokenAPIV1ModelRegistryTokensProviderPostProviderModelProvider(str, Enum):
    r"""The provider of the model registry"""
    HUGGINGFACE = 'huggingface'
    OPENAI = 'openai'
    COHERE = 'cohere'


@dataclasses.dataclass
class SaveTokenAPIV1ModelRegistryTokensProviderPostRequest:
    
    create_model_registry_token: shared_createmodelregistrytoken.CreateModelRegistryToken = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    provider: SaveTokenAPIV1ModelRegistryTokensProviderPostProviderModelProvider = dataclasses.field(metadata={'path_param': { 'field_name': 'provider', 'style': 'simple', 'explode': False }})
    r"""The provider of the model registry"""
    

@dataclasses.dataclass
class SaveTokenAPIV1ModelRegistryTokensProviderPostResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    http_validation_error: Optional[shared_httpvalidationerror.HTTPValidationError] = dataclasses.field(default=None)
    r"""Validation Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    save_token_api_v1_model_registry_tokens_provider_post_201_application_json_any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful Response"""
    