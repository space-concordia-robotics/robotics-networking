from roboticsnet.commands.commandable import Commandable

class QueryprocCommand(Commandable):
    """
    Transaction to query running processes (rover specific), and returns status

    Sorry for the crappy name. If it makes you feel better, some day I might
    have to name a child some day :o).

    Author:
        psyomn
    """

    def __init__(self, conn, session):
        """ Nothing fancy needed here """
        self.remote_client = conn
        self.session = session

    def execute(self):
        print "Do queries and send back stuff"
        cam1 = [0x0]
