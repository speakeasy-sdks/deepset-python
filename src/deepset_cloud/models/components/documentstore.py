"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .pipelineindexingstatus import PipelineIndexingStatus
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DocumentStore:
    indexing: PipelineIndexingStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexing') }})
    return_embedding: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('return_embedding') }})
    similarity: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('similarity') }})
    
