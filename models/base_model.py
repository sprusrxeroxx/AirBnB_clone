#!/usr/bin/python3

import datetime
import uuid

""""A Base model that defines all common attributes and methods for other classes"""

class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        updated_at = self.created_at

        


