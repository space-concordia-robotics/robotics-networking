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
        Parameters:
            port - is the port we are sending to
            host - to who to connect - default is localhost
        """
        self.port = port
        self.host = host

    def getPort(self): return self.port
    def getHost(self): return self.host

    def forward(self, magnitude):
        """
        Parameters:
            magnitude - is a byte; 0x0 to 0xFF
        """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_FORWARD, magnitude])
        self._sendMessage(message)

    def turn(self, magnitude):
        """
        Parameters:
            magnitude - is a byte; 0x0 to 0xFF
        """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_TURN, magnitude])
        self._sendMessage(message)

    def query(self):
        """ Issue a queryproc request """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_QUERYPROC])
        return self._sendMessageAwaitReply(message)

    def reverse(self, magnitude):
        """ Issue a reverse command """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_REVERSE, magnitude])
        return self._sendMessage(message)

    def startVideo(self):
        """ Send a request to start the video process - what happens if there is
            already a running process is not dealt in this particular library """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_START_VID])
        self._sendMessage(message)

    def stopVideo(self):
        """ Send a request to stop the video process """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_STOP_VID])
        self._sendMessage(message)

    def _sendMessage(self, message):
        """
        Given the host, and port, we build the connection. Don't call this
        outside the constructor, unless you know what you are doing.

        Parameters:
            message - is the bytearray to send, in string format
        """
        address = (self.host, self.port)
        conn = Client(address)
        conn.send_bytes(message)
        conn.close()

    def _sendMessageAwaitReply(self, message):
        """
        As _sendMessage, but this method waits for a reply

        Parameters:
            message - is the bytearray to send, in string format
        """
        address = (self.host, self.port)
        conn = Client(address)
        conn.send_bytes(message)
        rcv = conn.recv_bytes()
        conn.close()
        return rcv

    def graceful(self):
        """ Tell the server to gracefully shutdown. """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_COMMAND_GRACEFUL])
        self._sendMessage(message)

