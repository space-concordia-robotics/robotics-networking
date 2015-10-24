class CommandHook:
    """
    If the user wants to add special hooks to the commands when they run. This
    is useful if we want to make this library reusable, without modifying the
    actual commands inside said library. The user of the library would simply
    pass a reference to the piece of code the said user wants to execute.

    Author: psyomn
    """

    def __init__(self, forward=None, reverse=None, forwardLeft=None,
            forwardRight=None, reverseLeft=None, reverseRight=None,
            stop=None, queryproc=None, startVideo=None, stopVideo=None,
            snapshot=None, panoramicSnapshot=None):
        self.forward = forward
        self.reverse = reverse
        self.forwardLeft = forwardLeft
        self.forwardRight = forwardRight
        self.reverseLeft = reverseLeft
        self.reverseRight = reverseRight
        self.stop = stop
        self.queryproc = queryproc
        self.startVideo = startVideo
        self.stopVideo = stopVideo
