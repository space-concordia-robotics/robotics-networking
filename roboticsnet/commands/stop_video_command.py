from roboticsnet.commands.commandable import Commandable

class StopVideoCommand(Commandable):
    """ Sends stuff to the server, to tell it to stop doing video command
    stuff """

    def __init__(self, hooks):
        self.hooks = hooks

    def execute(self):
        self.hooks.stopVideoHook()
