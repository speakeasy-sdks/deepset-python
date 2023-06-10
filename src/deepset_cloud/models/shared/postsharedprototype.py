"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepset_cloud import utils
from marshmallow import fields
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PostSharedPrototype:
    expiration_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiration_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""The date after which the generated link will expire and become invalid. The expiration date must be within 60 days from the current date."""
    pipeline_names: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_names') }})
    r"""Type the names of the pipelines you want to share."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Explain how you expect the users to use this pipeline. Users who visit the shared prototype will see this text. For more information on how to set the right expectations regarding your pipeline, see [Guidelines for Onboarding Your Users](https://docs.cloud.deepset.ai/docs/guidelines-for-onboarding-your-users)."""
    show_files: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show_files'), 'exclude': lambda f: f is None }})
    r"""Select `True` if you want your users to be able to see the files."""
    show_metadata_filters: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show_metadata_filters'), 'exclude': lambda f: f is None }})
    r"""Select `True` if you want your users to be able to filter the documents by metadata."""
    

