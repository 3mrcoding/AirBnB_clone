#!/usr/bin/python3
"""Define the Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A Represents of the Review class"""

    place_id = ""
    user_id = ""
    text = ""
