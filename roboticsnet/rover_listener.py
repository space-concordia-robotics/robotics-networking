import traceback

from multiprocessing.connection import Listener

from roboticsnet.commands.command_factory import CommandFactory
from roboticsnet.sanitizer import sanitize
from roboticsnet.session import Session
from roboticsnet.gateway_constants import *
from roboticsnet.rover_utils import RoverUtils

class RoverListener:
    """
    author: psyomn

    The listener is basically the main entry point for this smaller module
    for the rover. It is responsible for receiving information, and passing it
    first to the validator, and then to the dispatcher.
    """

    def __init__(self, default_port=ROBOTICSNET_PORT):
        self.port = default_port
        self.end_listen = False
        self.session = Session()

    def listen(self):
        """ main entry point """
        print "Listening on port: ", self.port

        address = ('localhost', self.port)

        l = Listener(address)

        while not self.end_listen:
            try:
                conn = l.accept()
                bytes = conn.recv_bytes()
                print "Received: ", RoverUtils.hexArrToHumanReadableString(bytes)
                if ord(bytes[0]) == ROBOTICSNET_COMMAND_GRACEFUL:
                    self.end_listen = True
                else:
                    cmd = CommandFactory.make_from_byte_array(
                            bytes, conn, self.session)
                    cmd.execute()

                conn.close()

            except KeyboardInterrupt:
                print "Shutting down ..."
                self.end_listen = True

            except:
                # TODO: logging would be a good idea here
                print "There was some error. Ignoring last command"
                print traceback.format_exc()


        print "BYE."

