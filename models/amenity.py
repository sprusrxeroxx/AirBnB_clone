#!/usr/python3
""" Defines the Amenity class for representing amenities in
the Airbnb application.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for representing amenities in the Airbnb application.

    Public class attributes:
        name (str): Empty string by default, representing the amenity's name.
    """
    name = ""