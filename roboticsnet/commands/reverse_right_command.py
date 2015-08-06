from roboticsnet.commands.commandable import Commandable

class ReverseRightCommand(Commandable):
    """
    author: doomfest
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.reverseRight, {'value':self.magnitude})
