"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import postsharedprototype as components_postsharedprototype
from ...models.components import sharedprototype as components_sharedprototype
from typing import Optional


@dataclasses.dataclass
class CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostRequest:
    post_shared_prototype: components_postsharedprototype.PostSharedPrototype = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    



@dataclasses.dataclass
class CreatePrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    shared_prototype: Optional[components_sharedprototype.SharedPrototype] = dataclasses.field(default=None)
    r"""Successful Response"""
    

