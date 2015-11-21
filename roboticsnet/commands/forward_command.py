from roboticsnet.commands.commandable import Commandable

class ForwardCommand(Commandable):
    """
    Send commands to turn the wheels left or right depending on values.

    author: psyomn
    """

    def __init__(self, value, hooks, timediff):
        self.magnitude = value
        self.hooks = hooks
        self.timediff = timediff

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.forward, {'value':self.magnitude,'timediff':self.timediff})
