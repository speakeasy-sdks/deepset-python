"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import serverstate as shared_serverstate
from ..shared import servertype as shared_servertype
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Server:
    server_type: shared_servertype.ServerType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server_type') }})
    r"""An enumeration."""
    state: shared_serverstate.ServerState = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    r"""An enumeration."""
    

