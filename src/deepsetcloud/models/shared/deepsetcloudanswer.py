"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import deepsetcloudspan as shared_deepsetcloudspan
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils
from enum import Enum
from typing import Any, Optional

class DeepsetCloudAnswerAnswerTypeEnum(str, Enum):
    r"""Type of the answer."""
    GENERATIVE = 'generative'
    EXTRACTIVE = 'extractive'
    OTHER = 'other'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeepsetCloudAnswer:
    
    answer: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer') }})
    type: DeepsetCloudAnswerAnswerTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of the answer."""
    context: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context'), 'exclude': lambda f: f is None }})
    r"""Context of the answer."""
    document_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_id'), 'exclude': lambda f: f is None }})
    r"""ID of the document"""
    document_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_ids'), 'exclude': lambda f: f is None }})
    r"""IDs of the document"""
    file: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file'), 'exclude': lambda f: f is None }})
    r"""Object containing the `file_id` and `name` of a file. This is used to associate a document with a file."""
    files: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files'), 'exclude': lambda f: f is None }})
    r"""List of object containing the `file_id` and `name` of a file. This is used to associate an answer with its source files."""
    meta: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    r"""The metadata of this document."""
    offsets_in_context: Optional[list[shared_deepsetcloudspan.DeepsetCloudSpan]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offsets_in_context'), 'exclude': lambda f: f is None }})
    r"""Offsets of the answer in the context."""
    offsets_in_document: Optional[list[shared_deepsetcloudspan.DeepsetCloudSpan]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offsets_in_document'), 'exclude': lambda f: f is None }})
    r"""Offsets of the answer in the document."""
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    r"""The prompt that was used to generate the result."""
    result_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('result_id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the result."""
    score: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score'), 'exclude': lambda f: f is None }})
    r"""Score of the answer."""
    