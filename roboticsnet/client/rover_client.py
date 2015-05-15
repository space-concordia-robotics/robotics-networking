from multiprocessing.connection import Client
from roboticsnet.gateway_constants import *

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
        message = str(ROBOTICSNET_COMMAND_MOVE) +  str(magnitude)
        self._sendMessage(message)

    def turn(self, magnitude):
        message = [ROBOTICSNET_COMMAND_TURN, magnitude]
        self._sendMessage(message)

    def query(self):
        message = [ROBOTICSNET_COMMAND_QUERYPROC]
        self._sendMessage(message)

    def _sendMessage(self, message):
        """
        Given the host, and port, we build the connection. Don't call this
        outside the constructor, unless you know what you are doing.
        """
        address = (self.host, self.port)
        conn = Client(address)
        conn.send_bytes(message)
        conn.close()
