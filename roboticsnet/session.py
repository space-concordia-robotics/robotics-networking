class Session:
    """
    Store anything that needs to be known about the current running session here

    author: psyomn
    """

    def __init__(self):
        self.data = {}

    def put(self, key, data):
        self.data[key] = data

    def get(self, key):
        return self.data[key]

