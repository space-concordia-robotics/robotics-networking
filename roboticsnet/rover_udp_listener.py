import sys
import traceback
import threading
import socket

from rover_listener import RoverListener
from colorama import Fore
from multprocessing import Process, Pipe
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.monitoring_service import MonitoringService

class UdpListener(RoverListener):

    def __init__(self, default_port=ROBOTICSNET_PORT, hook=None,
            monitorProcs=None):
        
        RoverListener.__init__(self, default_port=ROBOTICSNET_PORT, hook=None,
            monitorProcs=None)

    def listen(self):
        """ main entry point """
        print "Listening on port: ", self.port

        address = ('', self.port)
        #UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        parent_conn, child_conn = Pipe()
        p = Process(target=myLogger.run, args=(child_conn,))
    
        p.start()

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
