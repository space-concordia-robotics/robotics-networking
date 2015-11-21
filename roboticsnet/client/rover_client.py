from multiprocessing.connection import Client
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.roboticsnet_exception import RoboticsnetException
import socket

class RoverClient:
    """
    The client that interfaces to the Rover gateway server. This is where we add
    different functions, that send the info to the server.

    author: psyomn
    """

    def __init__(self, host='localhost', port=ROBOTICSNET_PORT):
        self.host = host
        self.port = port

    def getPort(self):
        return self.port

    def getHost(self):
        return self.host

    def setHost(self, host):
        self.host = host

    def setPort(self, port):
        self.port = port

    #all of the movement commands will be send with UDP
    def forward(self, magnitude):
        """
        Parameters:
            magnitude - is a byte; 0x0 to 0xFF
        """
        self._validateByteValue(magnitude)
        message = RoverUtils.hexArr2Str([ROBOTICSNET_DRIVE_FORWARD, magnitude])
        self._sendMessage(message, False)

    def reverse(self, magnitude):
        """ Issue a reverse command """
        self._validateByteValue(magnitude)
        message = RoverUtils.hexArr2Str([ROBOTICSNET_DRIVE_REVERSE, magnitude])
        self._sendMessage(message, False)

    def forwardLeft(self, magnitude):
        """
        Parameters:
            magnitude - is a byte; 0x0 to 0xFF
        """
        self._validateByteValue(magnitude)
        message = RoverUtils.hexArr2Str([ROBOTICSNET_DRIVE_FORWARDLEFT, magnitude])
        self._sendMessage(message, False)

    def forwardRight(self, magnitude):
        """
        Parameters:
            magnitude - is a byte; 0x0 to 0xFF
        """
        self._validateByteValue(magnitude)
        message = RoverUtils.hexArr2Str([ROBOTICSNET_DRIVE_FORWARDRIGHT,magnitude])
        self._sendMessage(message, False)

    def reverseLeft(self, magnitude):
        """
        Parameters:
            magnitude - is a byte; 0x0 to 0xFF
        """
        self._validateByteValue(magnitude)
        message = RoverUtils.hexArr2Str([ROBOTICSNET_DRIVE_REVERSELEFT, magnitude])
        self._sendMessage(message, False)

    def reverseRight(self, magnitude):
        """
        Parameters:
            magnitude - is a byte; 0x0 to 0xFF
        """
        self._validateByteValue(magnitude)
        message = RoverUtils.hexArr2Str([ROBOTICSNET_DRIVE_REVERSERIGHT,magnitude])
        self._sendMessage(message, False)

    def stop(self):
        """ Issue a stop command """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_DRIVE_STOP])
        self._sendMessage(message)

    def query(self):
        """ Issue a queryproc request """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_SYSTEM_QUERYPROC])
        return self._sendMessageAwaitReply(message)

    def startVideo(self):
        """ Send a request to start the video process - what happens if there is
            already a running process is not dealt in this particular library """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_CAMERA_START_VID])
        self._sendMessage(message)

    def stopVideo(self):
        """ Send a request to stop the video process """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_CAMERA_STOP_VID])
        self._sendMessage(message)

    def snapshot(self):
        """ Sends a request to take a picture """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_CAMERA_SNAPSHOT])
        self._sendMessage(message)

    def panoramicSnapshot(self):
        """ Sends a request to take a panoramic snapshot """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_CAMERA_PANORAMICSNAPSHOT])
        self._sendMessage(message)

    def _sendMessage(self, message, TCP=True):
        """
        Given the host, and port, we build the connection. Don't call this
        outside the constructor, unless you know what you are doing.

        Parameters:
            message - is the bytearray to send, in string format
        """
        address = (self.host, self.port)
        if TCP:
            conn = Client(address)
            conn.send_bytes(message)
            conn.close()
        else:
            #from UdpCommunication on the Python wiki
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message, address)

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
        message = RoverUtils.hexArr2Str([ROBOTICSNET_SYSTEM_GRACEFUL])
        self._sendMessage(message)

    def sensInfo(self):
        """ Request information about sensors """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_SENSOR_INFO])
        return self._sendMessageAwaitReply(message)

    def _validateByteValue(self, value):
        """
        Check if value is between 0 to 255. If not, raise an exception

        Parameters:
            value - an integer.
        """
        if not value in range(0, 256):
            raise RoboticsnetException("You can send things in range of 0 to 255 only")

