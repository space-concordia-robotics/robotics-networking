from roboticsnet.commands.commandable import Commandable

class ReverseRightCommand(Commandable):
    """
    author: doomfest
    """

    def __init__(self, value, hooks, timediff):
        self.magnitude = value
        self.hooks = hooks
        self.timediff = timediff

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.reverseRight, {'value':self.magnitude, 'timediff':self.timediff})
