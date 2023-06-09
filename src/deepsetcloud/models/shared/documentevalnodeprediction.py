"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import labelwithprediction as shared_labelwithprediction
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepsetcloud import utils
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class DocumentEvalNodePredictionEvaluationModeEnum(str, Enum):
    r"""An enumeration."""
    ISOLATED = 'ISOLATED'
    INTEGRATED = 'INTEGRATED'

class DocumentEvalNodePredictionPredictionTypeEnum(str, Enum):
    r"""This node returns document objects during the prediction."""
    DOCUMENT = 'document'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DocumentEvalNodePrediction:
    
    answer_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('answer_match') }})
    r"""'True' if the node returned the answer as specified in the evaluation set."""
    context_and_answer_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context_and_answer_match') }})
    r"""'True' if the node returned the context and answer which was specified in the evaluation set."""
    context_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context_match') }})
    r"""'True' if the node returned the context as specified in the evaluation set."""
    context_similarity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context_similarity') }})
    r"""The maximum context similarity of all predictions for the given label."""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time when the prediction was created."""
    eval_mode: DocumentEvalNodePredictionEvaluationModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eval_mode') }})
    r"""Whether the node was evaluated as part of the entire pipeline (integrated) or on its own (isolated)."""
    eval_node_result_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eval_node_result_id') }})
    r"""ID for the results of a node which this prediction belongs to."""
    gold_id_and_answer_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gold_id_and_answer_match') }})
    r"""'True' if the node returned the document and answer as specified in the evaluation set."""
    gold_id_and_context_and_answer_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gold_id_and_context_and_answer_match') }})
    r"""'True' if the node returned the document, context, and answer as specified in the evaluation set."""
    gold_id_and_context_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gold_id_and_context_match') }})
    r"""'True' if the node returned the document and context as specified in the evaluation set."""
    gold_id_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gold_id_match') }})
    r"""'True' if the node returned the document as specified in the evaluation set."""
    gold_id_or_answer_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gold_id_or_answer_match') }})
    r"""'True' if the node returned the document or answer as specified in the evaluation set."""
    gold_id_or_context_match: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gold_id_or_context_match') }})
    r"""'True' if the node returned the document or context as specified in the evaluation set."""
    index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    r"""The index of this prediction for a particular query."""
    labels: list[shared_labelwithprediction.LabelWithPrediction] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labels') }})
    r"""The labels associated with this prediction including label specific prediction data such as the f1 score for this specific label."""
    prediction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prediction_id') }})
    r"""Unique identifier of this eval prediction."""
    prediction_type: DocumentEvalNodePredictionPredictionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prediction_type') }})
    r"""This node returns document objects during the prediction."""
    query: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query') }})
    r"""The text which was used to evaluate this particular node's query behavior."""
    rank: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rank') }})
    r"""The rank of this prediction among the predictions of the node for the given query."""
    context: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('context'), 'exclude': lambda f: f is None }})
    r"""Context of the node's prediction."""
    document_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_id'), 'exclude': lambda f: f is None }})
    r"""The ID of the predicted document."""
    filters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filters'), 'exclude': lambda f: f is None }})
    r"""Filters which were used for the evaluation of the query."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date and time when the prediction was created."""
    