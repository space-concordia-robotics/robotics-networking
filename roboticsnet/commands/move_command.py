from roboticsnet.commands.commandable import Commandable

class MoveCommand(Commandable):
    """
    author: psyomn
    """

    def __init__(self, value):
        self.magnitude = value

    def execute(self):
        print "Send things to motors"
