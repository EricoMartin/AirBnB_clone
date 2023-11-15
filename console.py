#!/usr/bin/python3
""" The console Module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ A console class that contains the entry point of the
        command interpreter
    """
    prompt = (hbnb)


    def do_quit(self, arg):
    """Quit command to exit the program"""
        do_EOF()

    def do_EOF(self, line):
        return True

    def emptyline(self, line):
        return self.prompt

    if __name__ == '__main__':
    HBNBCommand().cmdloop()

