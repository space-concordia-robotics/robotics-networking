import unittest

from roboticsnet.client.rover_client import RoverClient
from roboticsnet.roboticsnet_exception import RoboticsnetException

class ClientMock(RoverClient):
    """ Do nothing when actually sending things """

    def __init__(self, host, port):
        RoverClient.__init__(self, host, port)

    def _sendMessage(self, message):
        pass

    def _sendMessageAwaitReply(self, message):
        pass


class TestClientValidation(unittest.TestCase):
    """ This should test to see if the client freaks out if you give it silly
    values"""

    def setUp(self):
        self.cm = ClientMock('myhost', 123)

    def testGraceful(self):
        self.cm.graceful()

    def testAttrSet(self):
        self.assertEqual(self.cm.getHost(), 'myhost')
        self.assertEqual(self.cm.getPort(), 123)

    def testForward(self):
        self.cm.forward(12)

    def testTurnLeft(self):
        self.cm.turnLeft(12)

    def testTurnRight(self):
        self.cm.turnRight(12)

    def testQuery(self):
        self.cm.query()

    def testReverse(self):
        self.cm.reverse(123)

    def testStartVideo(self):
        self.cm.startVideo()

    def testStopVideo(self):
        self.cm.stopVideo()

    # BADVALS now

    def testForwardBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.forward(300)

    def testForwardBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.forward(-300)

    def testForwardZero(self):
        self.cm.forward(0)

    def testTurnRightBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.turnRight(300)

    def testTurnRightBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.turnLeft(-300)

    def testTurnRightZero(self):
        self.cm.turnRight(0)

    def testTurnLeftZero(self):
        self.cm.turnLeft(0)

    def testTurnLeftBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.turnLeft(300)

    def testTurnLeftBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.turnLeft(-300)

    def testReverseBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.reverse(300)

    def testReverseBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.reverse(-300)

    def testReverseZero(self):
        self.cm.reverse(0)

