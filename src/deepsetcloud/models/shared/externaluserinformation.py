"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExternalUserInformation:
    r"""Created a shared link for an existing external user"""
    
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    r"""Unique ID of the external user."""
    user_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_token') }})
    r"""A JSON web token you can use to grant access to a set of API endpoints for this specific user."""
    