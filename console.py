import cmd

class HelloWorld(cmd.Cmd):
    def do_greet(self, line):
        print("hello", line)

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
