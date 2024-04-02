"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PipelineQuery:
    
    queries: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queries') }})
    r"""A list of queries you want to run through the pipeline."""
    debug: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('debug'), 'exclude': lambda f: f is None }})
    r"""Shows debug output for the pipeline (for example, prompt)."""
    filters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters'), 'exclude': lambda f: f is None }})
    r"""Filters you can use to narrow down the search. For more information, see [metadata filtering](https://docs.haystack.deepset.ai/docs/metadata-filtering)."""
    params: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('params'), 'exclude': lambda f: f is None }})
    r"""Parameters you can use to customize the pipeline."""
    