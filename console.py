#!/usr/bin/python3
"""File responsable of """

import cmd


class HBNBCommand(cmd.Cmd):
    """CMD CONSOLE CLASS"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
