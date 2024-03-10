#!/usr/bin/python3

from models.base_model import BaseModel
from json import dump
from json import load

class FileStorage:
    __file_path = "file.json"
    __objects = {}

def all(self):
    # returns the dictionary __objects
    return FileStorage__objects

def new(self, obj):
 # set the key-value pair in __objects (class.id as key, obj as the value)
   FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

def save(self):
    # declaree an empty dictionary to hold the object we are serializing
    dictObj = {}
    # loop and grab the objects (key-value pair) we stored in __objects
    for key, val in FileStorage.__objects.items():
    # convert the values to a dictionary using our save_to_dict() method
        dictObj[key] = val.save_to_dict()
        # open the file path for writing (serialization)
        with open(FileStorage.__filePath, "w", encoding="utf-8") as jsonF:                                                   
        # dump the serialized object into the file
            dump(dictObj, jsonF)

from json import load

def reload(self):

    # dictionary to hold all our defined classes (user-defined)
    definedClasses = {'BaseModel': BaseModel}

    # Attempt to open the Json file in the filePath
    try:
        with open(FileStorage.__filePath, encoding-"utf-8") as jsonStr:
        # deserialize the JSON string in the file at the file path
            deserialized = load(jsonStr)
            # Iterate over each obj's value in the deserialized dictionary
            for obj_values in deserialized.values():
                # get obj's class name from the '__class__' key
                clsName = obj_values["__class__"]
            # get the actual class object in the definedClasses dictionary
                cls_obj = definedClasses[clsName]
                # Create a new class instance with the object's values as                                                                                                                                                                              
                # its arguments
                self.new(cls_obj(**obj_values))
    # Catch  FileNotFoundError and ignore if theres no file to deserialize
                
    except FileNotFoundError:
        pass





