from roboticsnet.commands.command_validator import validate
from roboticsnet.commands.move_command import MoveCommand
from roboticsnet.commands.turn_command import TurnCommand
from roboticsnet.commands.queryproc_command import QueryprocCommand
from roboticsnet.gateway_constants import *

class CommandFactory:
    """
    author: psyomn

    Consumes strings or byte arrays sent to service, and returns a command
    specific to that request
    """

    # TODO legacy: remove before milestone comes to a close
    @staticmethod
    def make_from_str(str):
        """ Pass the string that is received from the listener here, and the
        appropriate command will be created and returned"""

        if not validate(str):
            print "Received erroneous command: {", str, "}"
            return

        str_arr = str.split()

    @staticmethod
    def make_from_byte_array(bytes, conn, session):
        """
        Parameters:
            bytes - the information that the client sends

            conn - the connection back to the client, which sent some request
              (some commands might need this information, as the protocol
              dictates a two-way communication channel).

            session - the current information that should be known about the
              status of the rover. See session.py
        """
        cmd = ord(bytes[0])
        params = bytes[1:]

        if cmd == ROBOTICSNET_COMMAND_MOVE:
            print "Make move command"
            return CommandFactory._makeMove(params)

        elif cmd == ROBOTICSNET_COMMAND_TURN:
            print "Turn stuff"
            return CommandFactory._makeTurn(params)

        elif cmd == ROBOTICSNET_COMMAND_QUERYPROC:
            print "Query running processes"
            return QueryprocCommand(conn, session)

    @staticmethod
    def _makeMove(bytes):
        magnitude = ord(bytes[0])
        return MoveCommand(magnitude)

    @staticmethod
    def _makeTurn(bytes):
        magnitude = ord(bytes[0])
        return TurnCommand(magnitude)

