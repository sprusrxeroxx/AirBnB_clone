#!/usr/bin/python3

import datetime
import uuid

""""
    A Base model that defines all common attributes and methods for other classes
"""

class BaseModel:


    def __init__(self, *args, **kwargs):


        if kwargs:
            del kwargs["__class__"]
            for key, val in kwargs.items():

             # grab date and time stamps and convert them to datetime objec
                if key == "created_at" or key == "updated_at":
                    dt_object = datetime.datetime.strftime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dt_object)
                else:
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()


    def save_update(self):
        self.updated_at = datetime.datetime.now()
        return self.updated_at

    def save_dict(self):
        dictForm = {}

        dictForm["__class__"] = self.__class__.__name__

        for key, val in self.__dict__.items():
        # get the values which are of datetime object type
            if isinstance(val, type(datetime)):
        #convert them to string objects in ISO format
                dictForm[key] = val.isoformat()
            else:
                dictForm[key] = val
        return dictForm

    def __str__(self):
         return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"




         
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "Julien Kimba"
    my_model.julien_age = 37
    print(my_model)
    my_model.save_update()
    print("\n=== dictionary representatio ===\n")
    my_model_json = my_model.save_dict()
    print(my_model_json)
    print("\nJSON of my_model:\n")
    for key, value in my_model_json.items():
        print("\t{}: ({}) - {}".format(key, type(value), value))



