#!/usr/bin/python3
""" Defines the City class for representing cities in the
Airbnb application.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class for representing cities in the Airbnb application.

    Public class attributes:
        state_id (str): Empty string by default, representing the ID of
                        the State associated with the city.
        name (str): Empty string by default, representing the city's name.
    """
    state_id = ""
    name = ""