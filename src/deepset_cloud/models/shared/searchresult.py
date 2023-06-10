"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import deepsetcloudqueryresponse as shared_deepsetcloudqueryresponse
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SearchResult:
    r"""Returns the search results."""
    results: list[shared_deepsetcloudqueryresponse.DeepsetCloudQueryResponse] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    r"""List of search results."""
    query_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_id'), 'exclude': lambda f: f is None }})
    r"""The search query"""
    

