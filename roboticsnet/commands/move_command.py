from roboticsnet.commands.commandable import Commandable

class MoveCommand(Commandable):
    """
    Send commands to turn the wheels left or right depending on values.

    author: psyomn
    """

    def __init__(self, value):
        self.magnitude = value

    def execute(self):
        print "Send things to motors"
