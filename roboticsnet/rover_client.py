from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.roboticsnet_exception import RoboticsnetException
from colorama import Fore
import serial
import sys

class RoverClient:
    """
    The client that interfaces to the Rover gateway server. This is where we add
    different functions, that send the info to the server.

    author: psyomn
    """

    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

    def sendCommand(self, command):
        """ Sends a request to the server """
        message = RoverUtils.hexArr2Str([command])
        self._sendMessage(message)


    def timedCommand(self, command, magnitude=0):
        """ Sends a request to the server """
        """ This is only for movement commands """
        if not magnitude in range(0, 65):
            raise RoboticsnetException("You can send things in range of 0 to 65 only")
        message = RoverUtils.hexArrToTimestampedString([command, magnitude])
        self._sendMessage(message) #sent with udp

    def _sendMessage(self, message):
        self.ser.write(message+"\n")
