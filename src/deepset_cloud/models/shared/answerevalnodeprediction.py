"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import labelwithprediction as shared_labelwithprediction
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepset_cloud import utils
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class AnswerEvalNodePredictionEvaluationModeEnum(str, Enum):
    r"""An enumeration."""
    ISOLATED = 'ISOLATED'
    INTEGRATED = 'INTEGRATED'

class AnswerEvalNodePredictionPredictionTypeEnum(str, Enum):
    r"""This node returns answer objects during the prediction."""
    ANSWER = 'answer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AnswerEvalNodePrediction:
    
    context_similarity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context_similarity') }})
    r"""The maximum context similarity of all predictions for the given label."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time when the prediction was created."""
    eval_mode: AnswerEvalNodePredictionEvaluationModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eval_mode') }})
    r"""Whether the node was evaluated as part of the entire pipeline (integrated) or on its own (isolated)."""
    eval_node_result_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eval_node_result_id') }})
    r"""ID for the results of a node which this prediction belongs to."""
    exact_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exact_match') }})
    r"""'True' if the node returned the answer as specified in the evaluation set."""
    exact_match_context_scope: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exact_match_context_scope') }})
    r"""'True' if the node returned the context as specified in the evaluation set."""
    exact_match_document_id_and_context_scope: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exact_match_document_id_and_context_scope') }})
    r"""'True' if the node returned the document and context as specified in the evaluation set."""
    f1: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('f1') }})
    r"""Overlap between returned answer and correct answer."""
    f1_context_scope: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('f1_context_scope') }})
    r"""Best F1 for the correct answers with matching context."""
    f1_document_id_and_context_scope: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('f1_document_id_and_context_scope') }})
    r"""Best F1 for the correct answer with matching document and context."""
    f1_document_id_scope: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('f1_document_id_scope') }})
    r"""Best F1 for the correct answer with matching document."""
    index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    r"""The index of this prediction for a particular query."""
    labels: list[shared_labelwithprediction.LabelWithPrediction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    r"""The labels associated with this prediction including label specific prediction data such as the f1 score for this specific label."""
    prediction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prediction_id') }})
    r"""Unique identifier of this eval prediction."""
    prediction_type: AnswerEvalNodePredictionPredictionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prediction_type') }})
    r"""This node returns answer objects during the prediction."""
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""The text which was used to evaluate this particular node's query behavior."""
    rank: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rank') }})
    r"""The rank of this prediction among the predictions of the node for the given query."""
    answer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer'), 'exclude': lambda f: f is None }})
    r"""The answer which the node returned."""
    answer_end: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_end'), 'exclude': lambda f: f is None }})
    r"""End index of the predicted answer in the predicted context."""
    answer_start: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_start'), 'exclude': lambda f: f is None }})
    r"""Start index of the predicted answer in the predicted context."""
    context: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context'), 'exclude': lambda f: f is None }})
    r"""Context of the node's prediction."""
    document_answer_end: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_answer_end'), 'exclude': lambda f: f is None }})
    r"""End index of the predicted answer in the source document."""
    document_answer_start: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_answer_start'), 'exclude': lambda f: f is None }})
    r"""Start index of the predicted answer in the source document."""
    document_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_id'), 'exclude': lambda f: f is None }})
    r"""The ID of the predicted document."""
    document_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_ids'), 'exclude': lambda f: f is None }})
    r"""The IDs of the referenced documents."""
    filters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters'), 'exclude': lambda f: f is None }})
    r"""Filters which were used for the evaluation of the query."""
    prompt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    r"""The prompt that was used to generate the result."""
    sas: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas'), 'exclude': lambda f: f is None }})
    r"""Semantic similarity between returned answer and correct answer."""
    sas_context_scope: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas_context_scope'), 'exclude': lambda f: f is None }})
    r"""Best SAS for the correct answers with matching context."""
    sas_document_id_and_context_scope: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas_document_id_and_context_scope'), 'exclude': lambda f: f is None }})
    r"""Best SAS for the correct answer with matching document and context."""
    sas_document_id_scope: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas_document_id_scope'), 'exclude': lambda f: f is None }})
    r"""Best SAS for the correct answer with matching document."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date and time when the prediction was created."""
    