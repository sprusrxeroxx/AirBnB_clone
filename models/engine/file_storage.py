#!/usr/bin/python3
"""
Module that contains class for storage and persistence between
sessions which is vital for an application such as this
"""
import json
import os


class FileStorage:
    """
    FileStorage class contains methods and private class attributes
    that handle persistency and storage between sessions.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This simply returns all objects that have been saved in the
        form of a dictionary. This is useful for passing between
        sessions
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Create a new dictionary that will most likely be added to the
        __objects dictionary as a whole.
        Args:
            obj: the new obj to add which will be converted to a
                dictionary
        """
        key_name = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key_name] = obj

    def save(self):
        """
        Write the new object to the file that stores all the dictionary
        entries as a way to save items and persistency
        """
        my_dict = {}
        with open(FileStorage.__file_path, "w", encoding="utf8") as JSONfile:
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, JSONfile)

    def class_link(self):
        """
        Returns a dictionary that contains a map of class names and
        their respective classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity

        cls_link = {
                "BaseModel": BaseModel,
                "User": User,
                "City": City,
                "State": State,
                "Place": Place,
                "Review": Review,
                "Amenity": Amenity
        }
        return cls_link

    def reload(self):
        """
        reads from a file all serialised objects, converts
        them from json format to a dictionary and assigns the __objects
        attributed to them
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for objs in data.values():
                    cls_key = objs["__class__"]
                    cls_name = self.class_link()[cls_key]
                    self.new(cls_name(**objs))
        except FileNotFoundError:
            pass
