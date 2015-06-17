from roboticsnet.commands.commandable import Commandable

class TurnCommand(Commandable):
    """
    author: psyomn
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.turn, self.magnitude)
