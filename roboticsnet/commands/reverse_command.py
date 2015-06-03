from roboticsnet.commands.commandable import Commandable

class ReverseCommand(Commandable):
    """
    Send commands to reverse the movement of the rover
    """

    def __init__(self, value):
        self.magnitude = value

    def execute(self):
        print "Send things to reverse motors"
