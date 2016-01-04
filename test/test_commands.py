import unittest

from roboticsnet.commands import Commands

class TestCommands(unittest.TestCase):
    """ These just make sure that the commands, once executed, don't raise exceptions
        TODO: testhooks - hooks should also have parameters being passed - need
        to fix this
    """

    self.commands = Commands()

    def testForwardCommand(self):
        self.commands.execute([ROBOTICSNET_DRIVE_FORWARD,10,5])

    def testReverseCommand(self):
        self.commands.execute([ROBOTICSNET_DRIVE_REVERSE,10,5])

    def testForwardLeftCommand(self):
        self.commands.execute([ROBOTICSNET_DRIVE_FORWARDLEFT,10,5])

    def testForwardRightCommand(self):
        self.commands.execute([ROBOTICSNET_DRIVE_FORWARDRIGHT,10,5])

    def testReverseLeftCommand(self):
        self.commands.execute([ROBOTICSNET_DRIVE_REVERSELEFT,10,5])

    def testReverseRightCommand(self):
        self.commands.execute([ROBOTICSNET_DRIVE_REVERSERIGHT,10,5])

    def testStartVideoCommand(self):
        self.commands.execute([ROBOTICSNET_CAMERA_START_VID])

    def testStopVideoCommand(self):
        self.commands.execute([ROBOTICSNET_CAMERA_STOP_VID])

    def testSnapshotCommand(self):
        self.commands.execute([ROBOTICSNET_CAMERA_SNAPSHOT])

    def testPanoramicSnapshotCommand(self):
        self.commands.execute([ROBOTICSNET_CAMERA_PANORAMICSNAPSHOT])
