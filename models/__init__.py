#!/usr/bin/python3

"""
links BaseModel and FileStorage to allow persistence
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()