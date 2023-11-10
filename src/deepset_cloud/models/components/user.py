"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .organizationformatted import OrganizationFormatted
from dataclasses_json import Undefined, dataclass_json
from deepset_cloud import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class User:
    deleted: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deleted') }})
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""Email of a user"""
    family_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('family_name') }})
    r"""Family name of a user"""
    given_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('given_name') }})
    r"""Given name of a user"""
    oauth_provider: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauth_provider') }})
    r"""Oauth provider from auth0. For example: 'auth0', 'google-auth', 'github', and the like."""
    organization: OrganizationFormatted = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_id') }})
    oauth_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauth_id'), 'exclude': lambda f: f is None }})
    r"""Oauth ID from auth0"""
    
