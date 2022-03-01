#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd


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

    def do_quit(self, line):
        """(quit): command that exit the program"""
        return True

    def do_EOF(self, line):
        """(EOF): signal that exit the program"""
        return True

    def emptyline(self):
        """Do anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
