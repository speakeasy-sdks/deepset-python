"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import evalrunresponse as shared_evalrunresponse
from ..shared import evalrunsinglecolumnselectionresult as shared_evalrunsinglecolumnselectionresult
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils
from typing import Union



@dataclasses.dataclass
class EvalRunsResponseData:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EvalRunsResponse:
    data: Union[list[shared_evalrunresponse.EvalRunResponse], list[shared_evalrunsinglecolumnselectionresult.EvalRunSingleColumnSelectionResult]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    has_more: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_more') }})
    total: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total') }})
    

