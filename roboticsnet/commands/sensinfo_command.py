from roboticsnet.commands.commandable import Commandable

class SensinfoCommand(Commandable):
    """
    Sensor info command. A request is received to send back any and all
    information from the sensors.

    author: psyomn
    """

    def __init__(self, conn, session, hooks):
        self.remote_client = conn
        self.session = session
        self.hooks = hooks

    def execute(self):
        print "Execute sensinfo command"
