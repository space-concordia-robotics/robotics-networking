import unittest

from roboticsnet.gateway_constants import *
from roboticsnet.rover_client import RoverClient
from roboticsnet.roboticsnet_exception import RoboticsnetException

class ClientMock(RoverClient):
    """ Do nothing when actually sending things """

    def __init__(self, host, port):
        RoverClient.__init__(self, host, port)

    def _sendMessage(self, message, TCP=True):
        pass

    def _sendMessageAwaitReply(self, message):
        pass


class TestClientValidation(unittest.TestCase):
    """ This should test to see if the client freaks out if you give it silly
    values"""

    def setUp(self):
        self.cm = ClientMock('myhost', 123)

    def testGraceful(self):
        self.cm.sendCommand(ROBOTICSNET_SYSTEM_GRACEFUL)

    def testAttrSet(self):
        self.assertEqual(self.cm.getHost(), 'myhost')
        self.assertEqual(self.cm.getPort(), 123)

    def testForward(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARD,12)

    def testForwardLeft(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARDLEFT, 12)

    def testForwardRight(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARDRIGHT,12)

    def testReverseLeft(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSELEFT,12)

    def testReverseRight(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSERIGHT,12)

    def testQuery(self):
        self.cm.query()

    def testReverse(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSE,12)

    def testStartVideo(self):
        self.cm.sendCommand(ROBOTICSNET_CAMERA_START_VID)

    def testStopVideo(self):
        self.cm.sendCommand(ROBOTICSNET_CAMERA_STOP_VID)

    def testSnapshot(self):
        self.cm.sendCommand(ROBOTICSNET_CAMERA_SNAPSHOT)

    def testPanoramicSnapshot(self):
        self.cm.sendCommand(ROBOTICSNET_CAMERA_PANORAMICSNAPSHOT)

    def testPint(self):
        self.cm.ping()

    # BADVALS now

    def testForwardBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARD,300)

    def testForwardBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARD,-300)

    def testForwardZero(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARD,0)

    def testForwardRightBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARDRIGHT,300)

    def testForwardRightBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARDRIGHT,-300)

    def testForwardRightZero(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARDRIGHT,0)

    def testForwardLeftZero(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARDLEFT,0)

    def testForwardLeftBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARDLEFT,300)

    def testForwardLeftBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_FORWARDLEFT,-300)

    def testReverseRightBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSERIGHT,300)

    def testReverseRightBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSERIGHT,-300)

    def testReverseRightZero(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSERIGHT,0)

    def testReverseLeftZero(self):
        self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSELEFT,-0)

    def testReverseLeftBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSELEFT,300)

    def testReverseLeftBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSELEFT,-300)

    def testReverseBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSE,300)

    def testReverseBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSE,-300)

    def testReverseZero(self):
            self.cm.timedCommand(ROBOTICSNET_DRIVE_REVERSE,0)
