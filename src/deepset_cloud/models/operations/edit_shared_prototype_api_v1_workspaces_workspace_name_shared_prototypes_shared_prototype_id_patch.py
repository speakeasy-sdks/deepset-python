"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import patchsharedprototype as components_patchsharedprototype
from ...models.components import sharedprototype as components_sharedprototype
from typing import Optional


@dataclasses.dataclass
class EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchRequest:
    patch_shared_prototype: components_patchsharedprototype.PatchSharedPrototype = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    shared_prototype_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'shared_prototype_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the shared prototype"""
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    



@dataclasses.dataclass
class EditSharedPrototypeAPIV1WorkspacesWorkspaceNameSharedPrototypesSharedPrototypeIDPatchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    shared_prototype: Optional[components_sharedprototype.SharedPrototype] = dataclasses.field(default=None)
    r"""The prototype was successfully updated with the new values"""
    

