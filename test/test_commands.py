import unittest

from roboticsnet.session import Session
from roboticsnet.commands.forward_command import ForwardCommand
from roboticsnet.commands.reverse_command import ReverseCommand
from roboticsnet.commands.start_video_command import StartVideoCommand
from roboticsnet.commands.stop_video_command import StopVideoCommand
from roboticsnet.command_hook import CommandHook
from roboticsnet.commands.forward_left_command import ForwardLeftCommand
from roboticsnet.commands.forward_right_command import ForwardRightCommand
from roboticsnet.commands.reverse_left_command import ReverseLeftCommand
from roboticsnet.commands.reverse_right_command import ReverseRightCommand

class TestCommands(unittest.TestCase):
    """ These just make sure that the commands, once executed, don't raise exceptions
        TODO: testhooks - hooks should also have parameters being passed - need
        to fix this
    """

    @staticmethod
    def _makeEmptyHook():
        return CommandHook()

    def testForwardCommand(self):
        ForwardCommand(0x22, self._makeEmptyHook()).execute()

    def testReverseCommand(self):
        ReverseCommand(0x33, self._makeEmptyHook()).execute()

    def testForwardLeftCommand(self):
        ForwardLeftCommand(0x44, self._makeEmptyHook()).execute()

    def testForwardRightCommand(self):
        ForwardRightCommand(0x44, self._makeEmptyHook()).execute()

    def testReverseLeftCommand(self):
        ReverseLeftCommand(0x55, self._makeEmptyHook()).execute()

    def testReverseRightCommand(self):
        ReverseRightCommand(0x55, self._makeEmptyHook()).execute()

    def testStartVideoCommand(self):
        StartVideoCommand(self._makeEmptyHook()).execute()

    def testStopVideoCommand(self):
        StopVideoCommand(self._makeEmptyHook()).execute()
