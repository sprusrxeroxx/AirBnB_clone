#!/usr/bin/python3
""" A command interpreter to
manipulate the ojects of the app.
"""
import cmd
from models import storage


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

    def do_create(self, args):
        """ Create new class instance, save and display its id"""
        if args == "" or args is None:
            print(self.missing_class)
        else:
            commands = args.split(" ")

            class_name = self.extract_arg(commands[0])
            if class_name in storage.class_link():
                # create a new instance based on the class name
                new_instance = storage.class_link()[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print(self.unknown_class)

    # GOD ABEG
    def do_show(self, args):
        """ Get and print instance str representation by id and class name"""
        if args == "" or args is None:
            print(self.missing_class)
        else:
            cmds = args.split(" ")
            cls_name = self.extract_arg(cmds[0])

            # id arg checker
            if len(cmds) < 2:
                print(self.missing_id)
            elif cls_name not in storage.class_link():
                print(self.unknown_class)
            else:
                cls_id = self.extract_arg(cmds[1])
                val = "{}.{}".format(cls_name, cls_id)

                if val in storage.all():
                    print(storage.all()[val])
                else:
                    print(self.unknown_id)

    def do_destroy(self, args):
        """ Removes a saved instance based on class name and id"""
        if args == "" or args is None:
            print(self.missing_class)
        else:
            cmds = args.split(" ")
            cls_name = self.extract_arg(cmds[0])
            cls_id = self.extract_arg(cmds[1])

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
            cmd = self.extract_arg(args.split(" ")[0])

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
            update_key = "{}.{}".format(self.extract_arg(flags[0]),
                                        self.extract_arg(flags[1]))
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
    # HELPERS
    def extract_arg(self, arg="", msg=""):
        """Given a string it returns the string itself or extracts
        the values of the string in between the quotes

        Example:
            "hello" returns hello
            'hello' returns hello

        Args:
            arg: the argument
            msg: the message to print if extraction unsuccessful
        """
        # extract the text between string quotes
        # now to match the braces for a correct formatted str
        # IF WE GET A LOT OF RED CHECKS FOR TASK 7 CONSIDER
        # REMOVING CALLS TO THIS FUNCTION AND JUST PASSING
        # THEM STRAIGHT AWAY
        if '"' in arg or '\'' in arg:
            return arg[1:-1]
        else:
            return arg

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        #Non Interactive mode
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
