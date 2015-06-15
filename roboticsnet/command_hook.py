class CommandHook:
    """
    If the user wants to add special hooks to the commands when they run. This
    is useful if we want to make this library reusable, without modifying the
    actual commands inside said library. The user of the library would simply
    pass a reference to the piece of code the said user wants to execute.

    Author: psyomn
    """

    def __init__(self, forward=None, turn=None, queryproc=None, reverse=None,
            startVideo=None, stopVideo=None):
        self.forward = forward
        self.turn = turn
        self.queryproc = queryproc
        self.reverse = reverse
        self.startVideo = startVideo
        self.stopVideo = stopVideo

    def forwardHook(self):
        if self.forward:
            self.forward()

    def turnHook(self):
        if self.turn:
            self.turn()

    def queryprocHook(self):
        if self.queryproc:
            self.queryproc()

    def reverseHook(self):
        if self.reverse:
            self.reverse()

    def startVideoHook(self):
        if self.startVideo:
            self.startVideo();

    def stopVideoHook(self):
        if self.stopVideo:
            self.stopVideo();
