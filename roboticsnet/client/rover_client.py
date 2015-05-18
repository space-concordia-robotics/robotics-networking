from multiprocessing.connection import Client
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils

class RoverClient:
    """
    The client that interfaces to the Rover gateway server. This is where we add
    different functions, that send the info to the server.

    author: psyomn
    """

    def __init__(self, host='localhost', port=ROBOTICSNET_PORT):
        """
        port: is the port we are sending to
        host: to who to connect - default is localhost
        """
        self.port = port
        self.host = host

    def getPort(self): return self.port
    def getHost(self): return self.host

    def move(self, magnitude):
        """ magnitude: is a byte; 0x0 to 0xFF"""
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_MOVE, magnitude])
        self._sendMessage(message)

    def turn(self, magnitude):
        """ magnitude: is a byte; 0x0 to 0xFF"""
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_TURN, magnitude])
        self._sendMessage(message)

    def query(self):
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_QUERYPROC])
        self._sendMessage(message)

    def _sendMessage(self, message):
        """
        Given the host, and port, we build the connection. Don't call this
        outside the constructor, unless you know what you are doing.

        message: is a string
        """
        address = (self.host, self.port)
        conn = Client(address)
        conn.send_bytes(message)
        conn.close()
