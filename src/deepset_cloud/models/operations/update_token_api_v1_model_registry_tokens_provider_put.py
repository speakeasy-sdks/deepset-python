"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import updatemodelregistrytoken as components_updatemodelregistrytoken
from enum import Enum
from typing import Any, Optional

class UpdateTokenAPIV1ModelRegistryTokensProviderPutPathParamModelProvider(str, Enum):
    r"""The provider of the model registry"""
    HUGGINGFACE = 'huggingface'
    OPENAI = 'openai'
    COHERE = 'cohere'


@dataclasses.dataclass
class UpdateTokenAPIV1ModelRegistryTokensProviderPutRequest:
    provider: UpdateTokenAPIV1ModelRegistryTokensProviderPutPathParamModelProvider = dataclasses.field(metadata={'path_param': { 'field_name': 'provider', 'style': 'simple', 'explode': False }})
    r"""The provider of the model registry"""
    update_model_registry_token: components_updatemodelregistrytoken.UpdateModelRegistryToken = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateTokenAPIV1ModelRegistryTokensProviderPutResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    any: Optional[Any] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

