"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import createtagresponse as components_createtagresponse
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateTagAPIV1WorkspacesWorkspaceNameTagsPostTagParameters:
    r"""The parameters of the tag you want to create."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the tag."""
    



@dataclasses.dataclass
class CreateTagAPIV1WorkspacesWorkspaceNameTagsPostRequest:
    request_body: CreateTagAPIV1WorkspacesWorkspaceNameTagsPostTagParameters = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    workspace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_name', 'style': 'simple', 'explode': False }})
    r"""Type the name of the workspace."""
    



@dataclasses.dataclass
class CreateTagAPIV1WorkspacesWorkspaceNameTagsPostResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    create_tag_response: Optional[components_createtagresponse.CreateTagResponse] = dataclasses.field(default=None)
    r"""Successful Response"""
    

