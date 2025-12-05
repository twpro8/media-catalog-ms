"""
Language common model module.
"""

from pydantic import BaseModel, Field


class LanguageBaseModel(BaseModel):
    """
    LanguageBaseModel common fields.
    """

    code: str = Field(examples=["en"])
    name: str = Field(examples=["English"])
