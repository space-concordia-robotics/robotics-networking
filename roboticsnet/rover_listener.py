import sys
import traceback
import threading
import logging
import serial

from multiprocessing import Process, Pipe
from colorama import Fore
from roboticslogger.logger import Logger
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.monitoring_service import MonitoringService
from roboticsnet.command_validator import calculate_time_diff

class RoverListener():
    """
    author: psyomn

    The listener is basically the main entry point for this smaller module
    for the rover. It is responsible for receiving information, and passing it
    first to the validator, and then to the dispatcher.
    """

    def __init__(self, default_port=TCP_PORT,
            monitorProcs=None, hook=None):

        self.ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=None)
        self.end_listen = False
        self.commandable = hook #again, just a placeholder name. could be changed
        logging.basicConfig(filename='rover_listener.log',level=logging.DEBUG)


    def start(self):
        while not self.end_listen:
            try:
                received_bytes = self.ser.readline()
                readable = RoverUtils.hexArrToHumanReadableString(received_bytes)
                print "received",readable

                if ord(received_bytes[0]) == SYSTEM_GRACEFUL:
                    message = RoverUtils.hexArr2Str([SYSTEM_GRACEFUL])
                    self.end_listen = True
                else:
                    self.commandable.execute(received_bytes)
            except Exception as e:
                print e.message
