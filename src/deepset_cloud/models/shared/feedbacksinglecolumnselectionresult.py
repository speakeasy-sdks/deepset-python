"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class FeedbackSingleColumnSelectionResult:
    r"""This response format is only used with the `select` query parameter. It returns a list of distinct JSON objects with the selected attributes, for example, '[{\\"feedback_id\\": \\"...\\", \\"is_correct_answer\\": true}]' for 'select=feedback_id, is_correct_answer, created_by/user_id'. Selecting single columns is supported for the 'feedback_id', 'is_correct_answer', and 'is_correct_document' columns."""
    pass
