"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils
from enum import Enum
from typing import Optional



@dataclasses.dataclass
class LabelWithPredictionHaystackFilters:
    r"""Filters you can use to narrow down the search. For more information, see [metadata filtering](https://docs.haystack.deepset.ai/docs/metadata-filtering)."""
    pass



@dataclasses.dataclass
class LabelWithPredictionMeta:
    pass

class LabelWithPredictionLabelStateAsStr(str, Enum):
    r"""An enumeration."""
    MATCHING_NOT_STARTED = 'MATCHING_NOT_STARTED'
    MATCHED = 'MATCHED'
    NO_MATCH_FOUND = 'NO_MATCH_FOUND'
    CANDIDATES_FOUND = 'CANDIDATES_FOUND'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class LabelWithPrediction:
    context_similarity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context_similarity') }})
    r"""Similarity of the context with the gold context of this specific label."""
    document_id_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_id_match') }})
    r"""'True' if the selected document ID matched with the gold ID of this specific label."""
    label_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label_id') }})
    r"""Unique identifier of a label"""
    meta: LabelWithPredictionMeta = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta') }})
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    state: LabelWithPredictionLabelStateAsStr = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    r"""Represents the current state for matching a file."""
    answer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer'), 'exclude': lambda f: f is None }})
    answer_end: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_end'), 'exclude': lambda f: f is None }})
    answer_exact_match: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_exact_match'), 'exclude': lambda f: f is None }})
    r"""'True' if the answer matched the gold answer of this specific label."""
    answer_match: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_match'), 'exclude': lambda f: f is None }})
    r"""'True' if the document matched the gold document of this specific label."""
    answer_start: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_start'), 'exclude': lambda f: f is None }})
    candidates: Optional[dict[str, float]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('candidates'), 'exclude': lambda f: f is None }})
    r"""A dictionary that holds the UUID as key and score as value for each candidate in the label to file matching."""
    context: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context'), 'exclude': lambda f: f is None }})
    external_file_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_file_name'), 'exclude': lambda f: f is None }})
    f1: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('f1'), 'exclude': lambda f: f is None }})
    r"""F1 score for this specific label."""
    file_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_id'), 'exclude': lambda f: f is None }})
    filters: Optional[LabelWithPredictionHaystackFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters'), 'exclude': lambda f: f is None }})
    r"""Filters you can use to narrow down the search. For more information, see [metadata filtering](https://docs.haystack.deepset.ai/docs/metadata-filtering)."""
    sas: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas'), 'exclude': lambda f: f is None }})
    r"""The SAS score for this specific label."""
    

