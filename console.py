#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    This class implemented:
        - quit and EOF to exit the program
        - help by default
        - a custom prompt: (hbnb)
        - an empty line + ENTER shouldn't execute anything

    Attribute:
        - prompt (str)
    """
    prompt = "(hbnb) "
    list_class = ['BaseModel']

    def do_quit(self):
        """quit command to exit the program
        """
        return True

    def do_EOF(self):
        """EOF signal to exit the program
        """
        return True

    def emptyline(self):
        """Do anything
        """
        pass

    def do_create(self, line):
        """create command to create a new instance
        """
        if line == "":
            print("** class name missing **")
        elif line not in self.list_class:
            print("** class doesn't exist **")
        else:
            var = BaseModel()
            var.save()
            print(var.id)

    def do_show(self, line):
        """show command to print the string representation of an instance
        """
        my_list = line.split(' ')
        key = "{}.{}".format(my_list[0], my_list[1])

        if line == "":
            print("** class name missing **")
        elif my_list[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(my_list) < 2:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[key])

    def do_destroy(self, line):
        """destroy command to delete an instance
        """
        my_list = line.split(' ')
        key = "{}.{}".format(my_list[0], my_list[1])
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(my_list) < 2:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()[key]
            models.storage.save()

    def do_update(self, line):
        my_list = line.split(' ')

    def do_all(self, line):
        """all command to print all string representation of all instance
        """
        my_list = line.split(' ')
        if line == "" or my_list[0] in self.list_class:
            my_list_str = []
            my_str = models.storage.all().items()
            for key, value in my_str:
                my_list_str.append(str(value))
            print("{}".format(my_list_str))
        elif my_list[0] not in self.list_class:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
