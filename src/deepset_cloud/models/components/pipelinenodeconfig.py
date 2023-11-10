"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils


@dataclasses.dataclass
class PipelineParameters:
    r"""The configuration parameters of this pipeline component"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PipelineNodeConfig:
    params: PipelineParameters = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('params') }})
    r"""The configuration parameters of this pipeline component"""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Python class name of the node."""
    
