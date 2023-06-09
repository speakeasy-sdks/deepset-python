"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import searchcount as shared_searchcount
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchCountPagination:
    r"""Successful Response"""
    
    data: list[shared_searchcount.SearchCount] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    has_more: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_more'), 'exclude': lambda f: f is None }})
    total: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total'), 'exclude': lambda f: f is None }})
    