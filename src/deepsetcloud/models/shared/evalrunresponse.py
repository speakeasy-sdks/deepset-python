"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import pipelinenodeconfig as shared_pipelinenodeconfig
from ..shared import tag as shared_tag
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepsetcloud import utils
from marshmallow import fields
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EvalRunResponseOauthUser:
    r"""The user who created the eval run."""
    
    family_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('family_name') }})
    r"""Family name of a user"""
    given_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('given_name') }})
    r"""Given name of a user"""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EvalRunResponseEvalRunParameters:
    r"""Parameters set for this evaluation run"""
    
    debug: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('debug') }})
    r"""Turns the debug mode on for this evaluation run. The debug mode shows you what went wrong if the evaluation run fails."""
    evaluation_set_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('evaluation_set_id') }})
    r"""A unique identifier of the evaluation set used for the evaluation run."""
    evaluation_set_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('evaluation_set_name') }})
    r"""The name of the evaluation set used for the evaluation run."""
    pipeline_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_name') }})
    r"""The name of the pipeline used for evaluation."""
    pipeline_snapshot_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_snapshot_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time when the pipeline snapshot was taken."""
    pipeline_snapshot_yaml: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_snapshot_yaml') }})
    r"""Pipeline YAML at the time of the snapshot."""
    sas_model_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas_model_name'), 'exclude': lambda f: f is None }})
    r"""The name of the model used to calculate SAS metrics during an experiment."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EvalRunResponsePipelineMetric:
    r"""The metrics for the whole pipeline."""
    
    integrated_exact_match: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_exact_match'), 'exclude': lambda f: f is None }})
    r"""The number of exact matches of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    integrated_f1: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_f1'), 'exclude': lambda f: f is None }})
    r"""The F1 score of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    integrated_mean_average_precision: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_mean_average_precision'), 'exclude': lambda f: f is None }})
    r"""The mean average precision of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    integrated_mean_reciprocal_rank: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_mean_reciprocal_rank'), 'exclude': lambda f: f is None }})
    r"""The mean reciprocal rank of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    integrated_normal_discounted_cumulative_gain: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_normal_discounted_cumulative_gain'), 'exclude': lambda f: f is None }})
    r"""The normal discounted cumulative gain of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    integrated_precision: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_precision'), 'exclude': lambda f: f is None }})
    r"""The precision of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    integrated_recall_multi_hit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_recall_multi_hit'), 'exclude': lambda f: f is None }})
    r"""The recall multi hit metric of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    integrated_recall_single_hit: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_recall_single_hit'), 'exclude': lambda f: f is None }})
    r"""The recall single hit metric of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    integrated_sas: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrated_sas'), 'exclude': lambda f: f is None }})
    r"""The SAS score of the pipeline. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    isolated_exact_match: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isolated_exact_match'), 'exclude': lambda f: f is None }})
    r"""The number of exact matches of the last answer_node in isolated mode. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    isolated_f1: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isolated_f1'), 'exclude': lambda f: f is None }})
    r"""The F1 score of the last answer_node in isolated mode. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    isolated_sas: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isolated_sas'), 'exclude': lambda f: f is None }})
    r"""The SAS score of the last answer_node in isolated mode. For more information, see [Experiments and Metrics](https://docs.cloud.deepset.ai/docs/experiments-and-metrics)"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EvalRunResponse:
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date and time when the evaluation run was created."""
    created_by: EvalRunResponseOauthUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by') }})
    r"""The user who created the eval run."""
    eval_run_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eval_run_id') }})
    r"""A unique identifier of the evaluation run."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Unique name of an evaluation run."""
    parameters: EvalRunResponseEvalRunParameters = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters') }})
    r"""Parameters set for this evaluation run"""
    pipeline_metrics: EvalRunResponsePipelineMetric = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_metrics') }})
    r"""The metrics for the whole pipeline."""
    pipeline_parameters: dict[str, shared_pipelinenodeconfig.PipelineNodeConfig] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_parameters') }})
    r"""The parameters for each pipeline node with key and value."""
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Status of the evaluation run. Returns one of these values: CREATED, STARTED, FAILED, ENDED."""
    tags: list[shared_tag.Tag] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags') }})
    r"""A list of tags associated with the evaluation run."""
    comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment'), 'exclude': lambda f: f is None }})
    r"""Add a comment about this evaluation run."""
    eval_results: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eval_results'), 'exclude': lambda f: f is None }})
    r"""Contains the evaluated pipeline nodes and their overall metrics."""
    last_edited_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_edited_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date and time when the evaluation run was last edited."""
    last_edited_by: Optional[EvalRunResponseOauthUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_edited_by'), 'exclude': lambda f: f is None }})
    r"""The user who created the eval run."""
    