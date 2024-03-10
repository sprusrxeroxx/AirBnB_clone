#!/usr/bin/python3
""" A command interpreter to
manipulate the ojects of the app.
"""
from models import *
import json
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """ Defines a class to the entry point the command interpreter."""

    prompt = "(hbnb) "
    missing_class = "** class name missing **"
    missing_id = "** instance id missing **"
    missing_attr = "** attribute name missing **"
    missing_val = "** value missing **"
    unknown_class = "** class doesn't exist **"
    unknown_id = "** no instance found **"

    def emptyline(self):
        """ overides default emptyline execution """
        pass

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """ Exits the program with EOF command like cntrl+D
        """
        print()
        return True

    def do_create(self, line):
        """Function that creates new instance of BaseModel."""

        if line == "" or line is None:
            print("** class name missing **")

        elif line not in storage.classes():
            print("** class doesn't exist **")

        else:
            instance = storage.classes()[line]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Function that prints the string representation of an instance."""

        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                patt = "{}.{}".format(words[0], words[1])
                if patt not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[patt])

    def do_destroy(self, line):
        """Function that deletes an instance based on class name and id."""

        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                patt = "{}.{}".format(words[0], words[1])
                if patt not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[patt]
                    storage.save()

    def do_all(self, line):
        """Function that prints all string representation of an instance."""

        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            else:
                new_list = [str(obj) for patt, obj in storage.all().items()
                            if type(obj).__name__ == words[0]]
                print(new_list)

        else:
            f_list = [str(obj) for patt, obj in storage.all().items()]
            print(f_list)

    def do_update(self, line):
        """Function that updates an instance based on name and id"""

        if line == "" or line is None:
            print("** class name missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, line)
        cname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if not match:
            print("** class name missing **")

        elif cname not in storage.classes():
            print("** class doesn't exist **")

        elif uid is None:
            print("** instance id missing **")

        else:
            patt = "{}.{}".format(cname, uid)
            if patt not in storage.all():
                print("** no instance found **")

            elif not attribute:
                print("** attribute name missing **")

            elif not value:
                print("** value missing **")

            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float

                    else:
                        cast = int

                else:
                    value = value.replace('"', '')

                attributes = storage.attributes()[cname]
                if attribute in attributes:
                    value = attributes[attribute](value)

                elif cast:
                    try:
                        value = cast(value)

                    except ValueError:
                        pass

                setattr(storage.all()[patt], attribute, value)
                storage.all()[patt].save()

    def default(self, line):
        """Function that defines default shell behaviour"""

        self.console(line)

    def console(self, line):
        """Function that defines how shell interprets commands for classes"""

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return (line)

        cname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        uid_pattern = re.search('^"([^"]*)"(?:, (.*))?$', args)

        if uid_pattern:
            uid = uid_pattern.group(1)
            attr_or_dict = uid_pattern.group(2)

        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""

        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(cname, uid, match_dict.group(1))
                return ("")

            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)

            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")

        cmd = method + " " + cname + " " + uid + " " + attr_and_value
        self.onecmd(cmd)
        return (cmd)

    def do_count(self, line):
        """Counts the instances of a class."""

        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")

        elif words[0] not in storage.classes():
            print("** class doesn't exist **")

        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def update_dict(self, cname, uid, s_dict):
        """Function to search/set dict instances in JSON file."""

        delim = s_dict.replace("'", '"')
        word = json.loads(delim)

        if not cname:
            print("** class name missing **")

        elif uid is None:
            print("** instance id missing **")

        else:
            patt = "{}.{}".format(cname, uid)
            if patt not in storage.all():
                print("** no instance found **")

            else:
                attributes = storage.attributes()[cname]
                for attribute, value in word.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)

                    setattr(storage.all()[patt], attribute, value)

                storage.all()[patt].save()



    def do_destroy(self, args):
        """ Removes a saved instance based on class name and id"""
        if args == "" or args is None:
            print(self.missing_class)
        else:
            cmds = args.split(" ")
            cls_name = cmds[0]
            cls_id = cmds[1]

            # id arg check
            if len(cmds) < 2:
                print(self.missing_id)
            elif cls_name not in storage.class_link():
                print(self.unknown_class)
            else:
                val = "{}.{}".format(cls_name, cls_id)

                if val in storage.all():
                    storage.all().pop(val)
                else:
                    print(self.unknown_id)

    def do_all(self, args):
        """ Prints all stored args otherwise prints passed class name"""
        if args == "":
            # default behaviour to print everything in the file.json
            # if no args are passed
            my_list = []
            for _, values in storage.all().items():
                my_list.append(str(values))
                print(my_list)
        else:
            cmd = args.split(" ")[0]

            # if the cmd doesn't exist don't print it
            if cmd not in storage.class_link():
                print(self.unknown_class)
            else:
                my_list = []
                for _, values in storage.all().items():
                    if type(values).__name__ == cmd:
                        my_list.append(str(values))
                print(my_list)

    def do_update(self, args):
        if args == "" or args is None:
            print(self.missing_class)
        else:
            flags = args.split(" ")
            update_key = f"{flags[0]}.{flags[1]}"
            print(update_key)

            if len(flags) < 2:
                print(self.missing_id)
            elif update_key not in storage.all():
                print(self.unknown_id)
            elif len(flags) < 3:
                print(self.missing_attr)
            elif len(flags) < 4:
                print(self.missing_val)
            elif flags[0] not in storage.class_link():
                print(self.unknown_class)

            for key, _ in storage.all().items():
                if update_key == key:
                    setattr(storage.all()[key], flags[2], flags[3])
                    storage.all()[key].save()

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        #Non Interactive mode
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
