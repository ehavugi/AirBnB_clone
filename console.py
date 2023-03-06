#!/usr/bin/python3
import cmd

"""
HBNB command reader
"""


class HBNBCommand(cmd.Cmd):
    """
    HBNB console
    """
    prompt = "(hbnb) "

    def do_exit(self, line):
        """
        exit the console.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the console.

        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
