"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import modelregistrytoken as components_modelregistrytoken
from enum import Enum
from typing import Optional

class ModelProvider(str, Enum):
    r"""The provider of the model registry"""
    HUGGINGFACE = 'huggingface'
    OPENAI = 'openai'
    COHERE = 'cohere'


@dataclasses.dataclass
class GetTokenAPIV1ModelRegistryTokensProviderGetRequest:
    provider: ModelProvider = dataclasses.field(metadata={'path_param': { 'field_name': 'provider', 'style': 'simple', 'explode': False }})
    r"""The provider of the model registry"""
    



@dataclasses.dataclass
class GetTokenAPIV1ModelRegistryTokensProviderGetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    model_registry_token: Optional[components_modelregistrytoken.ModelRegistryToken] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

