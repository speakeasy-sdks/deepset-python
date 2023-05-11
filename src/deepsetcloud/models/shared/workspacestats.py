"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkspaceStats:
    r"""Successful Response"""
    
    average_response_time: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('average_response_time') }})
    document_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_count') }})
    file_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_count') }})
    search_request_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_request_count') }})
    