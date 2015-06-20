from roboticsnet.commands.commandable import Commandable

class TurnRightCommand(Commandable):
    """
    author: doomfest
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.turnRight, {'value':self.magnitude})
