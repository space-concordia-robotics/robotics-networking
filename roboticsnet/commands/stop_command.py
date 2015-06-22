from roboticsnet.commands.commandable import Commandable

class StopCommand(Commandable):
    """
    author: doomfest
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.stop, {'value':self.magnitude})

