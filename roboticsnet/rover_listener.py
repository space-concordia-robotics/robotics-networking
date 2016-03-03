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
                    self.end_listen = True
                elif ord(received_bytes[0]) == SYSTEM_PING:
                    diff = calculate_time_diff(ord(received_bytes[1]))
                    logging.info("Received ping from {0} in {1}s".format(addr, diff))
                    self.ser.write(str(diff)+"\n")
                else:
                    self.commandable.execute(received_bytes)

            except AttributeError as e:
                logging.error("Attribute error on commandable execute. This is most likely because there is no commandable file to execute:\n\t{0}".format(e.message))
            except:
                logging.error("There was some error. Ignoring last command")
                logging.error(sys.exc_info()[0])
                logging.error(traceback.format_exc())

        self.ser.close()
        self._stopRunningServices()
        print "Server closed."

    def _stopRunningServices(self):
        """ If there exists any running services (like sensor polling
        functions), this method will stop them """
        print "Attempting to stop services"
        print self.monitorServices
        for service in self.monitorServices:
            print "Send stop to: ", service
            service.stop()
        for service in self.monitorServices:
            print "Join: ", service
            service.join()

    def stop(self):
        self.end_listen = True


    def _spawnMonitoringServices(self, monitorProcs):
        """ This starts all the monitoring services (as threads) """
        if not monitorProcs:
            return

        for lamb in monitorProcs:
            print "Init polling service [", lamb.func_name, "]"
            print "  [Service Info] ", lamb.__doc__
            monServ = MonitoringService(0, lamb)
            self.monitorServices.append(monServ)
            monServ.start()

        print "All services started"
