from roboticsnet.commands.commandable import Commandable

class PanoramicSnapshotCommand(Commandable):
    """Sends a request to take a panoramic photo on the rover"""

    def __init__(self, hooks):
        self.hooks = hooks

    def execute(self):
        if self.hooks:
            self._runHook(self.hooks.panoramicSnapshot, None)
