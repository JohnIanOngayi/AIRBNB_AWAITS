#!/usr/bin/python3

"""
Module contains class HBNBCommand that runs the program's front end
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class defines an interative shell
    """

    prompt = "(hbnb) "
    CLS = ["BaseModel", "User", "Amenity", "State", "City", "Place", "Review"]

    def do_quit(self):
        """
        Quits the Console
        """
        return True

    def do_EOF(self, line):
        """
        Quits the Console
        """
        print("")
        return True

    def do_create(self, line):
        """
        Creates an instance of BaseModel
        
        Parameters:
        line (str): string that comes after command 'create'
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line in HBNBCommand.CLS:
                obj = eval(line)()
                print(obj.id)
                obj.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints str representation of an instance

        Parameters:
        line (str): string after command that contains class and id
        """
        _class, _id = line.split()
        if len(line) == 0:
            print("** class name is missing **")
        else:
            if _class in HBNBCommand.CLS:
                if f"{_class}.{_id}" in FileStorage._FileStorage__objects.keys():
                    print(FileStorage._FileStorage__objects[f"{_class}.{_id}"])
                elif len(_id) == 0:
                    print("** instance id missing **")
                else:
                    print("** no instance found **")
            else:
                print ("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes instance based on class name and id

        Parameters:
        line (str): string after command that contains class and id
        """
        _class, _id = line.split()
        if len(line) == 0:
            print("** class name is missing **")
        else:
            if _class in HBNBCommand.CLS:
                if f"{_class}.{_id}" in FileStorage._FileStorage__objects.keys():
                    del FileStorage._FileStorage__objects[f"{_class}.{_id}"]
                elif len(_id) == 0:
                    print("** instance id missing **")
                else:
                    print("** no instance found **")
            else:
                print ("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints string representations of all istances of a class

        Parameters:
        line (str): string after command contaning the class name
        """
        _all = list()
        if line in HBNBCommand.CLS:
            for k, v in FileStorage._FileStorage__objects.items():
                _class, _id = k.split('.')
                if _class == line:
                    _all.append(v.__str__())
            print(f"{_all}")
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on class name and id

        Parameters:
        line (str): contains the object, attribute and if
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
