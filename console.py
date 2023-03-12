#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

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

    def do_show(self, line):
        """
        print string representation of an instance based on class name and id
        show BaseModel 1234-1234-1234
        """
        print(line.split(" "))

    def do_destroy(self, line):
        """
        deletes an instance based on the class name and id
        """
        print("destroy ", line)

    def do_all(self, line):
        """
        """
        elements = storage.all()
        a_l = []
        if line:
            a = line.split(" ")[0]
            for key in elements.keys():
                if a == key.split(".")[0]:
                    a_l.append(elements[key])
            print(a_l)
        else:
            for key in elements.keys():
                a_l.append(elements[key])
            print(a_l)

    def do_update(self, line):
        """
        print updating
        """
        print("update ", line)

    def do_create(self, line):
        print("create : ", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
