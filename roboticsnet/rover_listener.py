import sys
import traceback
import threading
import socket
import logging

from multiprocessing import Process, Pipe
from colorama import Fore
from roboticslogger.logger import Logger
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.monitoring_service import MonitoringService

class RoverListener():
    """
    author: psyomn

    The listener is basically the main entry point for this smaller module
    for the rover. It is responsible for receiving information, and passing it
    first to the validator, and then to the dispatcher.
    """

    def __init__(self, default_port=ROBOTICSNET_PORT,
            monitorProcs=None, hook=None):
        """
        default_port:
            The port that the server monitors on in default.
        
        hook:
            This is really just a placeholder name for the initialization of the Commands class the listener uses.

        monitorProcs:
            An array of lambdas, which have arity of 1 (they take in one
            parameter).


        author: psyomn
        """
        self.port = default_port
        self.end_listen = False
        self.monitorServices = []
        self._spawnMonitoringServices(monitorProcs)
        self.commandable = hook #again, just a placeholder name. could be changed
        logging.basicConfig(filename='rover_listener.log',level=logging.DEBUG)


    def start(self):
    
        """ main entry point """
        logging.info("listening on port: %d" % (self.port))

        address = ('', self.port)
        
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(address)
        s.listen(1)
        
        """To kill the Udp listener when this one receives graceful"""
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        while not self.end_listen:
            try:
                conn, addr = s.accept()
                received_bytes = conn.recv(1024)
                logging.info("Received: "+RoverUtils.hexArrToHumanReadableString(received_bytes))
                print RoverUtils.hexArrToHumanReadableString(received_bytes)
                
                if ord(received_bytes[0]) == ROBOTICSNET_SYSTEM_GRACEFUL:
                    message = RoverUtils.hexArr2Str([ROBOTICSNET_SYSTEM_GRACEFUL])
                    sock2.sendto(message, ("localhost",10667))
                    self.end_listen = True
                else:
                    self.commandable.execute(received_bytes)

            except:
                logging.error("There was some error. Ignoring last command")
                logging.error(sys.exc_info()[0])
                logging.error(traceback.format_exc())

            finally:
                """ Conn might not be set if nothing is received """
                if 'conn' in vars() or 'conn' in globals():
                    conn.close()
        self._stopRunningServices()
        print "BYE."

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

