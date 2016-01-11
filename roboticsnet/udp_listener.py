import sys
import traceback
import threading
import socket

from rover_listener import RoverListener
from colorama import Fore
from multiprocessing import Process, Pipe
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.monitoring_service import MonitoringService

class UdpListener(threading.Thread):

    def __init__(self, default_port=10667, hook=None,
            monitorProcs=None):
        
        
        threading.Thread.__init__(self)
        self.port = default_port
        self.end_listen = False
        self.monitorServices = []
        self._spawnMonitoringServices(monitorProcs)
        #self.myLogger = Logger()
        self.commandable = hook #again, just a placeholder name. could be changed

    def run(self):

        address = ('', self.port)
        #UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(address)

        while not self.end_listen:
            try:
                #UDP
                received_bytes, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

                print "Received: ",
                print(Fore.GREEN + RoverUtils.hexArrToHumanReadableString(received_bytes))
                print(Fore.RESET)
                self.commandable.execute(received_bytes)

            except KeyboardInterrupt:
                """ User hits C^c """
                print "Shutting down ..."
                self.end_listen = True

            except:
                print "There was some error. Ignoring last command"
                print sys.exc_info()[0]
                print traceback.format_exc()
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
        #parent_conn.send(["done"])
        #parent_conn.close()
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

