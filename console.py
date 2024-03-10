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

            class_name = commands[0]
            if class_name in storage.class_link():
                # create a new instance based on the class name
                new_instance = storage.class_link()[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print(self.unknown_class)

    def do_show(self, args):
        """ extract and show instance str representation by id and class name"""
        if args == "" or args is None:
            print(self.missing_class)
        else:
            cmds = args.split(" ")
            cls_name = cmds[0]

            # id arg checker
            if len(cmds) < 2:
                print(self.missing_id)
            elif cls_name not in storage.class_link():
                print(self.unknown_class)
            else:
                cls_id = cmds[1]
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
