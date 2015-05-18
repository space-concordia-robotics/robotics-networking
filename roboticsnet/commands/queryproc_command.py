from roboticsnet.commands.commandable import Commandable

class QueryprocCommand(Commandable):
    """
    Transaction to query running processes (rover specific), and returns status

    Sorry for the crappy name. If it makes you feel better, some day I might
    have to name a child :o).

    Author:
        psyomn
    """

    def __init__(self):
        """ Nothing fancy needed here """
        pass

    def execute(self):
        print "Do queries and send back stuff"
