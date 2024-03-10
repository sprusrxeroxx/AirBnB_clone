#!/usr/bin/python3
""" This module contains the user class, a subclassof BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ a class that defines a new user in the application.
    Args:
        email (str): user's email address
        password (str): user's password
        first_name (str): user's first name
        last_name (str): the user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""