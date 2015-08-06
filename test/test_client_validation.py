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

    def testForwardLeft(self):
        self.cm.forwardLeft(12)

    def testForwardRight(self):
        self.cm.forwardRight(12)

    def testReverseLeft(self):
        self.cm.reverseLeft(12)

    def testReverseRight(self):
        self.cm.reverseRight(12)

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

    def testForwardRightBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.forwardRight(300)

    def testForwardRightBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.forwardRight(-300)

    def testForwardRightZero(self):
        self.cm.forwardRight(0)

    def testForwardLeftZero(self):
        self.cm.forwardLeft(0)

    def testForwardLeftBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.forwardLeft(300)

    def testForwardLeftBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.forwardLeft(-300)

    def testReverseRightBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.reverseRight(300)

    def testReverseRightBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.reverseRight(-300)

    def testReverseRightZero(self):
        self.cm.reverseRight(0)

    def testReverseLeftZero(self):
        self.cm.reverseLeft(0)

    def testReverseLeftBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.reverseLeft(300)

    def testReverseLeftBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.reverseLeft(-300)

    def testReverseBadValueBig(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.reverse(300)

    def testReverseBadValueSmall(self):
        with self.assertRaises(RoboticsnetException):
            self.cm.reverse(-300)

    def testReverseZero(self):
        self.cm.reverse(0)

