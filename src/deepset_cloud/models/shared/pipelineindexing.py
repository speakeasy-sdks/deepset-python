"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import pipelineindexingstatus as shared_pipelineindexingstatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepset_cloud import utils
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PipelineIndexingOauthUser:
    r"""The user who created the pipeline."""
    family_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('family_name') }})
    r"""Family name of a user"""
    given_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('given_name') }})
    r"""Given name of a user"""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PipelineIndexing:
    r"""Successful Response"""
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""Datetime object, specifies when the pipeline was created"""
    desired_status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('desired_status') }})
    r"""Desired status of a pipeline. This string is either 'DEPLOYED' or  'UNDEPLOYED'."""
    indexing: shared_pipelineindexingstatus.PipelineIndexingStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexing') }})
    is_default: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_default') }})
    r"""Pipeline is set to default"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the pipeline"""
    pipeline_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_id') }})
    r"""Unique identifier of a pipeline"""
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Status of a pipeline. This string can be: 'DEPLOYED', 'UNDEPLOYED', 'DEPLOYMENT_IN_PROGRESS', and the like"""
    created_by: Optional[PipelineIndexingOauthUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by'), 'exclude': lambda f: f is None }})
    r"""The user who created the pipeline."""
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted'), 'exclude': lambda f: f is None }})
    r"""Soft deletion of pipelines"""
    last_edited_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_edited_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Datetime object, specifies when the pipeline was edited"""
    last_edited_by: Optional[PipelineIndexingOauthUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_edited_by'), 'exclude': lambda f: f is None }})
    r"""The user who last edited the pipeline."""
    

