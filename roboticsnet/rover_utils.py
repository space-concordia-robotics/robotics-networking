class RoverUtils:

    @staticmethod
    def hexArr2Str(hexArr):
        """
        NB: join MUST have no spaces in between. This makes a hex array
        into a string (so you should not pass values per element which exceed
        255, or 0xFF
        """
        return ''.join(map(lambda x: chr(x), hexArr))

    @staticmethod
    def hexArrToString(hexArr):
        """
        Parameters:
            hexArr - is an array that is known to contain byte data.

        Return:
            a string representing the bytes, in human readable form (this is
            used when you want to print the information)
        """
        return ' '.join(map(lambda x: hex(ord(x)), bytes))

