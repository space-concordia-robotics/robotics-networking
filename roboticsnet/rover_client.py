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

    def __init__(self, host='localhost', tcp_port=ROBOTICSNET_TCP_PORT, udp_port=ROBOTICSNET_UDP_PORT):
        self.host = host
        self.tcp_port = tcp_port
        self.udp_port = udp_port

    def getPort(self, TCP = True):
        if (TCP):
            return self.tcp_port
        else:
            return self.udp_port

    def getHost(self):
        return self.host

    def setHost(self, host):
        self.host = host

    def setPort(self, port, TCP = True):
        if (TCP):
            self.tcp_port = port
        else:
            self.udp_port = port


    def query(self):
        """ Issue a queryproc request """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_SYSTEM_QUERYPROC])
        return self._sendMessageAwaitReply(message)

    def sendCommand(self, command):
        """ Sends a request to the server """
        message = RoverUtils.hexArr2Str([command])
        self._sendMessage(message)

    def timedCommand(self, command, magnitude=0):
        """ Sends a request to the server """
        """ This is only for movement commands """
        if not magnitude in range(0, 65):
            raise RoboticsnetException("You can send things in range of 0 to 255 only")
        message = RoverUtils.hexArrToTimestampedString([command, magnitude])
        self._sendMessage(message, False) #sent with udp

    def _sendMessage(self, message, TCP=True):
        """
        Given the host, and port, we build the connection. Don't call this
        outside the constructor, unless you know what you are doing.

        Parameters:
            message - is the bytearray to send, in string format
            TCP     - whether or not it will be sent with TCP. true by default
        """
        if TCP:
            address = (self.host, self.tcp_port)

            print "Using port: " + Fore.GREEN, self.tcp_port, Fore.RESET
            print "Using host: " + Fore.GREEN, self.host, Fore.RESET

            #from TCPCommunication on the Python wiki
            tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tsock.connect(address)
            tsock.send(message)
            tsock.close()
        else:
            #from UdpCommunication on the Python wiki
            print "Using port: " + Fore.GREEN, self.udp_port, Fore.RESET
            print "Using host: " + Fore.GREEN, self.host, Fore.RESET

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message, (self.host,self.udp_port))

    def _sendMessageAwaitReply(self, message):
        """
        As _sendMessage, but this method waits for a reply

        Parameters:
            message - is the bytearray to send, in string format
        """
        address = (self.host, self.tcp_port)
        tsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tsock.connect(address)
        tsock.send(message)
        data = tsock.recv(20)
        tsock.close()
        return data

    def sensInfo(self):
        """ Request information about sensors """
        message = RoverUtils.hexArr2Str([ROBOTICSNET_SENSOR_INFO])
        return self._sendMessageAwaitReply(message)
