class RoverUtils:

    @staticmethod
    def hexArr2Str(hexArr):
        """
        NB: join MUST have no spaces in between. This makes a hex array
        into a string (so you should not pass values per element which exceed
        255, or 0xFF
        """
        return ''.join(map(lambda x: chr(x), hexArr))

