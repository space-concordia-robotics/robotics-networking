from multiprocessing.connection import Listener

from roboticsnet.commands.command_factory import CommandFactory
from roboticsnet.sanitizer import sanitize

class RoverListener:
    """
    author: psyomn

    The listener is basically the main entry point for this smaller module
    for the rover. It is responsible for receiving information, and passing it
    first to the validator, and then to the dispatcher.
    """

    def __init__(self, default_port=5000):
        self.port = default_port

    def listen(self):
        """ main entry point """
        print "Listening on port: ", self.port

        address = ('localhost', self.port)

        l = Listener(address)

        # TODO add graceful shutdown?
        while True:
            conn = l.accept()
            print "Received: ", conn.recv_bytes()
            conn.close()

