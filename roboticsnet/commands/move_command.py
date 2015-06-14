from roboticsnet.commands.commandable import Commandable

class MoveCommand(Commandable):
    """
    Send commands to turn the wheels left or right depending on values.

    author: psyomn
    """

    def __init__(self, value, hooks):
        self.magnitude = value
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self.hooks.moveHook()
