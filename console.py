#!/usr/bin/python3
""" The console Module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ A console class that contains the entry point of the
        command interpreter
    """
    prompt = "(hbnb)"


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ Returns the end of file """
        return True

    def emptyline(self, line):
        """ Override the emptyline method """
        return self.prompt

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

