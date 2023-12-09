#!/usr/bin/python3
"""A Define the File Storage class"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """A class to handle all the storage related process"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all the created objects"""
        return self.__objects

    # def new(self, obj):
    # key = f"{obj.__class__.__name__}.{obj.id}"
    # self.__objects[key] = obj.to_dict()

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    # def save(self):
    # with open(self.__file_path, "w") as file:
    # json.dump(self.__objects, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
        except Exception as e:
            pass

    # def reload(self):
    # if os.path.exists(self.__file_path):
    # with open(self.__file_path, "r") as file:
    # x = json.load(file)
