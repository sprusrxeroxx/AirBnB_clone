#!/usr/bin/python3
""" Defines the Place class for representing places in
the Airbnb application.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class for representing places in the Airbnb application.

    Public class attributes:
        city_id (str): Empty string by default, representing the ID of
                    the City associated with the place.

        user_id (str): Empty string by default, representing the ID of
                    the User associated with the place.

        name (str): Empty string by default, representing the place's name.

        description (str): Empty string by default, representing the
                        description of the place.

        number_rooms (int): 0 by default, representing the number of
                        rooms in the place.

        number_bathrooms (int): 0 by default, representing the number of
                            bathrooms in the place.

        max_guest (int): 0 by default, representing the maximum number of
                        guests allowed in the place.

        price_by_night (int): 0 by default, representing the price per night
                            for the place.

        latitude (float): 0.0 by default, representing the latitude coordinate
                        of the place.

        longitude (float): 0.0 by default, representing the longitude
                            coordinate of the place.

        amenity_ids (list): Empty list by default, representing the list of
                            Amenity IDs associated with the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []