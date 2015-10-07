from roboticsnet.commands.commandable import Commandable
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils

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
        values = []
        ms = self.session.get("monitoringService")

        values.append(ROBOTICSNET_COMMAND_SENSEINFO_RESP)

        for ix, service in enumerate(ms):
            values.append(ix)
            values.append(service.getValue())

        reply = ''.join(RoverUtils.hexArr2Str(values))
        self.remote_client.send_bytes(reply)

        # TODO hooks for this?
