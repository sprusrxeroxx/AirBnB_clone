#!/usr/bin/python3
""" Defines the Review class for representing reviews in the
Airbnb application.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for representing reviews in the Airbnb application.

    Public class attributes:
        place_id (str): Empty string by default, representing the ID of
                        the Place associated with the review.

        user_id (str): Empty string by default, representing the ID of the User
                        associated with the review.

        text (str): Empty string by default, representing the review text.
    """
    place_id = ""
    user_id = ""
    text = ""