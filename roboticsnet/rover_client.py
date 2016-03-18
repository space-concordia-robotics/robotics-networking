from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.roboticsnet_exception import RoboticsnetException
import serial
import sys

class RoverClient:
    """
    The client that interfaces to the Rover gateway server. This is where we add
    different functions, that send the info to the server.

    author: psyomn
    """

    def __init__(self):
        portList = [x for x in RoverUtils.findPorts() if "ACM" not in x]
        #change this to portList[1] when testing antennas on the same computer
        if len(portList)>0:
            self.ser = serial.Serial(portList[0], 9600, timeout=1)
        else:
            self.ser = None

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
        """Writing to the serial port.
           The \n is so that ser.readline works on the other end"""
        self.ser.write(message+"\n")


    def query(self):
        """ Issue a queryproc request """
        message = RoverUtils.hexArr2Str([SYSTEM_QUERYPROC])
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
        self._sendMessage(message)


    def _sendMessageAwaitReply(self, message):
        """
        Waits for a reply after sending command.
        """
        self.ser.write(message+"\n")
        data = self.ser.readline()
        
        return data

    def sensInfo(self):
        """ Request information about sensors """
        message = RoverUtils.hexArr2Str([SENSOR_INFO])
        return self._sendMessageAwaitReply(message)

    def ping(self):
        """ Pings the rover with a timestamp """
        message = RoverUtils.hexArrToTimestampedString([SYSTEM_PING])
        return self._sendMessageAwaitReply(message)





