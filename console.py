#!/usr/bin/python3

"""Define console for AirBnB"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
