from roboticsnet.commands.commandable import Commandable

class ForwardLeftCommand(Commandable):
    """
    author: msnidal
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.forwardLeft, {'value':self.magnitude})
