#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    """Quit command to exit the program"""
    def do_quit(self):
        return True

    def help_quit(self):
	    print("\nQuit command to exit the program\n")

    def do_EOF(self):
        print("\n")
        return True

    def help_EOF(self):
	    print("\nEOF signal to quit the program\n")

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        #Non Interactive mode
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
