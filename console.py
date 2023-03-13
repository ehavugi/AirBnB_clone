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
import re


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
        """return all"""
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
        if hasattr(instance, attr):
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

    def precmd(self, line):
        """
        Overide default response to get custom cmd processing.

        """

        if line != "":
            a = line.split('.')

            # Process the update command
            m = re.match(r"(\S+)\.update\((\S+), (\S+), (\S+)\)", line)
            if m:
                m = m.groups()
                m = [str(i).strip('\"') if type(i) == str else i for i in m]
                className = m[0]
                id_ = m[1]
                attrName = m[2]
                value = m[3]
                if className in globals():
                    new_ = "update {} {} {} {}".format(className,
                                                       id_, attrName, value)
                    return new_
                return line
            m = re.match(r"(\S+)\.update\((\S+),(.*)\)", line)

            if m:
                m = m.groups()
                m = [str(i).strip('\"') for i in m]
                if len(m) == 3:
                    className = m[0]
                    if not (className in globals()):
                        return line
                    id_ = m[1]
                    dict_ = eval(m[2])
                    cmd_ = ""
                    if type(dict_) == dict:
                        for key, value in dict_.items():
                            new = "update {} {} {} {}".format(className, id_,
                                                              key, value)
                            if cmd_ == "":
                                self.onecmd(new)
                        return ""
                    else:
                        print('Uuuh', m)
            if len(a) == 2 and a[1] == "count()":
                count = 0
                for key in storage.all().keys():
                    if key.split(".")[0] == a[0]:
                        count += 1
                print(count)
                return ""
            if len(a) == 2 and a[1] == "all()":
                if a[0] in globals():
                    return "all {}".format(a[0])
            if len(a) == 2 and a[1].startswith("show"):
                if a[0] in globals():
                    b = a[1].split('"')[1]
                    return "show {} {}".format(a[0], b)
            if len(a) == 2 and a[1].startswith("destroy"):
                if a[0] in globals():
                    b = a[1].split('"')[1]
                    return "destroy {} {}".format(a[0], b)
            return (line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
