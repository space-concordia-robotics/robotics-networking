from roboticsnet.commands.commandable import Commandable

class TurnCommand(Commandable):
    """
    author: psyomn
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        print "Send things to turn wheels left right"
        if not self.hooks == None:
            self.hooks.turnHook()
