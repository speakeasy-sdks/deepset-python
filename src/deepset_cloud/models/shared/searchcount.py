"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SearchCount:
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    r"""Number of queries that were sent."""
    date_: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date') }})
    r"""Date of the counted search queries."""
    

