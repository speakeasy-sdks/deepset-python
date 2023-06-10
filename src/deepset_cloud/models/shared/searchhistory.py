"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import pipelinename as shared_pipelinename
from ..shared import searchresulthistoryentry as shared_searchresulthistoryentry
from ..shared import useridname as shared_useridname
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepset_cloud import utils
from marshmallow import fields



@dataclasses.dataclass
class SearchHistoryQueryRequest:
    r"""Query request"""
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SearchHistory:
    duration: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duration') }})
    r"""Duration in ms."""
    pipeline: shared_pipelinename.PipelineName = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline') }})
    request: SearchHistoryQueryRequest = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request') }})
    r"""Query request"""
    response: list[shared_searchresulthistoryentry.SearchResultHistoryEntry] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('response') }})
    r"""Response list from Haystack open source"""
    search_history_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_history_id') }})
    r"""Unique identifier of the search"""
    time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Timestamp when the query was sent"""
    user: shared_useridname.UserIDName = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    

