from roboticsnet.commands.commandable import Commandable
from roboticsnet.rover_utils import RoverUtils
import itertools

class QueryprocCommand(Commandable):
    """
    Transaction to query running processes (rover specific), and returns status

    Sorry for the crappy name. If it makes you feel better, some day I might
    have to name a child some day :o).

    Author:
        psyomn
    """

    def __init__(self, conn, session, hooks):
        """ Nothing fancy needed here """
        self.remote_client = conn
        self.session = session
        self.hooks = hooks

    def execute(self):
        # TODO eventually we should remove dummy data
        cam1 = [0x01, 0x01]
        cam2 = [0x02, 0x02]
        cam3 = [0x03, 0x00]
        rovercore = [0x00, 0x01]

        import random
        mess_shuffle = [rovercore, cam1, cam2, cam3]
        random.shuffle(mess_shuffle)

        message_a = list(itertools.chain.from_iterable(mess_shuffle))

        message_str = ''.join(RoverUtils.hexArr2Str(message_a))

        self.remote_client.send_bytes(message_str)

        if self.hooks:
            self.hooks.queryprocHook()

