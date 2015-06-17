import unittest

from roboticsnet.session import Session
from roboticsnet.commands.forward_command import ForwardCommand
from roboticsnet.commands.turn_command import TurnCommand
from roboticsnet.commands.reverse_command import ReverseCommand
from roboticsnet.commands.start_video_command import StartVideoCommand
from roboticsnet.commands.stop_video_command import StopVideoCommand
from roboticsnet.command_hook import CommandHook

class ValContainer:
    def __init__(self):
        self.val = None

    def put(self, val):
        self.val = val

    def get(self):
        return self.val

class TestCommands(unittest.TestCase):
    """ Test that the values have been received through hooks """

    def testForwardCommand(self):
        vc = ValContainer()
        ForwardCommand(0x22, CommandHook(forward=vc.put)).execute()
        assert(vc.get()["value"], 0x22)

    def testReverseCommand(self):
        vc = ValContainer()
        ReverseCommand(0x33, CommandHook(reverse=vc.put)).execute()
        assert(vc.get()["value"], 0x33)

    def testTurnCommand(self):
        vc = ValContainer()
        TurnCommand(0x44, CommandHook(turn=vc.put)).execute()
        assert(vc.get()["value"], 0x44)

    def testStartVideoCommand(self):
        pass

    def testStopVideoCommand(self):
        pass
