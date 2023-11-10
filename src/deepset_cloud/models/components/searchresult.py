"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .deepsetcloudqueryresponse import DeepsetCloudQueryResponse
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchResult:
    results: List[DeepsetCloudQueryResponse] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    r"""List of search results."""
    query_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_id'), 'exclude': lambda f: f is None }})
    r"""The search query"""
    
