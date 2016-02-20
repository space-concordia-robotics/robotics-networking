import sys
import traceback
import threading
import socket
import logging

from rover_listener import RoverListener
from colorama import Fore
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.monitoring_service import MonitoringService

class UdpListener(RoverListener):

    def __init__(self, default_port=ROBOTICSNET_UDP_PORT, hook=None,
            monitorProcs=None):


        self.port = default_port
        self.end_listen = False
        self.monitorServices = []
        self._spawnMonitoringServices(monitorProcs)
        self.commandable = hook #again, just a placeholder name. could be changed
        logging.basicConfig(filename='udp_listener.log',level=logging.DEBUG)

    def start(self):
        logging.info("UDP listening on port: %d" % (self.port))
        print "UDP listening on port:",self.port


        address = ('', self.port)
        #UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(address)

        while not self.end_listen:
            try:
                #UDP
                received_bytes, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
                logging.info("Received: "+RoverUtils.hexArrToHumanReadableString(received_bytes))
                print "Received: "+RoverUtils.hexArrToHumanReadableString(received_bytes)
                if ord(received_bytes[0]) == SYSTEM_GRACEFUL:
                    self.end_listen = True
                else:
                    try:
                        self.commandable.execute(received_bytes)
                    except AttributeError as e:
                        logging.error("Attribute error on commandable execute. This is most likely because there is no commandable file to execute:\n\t{0}".format(e.message))
                    except Exception as e:
                        logging.error("Critical error executing command:\n\t{0}".format(e.message))


            except KeyboardInterrupt:
                """ User hits C^c """
                print "Shutting down ..."
                self.end_listen = True

            except:
                print "There was some error. Ignoring last command"
                print sys.exc_info()[0]
                print traceback.format_exc()
            finally:
                """conn might not be set if nothing is
                received """
                if 'conn' in vars() or 'conn' in globals():
                    conn.close()
        self._stopRunningServices()
        conn.close()
