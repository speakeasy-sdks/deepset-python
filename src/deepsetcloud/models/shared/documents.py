"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import document as shared_document
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Documents:
    r"""Successful Response"""
    
    data: list[shared_document.Document] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    total: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    r"""The total number of documents created for a file with the ID you specified."""
    