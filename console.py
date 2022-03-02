#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
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
    list_class = ['BaseModel', 'User']

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
        my_list = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            var = eval(my_list[0])()
            var.save()
            print(var.id)

    def do_show(self, line):
        """show command to print the string representation of an instance
        """
        my_list = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(my_list) < 2:
            print("** instance id missing **")
        else:
            my_dict = models.storage.all()
            key = "{}.{}".format(my_list[0], my_list[1])
            if key in my_dict:
                print(my_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """destroy command to delete an instance
        """
        my_list = line.split(' ')
        if line == "":
            print("** class name missing **")
        elif my_list[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(my_list) < 2:
            print("** instance id missing **")
        else:
            my_dict = models.storage.all()
            key = "{}.{}".format(my_list[0], my_list[1])
            if key in my_dict:
                del my_dict[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """all command to print all string representation of all instance
        """
        my_list = line.split(' ')
        if line == "" or my_list[0] in HBNBCommand.list_class:
            my_list_str = []
            my_str = models.storage.all().items()
            for key, value in my_str:
                if line == "" or type(value) is eval(my_list[0]):
                    my_list_str.append(str(value))
            print("{}".format(my_list_str))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
