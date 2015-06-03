class CommandHook:
    """
    If the user wants to add special hooks to the commands when they run. This
    is useful if we want to make this library reusable, without modifying the
    actual commands inside said library. The user of the library would simply
    pass a reference to the piece of code the said user wants to execute.

    Author: psyomn
    """

    def __init__(self, move=None, turn=None, queryproc=None, reverse=None):
        self.move = move
        self.turn = turn
        self.queryproc = queryproc
        self.reverse = reverse

