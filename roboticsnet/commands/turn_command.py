from roboticsnet.commands.commandable import Commandable

class TurnCommand(Commandable):
    """
    author: psyomn
    """

    def __init__(self, value):
        self.magnitude = value

    def execute(self):
        print "Send things to turn wheels left right"
