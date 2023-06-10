"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import pipelineindexing as shared_pipelineindexing
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PipelinePagination:
    r"""Successful Response"""
    data: list[shared_pipelineindexing.PipelineIndexing] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_more') }})
    total: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    

