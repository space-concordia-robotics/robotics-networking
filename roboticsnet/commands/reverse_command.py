from roboticsnet.commands.commandable import Commandable

class ReverseCommand(Commandable):
    """
    Send commands to reverse the movement of the rover
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.reverse, {'value':self.magnitude})
