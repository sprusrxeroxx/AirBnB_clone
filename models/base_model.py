#!/usr/bin/python3

"""
This module contains the BaseModel class that all other classses
will inherit common attributes and methods from
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Defines a class Basemodel from which all subclasses
    inherit from. This is the ADAM class
    """
    def __init__(self, *args, **kwargs):
        """ Initialises all public instances attributes for the programm """

        if kwargs:
            del kwargs["__class__"]
            for keys, value in kwargs.items():
                if keys == "updated_at" or keys == "created_at":
                    # convert value from str to datetime object
                    dt_object = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                            )
                    setattr(self, keys, dt_object)
                else:
                    setattr(self, keys, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates the 'updated_at' attribute to the current time and date
        """
        self.updated_at = datetime.now()  # last update
        return models.storage.save()

    def to_dict(self):
        """
        returns a dictionary representation of the
        class for use in serialization to json objects
        """
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        # iterate, extract & convert datetime values to a str in ISO format
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return dict(my_dict)

    def __str__(self):
        """
        returns a string representation of the class and its attributes.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
            )


if __name__ == "__main__":
    # creating a class instance and update it with a few attributes
    my_model = BaseModel()
    my_model.name = "Julien Kimba"
    my_model.julien_age = 37
    print(my_model.id)
    print(my_model)
    print(my_model.created_at)
    print("\n------- Serialized to dictionary below -------\n")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("\n------ JSON of <'my_model'> below ------\n")
    for key, value in my_model_json.items():
        print("\t{}: ({}) - {}".format(key, type(value), value))
    print("\n ------ deserialized to an instance below ------\n")
    # parse in the dictionary to the class constructor for deserialization
    new_model = BaseModel(**my_model_json)
    print(new_model.id)
    print(new_model)
    print(new_model.created_at)
    print("\n------ the two instanceses compared below -----\n")
    print(new_model is my_model)
