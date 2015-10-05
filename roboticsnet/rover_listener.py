import traceback
import threading

from multiprocessing.connection import Listener
from colorama import Fore

from roboticsnet.commands.command_factory import CommandFactory
from roboticsnet.sanitizer import sanitize
from roboticsnet.session import Session
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils
from roboticsnet.monitoring_service import MonitoringService

class RoverListener:
    """
    author: psyomn

    The listener is basically the main entry point for this smaller module
    for the rover. It is responsible for receiving information, and passing it
    first to the validator, and then to the dispatcher.
    """

    def __init__(self, default_port=ROBOTICSNET_PORT, hooks=None,
            monitorProcs=None):
        """
        default_port:
            The port that the server monitors on in default.

        hooks:
            Depending on what we receive on the server, we can bind different
            behavior. There's two examples you can consult and see how this
            mechanism works in robotics-networking/examples.

        monitorProcs:
            An array of lambdas, which have arity of 1 (they take in one
            parameter).

            On top of hooks, we define some functions to be executed on and on
            during the whole lifetime of the system. These should be able to set
            some value, and return that value when these services are asked for
            system information.

        author: psyomn
        """
        self.port = default_port
        self.end_listen = False
        self.session = Session()
        self.hooks = hooks
        self.monitorServices = []
        self._spawnMonitoringServices(monitorProcs)

    def listen(self):
        """ main entry point """
        print "Listening on port: ", self.port

        address = ('', self.port)

        l = Listener(address)

        while not self.end_listen:
            try:
                conn = l.accept()
                received_bytes = conn.recv_bytes()

                print "Received: ",
                print(Fore.GREEN + RoverUtils.hexArrToHumanReadableString(received_bytes))
                print(Fore.RESET)

                if ord(received_bytes[0]) == ROBOTICSNET_COMMAND_GRACEFUL:
                    self.end_listen = True
                else:
                    cmd = CommandFactory.makeFromByteArray(\
                            received_bytes,
                            conn,
                            self.session,
                            self.hooks)
                    cmd.execute()

            except KeyboardInterrupt:
                """ User hits C^c """
                print "Shutting down ..."
                self.end_listen = True

            except:
                # TODO: logging would be a good idea here
                print "There was some error. Ignoring last command"
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

