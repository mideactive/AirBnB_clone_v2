#!/usr/bin/python3
"""
    Define class FileStorage
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        cls_obj = {}
        for key, obj in FileStorage.__objects.items():
            if cls == obj.__class__:
                cls_obj[key] = obj
        return cls_obj
=======
        '''
            Return the dictionary
        '''
        fs_objects = {}
        if cls:
            if type(cls) is str and cls in classes:
                for key, val in self.__objects.items():
                    if cls == key.split('.')[0]:
                        fs_objects[key] = val
            elif cls.__name__ in classes:
                for key, val in self.__objects.items():
                    if cls.__name__ == key.split('.')[0]:
                        fs_objects[key] = val
        else:
            return self.__objects
        return fs_objects
>>>>>>> 927552bc3540735800b7f3f34622ceaadcdafc70

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj.to_dict()
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
<<<<<<< HEAD
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except IOError:
            pass

    def delete(self, obj=None):
        """ Delete obj if exists
        """
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in FileStorage.__objects:
                del FileStorage.__objects[obj_key]

    def close(self):
        """deserializing the JSON file to objects
=======
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete object from __objects if it's inside
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]
        self.save()

    def close(self):
        """
        call reload
>>>>>>> 927552bc3540735800b7f3f34622ceaadcdafc70
        """
        self.reload()
