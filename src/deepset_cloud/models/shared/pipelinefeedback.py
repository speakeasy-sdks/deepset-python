"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import feedbacksearchresult as shared_feedbacksearchresult
from ..shared import tag as shared_tag
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepset_cloud import utils
from marshmallow import fields


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PipelineFeedback:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Datetime object, specifies when the feedback was created"""
    feedback_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feedback_id') }})
    r"""Unique identifier of the feedback"""
    is_correct_answer: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_correct_answer') }})
    r"""Feedback if the answer was correct"""
    is_correct_document: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_correct_document') }})
    r"""Feedback if the document was matched correctly"""
    search_result: shared_feedbacksearchresult.FeedbackSearchResult = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_result') }})
    tags: list[shared_tag.Tag] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags') }})
    r"""A list of tags associated with the feedback."""
    

