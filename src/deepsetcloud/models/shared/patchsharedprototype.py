"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchSharedPrototype:
    
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Explain how you expect the users to use this pipeline. Users who visit the shared prototype will see this text. For more information on how to set the right expectations regarding your pipeline, see [Guidelines for Onboarding Your Users](https://docs.cloud.deepset.ai/docs/guidelines-for-onboarding-your-users)."""
    show_files: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show_files'), 'exclude': lambda f: f is None }})
    r"""Select `True` if you want your users to be able to see the files."""
    show_metadata_filters: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show_metadata_filters'), 'exclude': lambda f: f is None }})
    r"""Select `True` if you want your users to be able to filter the documents by metadata."""
    