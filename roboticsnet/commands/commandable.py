class Commandable:
    """ Interface for anything that may be executed """

    def execute(self):
        raise NotImplementedError("You need to implement this functionality")
