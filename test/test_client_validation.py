import unittest

from roboticsnet.gateway_constants import *
from roboticsnet.rover_client import RoverClient
from roboticsnet.roboticsnet_exception import RoboticsnetException

class ClientMock(RoverClient):
    """ Do nothing when actually sending things """

    def __init__(self):
        RoverClient.__init__(self)

    def _sendMessage(self, message):
        pass

    def _sendMessageAwaitReply(self, message):
        pass


class TestClientValidation(unittest.TestCase):
    """ This should test to see if the client freaks out if you give it silly
    values"""

    def setUp(self):
        self.cm = ClientMock()

    def testGraceful(self):
        self.cm.sendCommand(SYSTEM_GRACEFUL)


    def testForward(self):
        self.cm.timedCommand(DRIVE_FORWARD,12)

    def testLeft(self):
        self.cm.timedCommand(DRIVE_LEFT, 12)

    def testRight(self):
        self.cm.timedCommand(DRIVE_RIGHT,12)

    def testQuery(self):
        self.cm.query()

    def testReverse(self):
        self.cm.timedCommand(DRIVE_REVERSE,12)

    def testStartVideo(self):
        self.cm.sendCommand(CAMERA_START_VID)

    def testStopVideo(self):
        self.cm.sendCommand(CAMERA_STOP_VID)

    def testSnapshot(self):
        self.cm.sendCommand(CAMERA_SNAPSHOT)

    def testPanoramicSnapshot(self):
        self.cm.sendCommand(CAMERA_PANORAMIC)

    def testPing(self):
        self.cm.ping()

    # BADVALS now

    def testForwardBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(DRIVE_FORWARD,300)

    def testForwardBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(DRIVE_FORWARD,-300)

    def testForwardZero(self):
        self.cm.timedCommand(DRIVE_FORWARD,0)

    def testForwardRightBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(DRIVE_RIGHT,300)

    def testForwardRightBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(DRIVE_RIGHT,-300)

    def testForwardRightZero(self):
        self.cm.timedCommand(DRIVE_RIGHT,0)

    def testForwardLeftZero(self):
        self.cm.timedCommand(DRIVE_LEFT,0)

    def testForwardLeftBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(DRIVE_LEFT,300)

    def testForwardLeftBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(DRIVE_LEFT,-300)

    def testReverseBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(DRIVE_REVERSE,300)

    def testReverseBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(DRIVE_REVERSE,-300)

    def testReverseZero(self):
            self.cm.timedCommand(DRIVE_REVERSE,0)
