"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateTagID:
    
    tag_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag_id') }})
    r"""Unique ID of the tag."""
    