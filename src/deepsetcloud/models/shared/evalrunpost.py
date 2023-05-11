"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from deepsetcloud import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EvalRunPost:
    
    debug: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('debug') }})
    r"""Turns the debug mode on for this evaluation run. The debug mode shows you what went wrong if the evaluation run fails."""
    evaluation_set_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('evaluation_set_name') }})
    r"""Which evaluation set do you want to use? Type its name here."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Give your evaluation run a unique name."""
    pipeline_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pipeline_name') }})
    r"""Which pipeline do you want to use for this evaluation run?"""
    comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment'), 'exclude': lambda f: f is None }})
    r"""Type any additional information or comments as raw text."""
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    r"""Enter the tags for this evaluation run."""
    