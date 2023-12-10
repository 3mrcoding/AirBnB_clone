#!/usr/bin/python3
"""File responsable of """

import cmd
from models.base_model import BaseModel
from models import storage
import datetime
import re


class HBNBCommand(cmd.Cmd):
    """CMD CONSOLE CLASS"""

    prompt = "(hbnb) "
    clases = ["BaseModel"]

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Method creates a new object of any added Class"""
        if len(arg) <= 0:
            print("** class name missing **")
        elif arg not in self.clases:
            print(" ** class doesn't exist **")
        else:
            x = BaseModel()
            x.save()
            print(f"{x.id}")

    def do_show(self, arg):
        """Method prints object of a Class"""
        parts = arg.split()
        if len(parts) < 1:
            print("** class name missing **")
        elif parts[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(parts) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            itr = 0
            for obj_keys, obj_val in all_objs.items():
                if parts[1] == obj_val.id:
                    obj = all_objs[obj_keys]
                    print(obj)
                    itr += 1
                    break
            if itr == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Method deletes object of a Class"""
        parts = arg.split()
        if len(parts) < 1:
            print("** class name missing **")
        elif parts[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(parts) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            itr = 0
            for obj_keys, obj_val in all_objs.items():
                if parts[1] == obj_val.id:
                    del all_objs[obj_keys]
                    storage.save()
                    itr += 1
                    break
            if itr == 0:
                print("** no instance found **")

    def do_all(self, arg):
        """print all objects"""
        parts = arg.split()
        all_objs = storage.all()
        list = []
        if len(parts) < 1:
            for obj_val in all_objs.values():
                list.append(f"{obj_val}")
            print(list)

        elif len(parts) == 1 and parts[0] not in self.clases:
            print("** class doesn't exist **")

        elif len(parts) == 1 and parts[0] in self.clases:
            for obj_keys, obj_val in all_objs.items():
                parts2 = obj_keys.split(".")
                if parts2[0] == parts[0]:
                    list.append(f"{obj_val}")
            print(list)

    def do_update(self, arg):
        """update object attribute"""
        parts = arg.split()
        if len(parts) < 1:
            print("** class name missing **")
        elif parts[0] not in self.clases:
            print("** class doesn't exist **")
        elif len(parts) < 2:
            print("** instance id missing **")
        elif len(parts) < 3:
            print("** attribute name missing **")
        elif len(parts) < 4:
            print("** value missing **")
        elif len(parts) >= 4:
            all_objs = storage.all()
            for obj_keys, obj_val in all_objs.items():
                parts2 = obj_keys.split(".")
                if parts2[0] == parts[0]:
                    if parts2[1] == parts[1]:
                        att_value = re.findall(r'"(.*?)"', parts[3])
                        obj_val.__dict__[f"{parts[2]}"] = f"{att_value[0]}"
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
