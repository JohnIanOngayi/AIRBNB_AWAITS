#!/usr/bin/python3

"""
init module for models
Everytime models is accessed, this module runs 
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
