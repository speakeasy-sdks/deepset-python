"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PipelineName:
    r"""Your pipeline was created."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the pipeline"""
    

