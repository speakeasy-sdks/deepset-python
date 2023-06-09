"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelRegistryToken:
    r"""Successful Response"""
    
    invalid: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invalid') }})
    r"""Signals whether the token is invalid."""
    model_registry_token_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_registry_token_id') }})
    r"""Unique identifier of the model registry token"""
    provider: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    r"""Model provider, for example huggingface"""
    provider_domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider_domain') }})
    r"""Model provider domain, for example huggingface.co"""
    