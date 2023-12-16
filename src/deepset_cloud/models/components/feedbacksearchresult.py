"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .pipelinefeedbackfile import PipelineFeedbackFile
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepset_cloud import utils
from enum import Enum
from typing import Dict, List, Optional


@dataclasses.dataclass
class FeedbackSearchResultDocuments:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FileDeprecatedUseFilesInstead:
    r"""Shows information about the file which contains the search result."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of a file."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the file"""
    



@dataclasses.dataclass
class SearchFilters:
    r"""Shows which metadata filters were used for the search query."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FeedbackUser:
    r"""The user who gave feedback to the search result."""
    family_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('family_name') }})
    r"""Family name of a user"""
    given_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('given_name') }})
    r"""Given name of a user"""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""Email of a user"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchQuery:
    r"""Shows information about the search query which returned this result."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Specifies when the search query was done."""
    duration: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration') }})
    r"""The number of seconds the pipeline took to find the answer."""
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""The search query"""
    query_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query_id') }})
    r"""Unique identifier of the search query."""
    user: FeedbackUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The user who gave feedback to the search result."""
    filters: Optional[SearchFilters] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters'), 'exclude': lambda f: f is None }})
    r"""Shows which metadata filters were used for the search query."""
    


class Type(str, Enum):
    r"""Shows the type of the prediction."""
    DOCUMENT = 'document'
    EXTRACTIVE = 'extractive'
    GENERATIVE = 'generative'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FeedbackSearchResult:
    documents: List[FeedbackSearchResultDocuments] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documents') }})
    r"""Shows the documents which contain the search results."""
    file: FileDeprecatedUseFilesInstead = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file') }})
    r"""Shows information about the file which contains the search result."""
    files: List[PipelineFeedbackFile] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('files') }})
    r"""Shows information about the files which contain the search results."""
    search: SearchQuery = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search') }})
    r"""Shows information about the search query which returned this result."""
    search_result_history_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_result_history_id') }})
    r"""Unique identifier of this search result"""
    type: Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Shows the type of the prediction."""
    answer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer'), 'exclude': lambda f: f is None }})
    r"""Shows the query answer. This is only returned for question answering pipelines."""
    context: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context'), 'exclude': lambda f: f is None }})
    r"""Shows the context of the search result."""
    offsets_in_context: Optional[List[Dict[str, int]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('offsets_in_context'), 'exclude': lambda f: f is None }})
    r"""Specifies the offset of the answer within the context."""
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    r"""The prompt that was used to generate the result."""
    rank: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rank'), 'exclude': lambda f: f is None }})
    r"""Shows the rank of the prediction."""
    score: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score'), 'exclude': lambda f: f is None }})
    r"""Shows the relevance score of the prediction."""
    

