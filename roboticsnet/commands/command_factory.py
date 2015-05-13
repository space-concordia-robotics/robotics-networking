from roboticsnet.commands.command_validator import validate
from roboticsnet.commands import *
from roboticsnet.gateway_constants import *

class CommandFactory:
    """
    author: psyomn

    Consumes strings or byte arrays sent to service, and returns a command
    specific to that request
    """

    @staticmethod
    def make_from_str(str):
        """ Pass the string that is received from the listener here, and the
        appropriate command will be created and returned"""

        if not validate(str):
            print "Received erroneous command: {", str, "}"
            return

        str_arr = str.split()

    @staticmethod
    def make_from_byte_array(bytes):
        cmd = bytes[0]
        params = bytes[1:]

        if cmd == ROBOTICSNET_COMMAND_MOVE:
            print "Make move command"
            return _make_move(params)

        elif cmd == ROBOTICSNET_COMMAND_TURN:
            print "Turn stuff"

        elif cmd == ROBOTICSNET_COMMAND_QUERYPROC:
            print "Query running processes"

    @staticmethod
    def _make_move(bytes):
        magnitude = bytes[0]
        return MoveCommand(magnitude)
