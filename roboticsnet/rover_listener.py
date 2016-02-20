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
from roboticsnet.command_validator import calculate_time_diff

class RoverListener():
    """
    author: psyomn

    The listener is basically the main entry point for this smaller module
    for the rover. It is responsible for receiving information, and passing it
    first to the validator, and then to the dispatcher.
    """

    def __init__(self, default_port=ROBOTICSNET_TCP_PORT,
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
        logging.info("TCP listening on port: %d" % (self.port))
        print "TCP listening on port: %d" % (self.port)

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

                readable = RoverUtils.hexArrToHumanReadableString(received_bytes)
                logging.info("{0}: {1}".format(addr, readable))
                print readable

                if ord(received_bytes[0]) == SYSTEM_GRACEFUL:
                    message = RoverUtils.hexArr2Str([SYSTEM_GRACEFUL])
                    sock2.sendto(message, ("localhost",10667))
                    self.end_listen = True
                elif ord(received_bytes[0]) == SYSTEM_PING:
                    diff = calculate_time_diff(ord(received_bytes[1]))
                    logging.info("Received ping from {0} in {1}s".format(addr, diff))
                    conn.send(str(diff))
                else:
                    self.commandable.execute(received_bytes)

            except AttributeError as e:
                logging.error("Attribute error on commandable execute. This is most likely because there is no commandable file to execute:\n\t{0}".format(e.message))
            except:
                logging.error("There was some error. Ignoring last command")
                logging.error(sys.exc_info()[0])
                logging.error(traceback.format_exc())

            finally:
                """ Conn might not be set if nothing is received """
                if 'conn' in vars() or 'conn' in globals():
                    conn.close()

        conn.close()
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
