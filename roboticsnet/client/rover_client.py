import roboticsnet.gateway_constants

class RoverClient:
    """
    The client that interfaces to the Rover gateway server. This is where we add
    different functions, that send the info to the server.

    author: psyomn
    """

    def __init__(self, port=ROBOTICSNET_PORT):
        self.port = port

    def move(self, magnitude):
        pass
