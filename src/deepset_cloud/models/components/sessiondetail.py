"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from deepset_cloud import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FileIngestionStatus:
    r"""The status of the ingestion process for this file."""
    failed_files: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failed_files'), 'exclude': lambda f: f is None }})
    r"""The number of files that failed to be ingested."""
    finished_files: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('finished_files'), 'exclude': lambda f: f is None }})
    r"""The number of files that were successfully ingested."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SessionDetail:
    expires_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expires_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The time when the session expires."""
    ingestion_status: FileIngestionStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ingestion_status') }})
    r"""The status of the ingestion process for this file."""
    session_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('session_id') }})
    r"""Unique identifier of a session."""
    documentation_url: Optional[str] = dataclasses.field(default='https://docs.cloud.deepset.ai/docs', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentation_url'), 'exclude': lambda f: f is None }})
    r"""The URL to the documentation of the session."""
    
