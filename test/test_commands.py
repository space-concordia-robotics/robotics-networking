import unittest

from roboticsnet.session import Session
from roboticsnet.commands.move_command import MoveCommand
from roboticsnet.commands.turn_command import TurnCommand
from roboticsnet.commands.reverse_command import ReverseCommand
from roboticsnet.commands.start_video_command import StartVideoCommand
from roboticsnet.commands.stop_video_command import StopVideoCommand
from roboticsnet.command_hook import CommandHook

class TestCommands(unittest.TestCase):
    """ These just make sure that the commands, once executed, don't raise exceptions
        TODO: testhooks - hooks should also have parameters being passed - need
        to fix this
    """

    @staticmethod
    def _makeEmptyHook():
        return CommandHook()

    def testForwardCommand(self):
        MoveCommand(0x22, self._makeEmptyHook()).execute()

    def testReverseCommand(self):
        ReverseCommand(0x33, self._makeEmptyHook()).execute()

    def testTurnCommand(self):
        TurnCommand(0x44, self._makeEmptyHook()).execute()

    def testStartVideoCommand(self):
        StartVideoCommand(self._makeEmptyHook()).execute()

    def testStopVideoCommand(self):
        StopVideoCommand(self._makeEmptyHook()).execute()
