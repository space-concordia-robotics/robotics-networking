from roboticsnet.commands.commandable import Commandable

class StopCommand(Commandable):
    """
    author: doomfest
    """

    def __init__(self, hooks, timediff):
        self.hooks = hooks
        self.timediff = timediff

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.stop, {'timediff':self.timediff})
