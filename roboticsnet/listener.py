class Listener:
    """
    author: psyomn

    The listener is basically the main entry point for this smaller module
    for the rover. It is responsible for receiving information, and passing it
    first to the validator, and then to the dispatcher.
    """

    def listen(port=5000):
        """ main entry point """
        print "Listening on port: ", port
