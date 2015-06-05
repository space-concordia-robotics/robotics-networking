import unittest

from roboticsnet.session import Session
from roboticsnet.commands.move_command import MoveCommand
from roboticsnet.commands.turn_command import TurnCommand
from roboticsnet.commands.reverse_command import ReverseCommand
from roboticsnet.command_hook import CommandHook

class TestCommands(unittest.TestCase):

    @staticmethod
    def _makeEmptyHook():
        return CommandHook()

    def testForwardCommand(self):
        MoveCommand(0x22, self._makeEmptyHook()).execute()

    def testReverseCommand(self):
        ReverseCommand(0x33, self._makeEmptyHook()).execute()

    def testTurnCommand(self):
        TurnCommand(0x44, self._makeEmptyHook()).execute()
