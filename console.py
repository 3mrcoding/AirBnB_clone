#!/usr/bin/python3
"""File responsable of """

import cmd


class HBNBCommand(cmd.Cmd):
    """CMD CONSOLE CLASS"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    # alliasing
    do_EOF = do_quit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
