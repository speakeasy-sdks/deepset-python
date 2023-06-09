"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sharedprototype as shared_sharedprototype
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PaginatedSharedPrototypes:
    r"""Successful Response"""
    
    data: list[shared_sharedprototype.SharedPrototype] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    r"""A list of matching shared prototypes."""
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_more') }})
    r"""Whether the paginated result has more results."""
    total: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    r"""The total number of results matching your query."""
    