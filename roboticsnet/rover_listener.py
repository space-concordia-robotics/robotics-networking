from multiprocessing.connection import Listener

from roboticsnet.commands.command_factory import CommandFactory
from roboticsnet.sanitizer import sanitize
from roboticsnet.gateway_constants import *

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

    def listen(self):
        """ main entry point """
        print "Listening on port: ", self.port

        address = ('localhost', self.port)

        l = Listener(address)

        while not self.end_listen:
            conn = l.accept()
            bytes = conn.recv_bytes()
            print "Received: ", ' '.join(map(lambda x: hex(ord(x)), bytes))
            conn.close()
            if bytes[0] == ROBOTICSNET_COMMAND_GRACEFUL:
                self.end_listen = True
            else:
                cmd = CommandFactory.make_from_byte_array(bytes)
                cmd.execute()

        print "BYE."

