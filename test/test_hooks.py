import unittest

from roboticsnet.session import Session
from roboticsnet.commands.forward_command import ForwardCommand
from roboticsnet.commands.forward_left_command import ForwardLeftCommand
from roboticsnet.commands.forward_right_command import ForwardRightCommand
from roboticsnet.commands.reverse_left_command import ReverseLeftCommand
from roboticsnet.commands.reverse_right_command import ReverseRightCommand
from roboticsnet.commands.reverse_command import ReverseCommand
from roboticsnet.commands.start_video_command import StartVideoCommand
from roboticsnet.commands.stop_video_command import StopVideoCommand
from roboticsnet.commands.snapshot_command import SnapshotCommand
from roboticsnet.commands.panoramic_snapshot_command import PanoramicSnapshotCommand

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

freeFuncFired = False
freeFuncParamsFired = False

def freefunc():
    global freeFuncFired
    freeFuncFired = True
    return True

def freefuncParams(params):
    global freeFuncParamsFired
    freeFuncParamsFired = True
    return True

class TestHooks(unittest.TestCase):
    """ Test that the values have been received through hooks, and that if we
    supply hooks with parameters to get things from the parts of the protocol
    which do not expect anything, we get 'None' instead. """

    def testForwardCommand(self):
        vc = ValContainer()
        ForwardCommand(0x22, CommandHook(forward=vc.put), 0).execute()
        self.assertEqual(vc.get()["value"], 0x22)

    def testReverseCommand(self):
        vc = ValContainer()
        ReverseCommand(0x33, CommandHook(reverse=vc.put), 12).execute()
        self.assertEqual(vc.get()["value"], 0x33)

    def testForwardLeftCommand(self):
        vc = ValContainer()
        ForwardLeftCommand(0x44, CommandHook(forwardLeft=vc.put), 2).execute()
        self.assertEqual(vc.get()["value"], 0x44)

    def testForwardRightCommand(self):
        vc = ValContainer()
        ForwardRightCommand(0x44, CommandHook(forwardRight=vc.put), 22).execute()
        self.assertEqual(vc.get()["value"], 0x44)

    def testReverseLeftCommand(self):
        vc = ValContainer()
        ReverseLeftCommand(0x55, CommandHook(reverseLeft=vc.put), 500).execute()
        self.assertEqual(vc.get()["value"], 0x55)

    def testReverseRightCommand(self):
        vc = ValContainer()
        ReverseRightCommand(0x55, CommandHook(reverseRight=vc.put), 12).execute()
        self.assertEqual(vc.get()["value"], 0x55)

    def testStartVideoCommand(self):
        vc = ValContainer()
        StartVideoCommand(CommandHook(startVideo=vc.put)).execute()
        self.assertEqual(vc.get(), None)

    def testStopVideoCommand(self):
        vc = ValContainer()
        StopVideoCommand(CommandHook(stopVideo=vc.put)).execute()
        self.assertEqual(vc.get(), None)

    def testSnapshotCommand(self):
        vc = ValContainer()
        SnapshotCommand(CommandHook(snapshot=vc.put)).execute()
        self.assertEqual(vc.get(), None)

    def testPanoramicSnapshotCommand(self):
        vc = ValContainer()
        PanoramicSnapshotCommand(CommandHook(panoramicSnapshot=vc.put)).execute()
        self.assertEqual(vc.get(), None)

    def testMultipleCalls(self):
        c = Counter()
        for x in range(0, 100):
            ReverseCommand(0x33, CommandHook(reverse=c.incr()), 0).execute()
        self.assertEqual(c.get(), 100)

    def testFreeFuncNoParams(self):
        global freeFuncFired
        ReverseCommand(0x33, CommandHook(reverse=freefunc), 1).execute()
        self.assertEqual(freeFuncFired, True)

    def testFreeFuncParams(self):
        global freeFuncParamsFired
        ReverseCommand(0x33, CommandHook(reverse=freefuncParams), 123).execute()
        self.assertEqual(freeFuncParamsFired, True)
