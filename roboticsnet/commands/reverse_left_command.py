from roboticsnet.commands.commandable import Commandable

class ReverseLeftCommand(Commandable):
    """
    author: msnidal
    """

    def __init__(self, value, hooks, timediff):
        self.magnitude = value
        self.hooks = hooks
        self.timediff = timediff

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.reverseLeft, {'value':self.magnitude, 'timediff':self.timediff})
