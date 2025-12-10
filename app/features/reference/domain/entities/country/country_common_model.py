"""
Country common model module.
"""

from pydantic import BaseModel, Field


class CountryBaseModel(BaseModel):
    """
    CountryBaseModel common fields.
    """

    code: str = Field(examples=["US"])
    name: str = Field(examples=["United States"])
