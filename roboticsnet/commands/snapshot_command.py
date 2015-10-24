from roboticsnet.commands.commandable import Commandable

class SnapshotCommand(Commandable):
    """Sends a request to take a snapshot"""

    def __init__(self, hooks):
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.snapshot, None)
