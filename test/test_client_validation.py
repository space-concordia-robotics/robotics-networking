import unittest

from roboticsnet.client.rover_client import RoverClient

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

    def testTurn(self):
        self.cm.turn(12)

    def testQuery(self):
        self.cm.query()

    def testReverse(self):
        self.cm.reverse(123)

    def testStartVideo(self):
        self.cm.startVideo()

    def testStopVideo(self):
        self.cm.stopVideo()
