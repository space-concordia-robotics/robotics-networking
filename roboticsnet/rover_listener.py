import sys
import traceback
import threading
import socket

from multprocessing import Process, Pipe
from colorama import Fore
from roboticslogger.logger import Logger
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.monitoring_service import MonitoringService
from commands import execute

class RoverListener:
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
        self.myLogger = Logger()
        self.commandable = hook #again, just a placeholder name. could be changed

    def listen(self):
        """ main entry point """
        print "Listening on port: ", self.port

        address = ('', self.port)
        
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(address)
        s.listen(1)
        conn, addr = s.accept()
        
        parent_conn, child_conn = Pipe()
        p = Process(target=myLogger.run, args=(child_conn,))
    
        p.start()
        
        while not self.end_listen:
            try:
                data = conn.recv(20)

                print "Received: ",
                print(Fore.GREEN + RoverUtils.hexArrToHumanReadableString(received_bytes))
                print(Fore.RESET)

                if ord(received_bytes[0]) == ROBOTICSNET_SYSTEM_GRACEFUL:
                    self.end_listen = True
                else:
                    self.commandable.execute(received_bytes)

            except KeyboardInterrupt:
                """ User hits C^c """
                print "Shutting down ..."
                self.end_listen = True
                

            except:
                parent_conn.send(["err", "There was some error. Ignoring last command"])
                parent_conn.send(["err", sys.exc_info()[0]])
                parent_conn.send(["err", traceback.format_exc())

            finally:
                """ It is the case that conn might not be set if nothing is
                received """
                if 'conn' in vars() or 'conn' in globals():
                    conn.close()
           
        self._stopRunningServices()
        print "BYE."

    def _stopRunningServices(self):
        """ If there exists any running services (like sensor polling
        functions), this method will stop them """
        print "Attempting to stop services"
        print self.monitorServices
        #stopping logger
        parent_conn.send(["done"])
        parent_conn.close()
        for service in self.monitorServices:
            print "Send stop to: ", service
            service.stop()
        for service in self.monitorServices:
            print "Join: ", service
            service.join()

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

