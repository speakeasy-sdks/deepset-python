"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostFile:
    
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'File' }})
    

@dataclasses.dataclass
class BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPost:
    
    file: BodyImportEvaluationSetAPIV1WorkspacesWorkspaceNameEvaluationSetsImportPostFile = dataclasses.field(metadata={'multipart_form': { 'file': True }})
    