#!/usr/bin/python3
"""

HBNB command reader

"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNB console
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        overrides default of executing last command with
        a no action when empty line is entered.
        """
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program.
        """
        return True

    def do_show(self, line):
        """
        print string representation of an instance based on class name and id
        show BaseModel 1234-1234-1234
        """
        a = line.strip().split(" ")
        if line == "":
            print("** class name missing **")
            return
        else:
            classes = globals().copy().keys()
            if not (a[0] in classes):
                print("** class doesn't exist **")
                return
        if len(a) == 1:
            print("** instance id missing **")
            return
        if len(a) == 2:
            key = "{}.{}".format(a[0], a[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        deletes an instance based on the class name and id
        """
        if line == "":
            print("** class name missing **")
            return
        className = line.split()[0]
        classes = globals().copy()
        if not (className in classes.keys()):
            print("** class doesn't exist **")
            return
        a = line.split()
        if len(a) < 2:
            print("** instance id missing **")
        if len(a) == 2:
            key = "{}.{}".format(a[0], a[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        """
        elements = storage.all()
        a_l = []
        if line:
            a = line.split(" ")[0]
            classes = globals().keys()
            if not (a in classes):
                print("** class doesn't exist **")
                return
            for key in elements.keys():
                if a == key.split(".")[0]:
                    a_l.append(str(elements[key]))
            print(a_l)
        else:
            for key in elements.keys():
                a_l.append(str(elements[key]))
            print(a_l)

    def do_update(self, line):
        """
        print updating
        """
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        className = args[0]
        classes = globals().copy()
        if not (className in classes.keys()):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            if not (key in storage.all()):
                print("** no instance found **")
                return
            else:
                instance = storage.all()[key]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr = args[2]
        value = args[3]
        value = type(getattr(instance, attr))(value)
        setattr(instance, attr, value)
        storage.save()

    def do_create(self, line):
        """
        test create model.

        """
        args = line.split()
        if line == "":
            print("** class name missing **")
            return
        else:
            classes = globals().copy()
            class_name = args[0]
            if class_name in classes.keys():
                obj = classes[class_name]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
