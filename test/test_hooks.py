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

class Counter:
    def __init__(self):
        self.count = 0

    def incr(self):
        self.count += 1

    def get(self):
        return self.count

def freefunc():
    return True

def freefuncParams(params):
    return True

class TestHooks(unittest.TestCase):
    """ Test that the values have been received through hooks, and that if we
    supply hooks with parameters to get things from the parts of the protocol
    which do not expect anything, we get 'None' instead. """

    def testForwardCommand(self):
        vc = ValContainer()
        ForwardCommand(0x22, CommandHook(forward=vc.put)).execute()
        self.assertEqual(vc.get()["value"], 0x22)

    def testReverseCommand(self):
        vc = ValContainer()
        ReverseCommand(0x33, CommandHook(reverse=vc.put)).execute()
        self.assertEqual(vc.get()["value"], 0x33)

    def testTurnCommand(self):
        vc = ValContainer()
        TurnCommand(0x44, CommandHook(turn=vc.put)).execute()
        self.assertEqual(vc.get()["value"], 0x44)

    def testStartVideoCommand(self):
        vc = ValContainer()
        StartVideoCommand(CommandHook(startVideo=vc.put)).execute()
        self.assertEqual(vc.get(), None)

    def testStopVideoCommand(self):
        vc = ValContainer()
        StopVideoCommand(CommandHook(stopVideo=vc.put)).execute()
        self.assertEqual(vc.get(), None)

    def testMultipleCalls(self):
        c = Counter()
        for x in range(0, 100):
            ReverseCommand(0x33, CommandHook(reverse=c.incr())).execute()
        self.assertEqual(c.get(), 100)

    def testFreeFuncNoParams(self):
        """ TODO: maybe we can have some way to make sure the free func fired
        for sure. This could probably be done with glob vars ONLY IN THIS FILE
        of course"""
        ReverseCommand(0x33, CommandHook(reverse=freefunc)).execute()

    def testFreeFuncParams(self):
        """ TODO: maybe we can have some way to make sure the free func fired
        for sure. This could probably be done with glob vars ONLY IN THIS FILE
        of course"""
        ReverseCommand(0x33, CommandHook(reverse=freefuncParams)).execute()

