from roboticsnet.commands.command_validator import validate
from roboticsnet.commands.forward_command import ForwardCommand
from roboticsnet.commands.turn_command import TurnCommand
from roboticsnet.commands.reverse_command import ReverseCommand
from roboticsnet.commands.queryproc_command import QueryprocCommand
from roboticsnet.commands.start_video_command import StartVideoCommand
from roboticsnet.commands.stop_video_command import StopVideoCommand
from roboticsnet.gateway_constants import *

class CommandFactory:
    """
    author: psyomn

    Consumes strings or byte arrays sent to service, and returns a command
    specific to that request
    """

    @staticmethod
    def makeFromByteArray(rcv_bytes, conn, session, hooks):
        """
        Parameters:
            rcv_bytes - the information that the client sends

            conn - the connection back to the client, which sent some request
              (some commands might need this information, as the protocol
              dictates a two-way communication channel).

            session - the current information that should be known about the
              status of the rover. See session.py

            hooks - if this is being as a library, we can add a hook here (note
              well single hook), that will be called, when the library receives
              the request, and the request is fully processed. In the end, the
              hooks are called.
        """
        cmd = ord(rcv_bytes[0])
        params = rcv_bytes[1:]

        if cmd == ROBOTICSNET_COMMAND_FORWARD:
            return CommandFactory._makeForward(params, hooks)

        elif cmd == ROBOTICSNET_COMMAND_REVERSE:
            return CommandFactory._makeReverse(params, hooks)

        elif cmd == ROBOTICSNET_COMMAND_TURN:
            return CommandFactory._makeTurn(params, hooks)

        elif cmd == ROBOTICSNET_COMMAND_QUERYPROC:
            return QueryprocCommand(conn, session, hooks)

        elif cmd == ROBOTICSNET_COMMAND_START_VID:
            return StartVideoCommand(hooks)

        elif cmd == ROBOTICSNET_COMMAND_STOP_VID:
            return StopVideoCommand(hooks)

    @staticmethod
    def _makeForward(rcv_bytes, hooks):
        magnitude = ord(rcv_bytes[0])
        return ForwardCommand(magnitude, hooks)

    @staticmethod
    def _makeTurn(rcv_bytes, hooks):
        magnitude = ord(rcv_bytes[0])
        return TurnCommand(magnitude, hooks)

    @staticmethod
    def _makeReverse(rcv_bytes, hooks):
        magnitude = ord(rcv_bytes[0])
        return ReverseCommand(magnitude, hooks)

