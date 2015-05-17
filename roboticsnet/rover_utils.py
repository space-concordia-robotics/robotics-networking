
class RoverUtils:

    @staticmethod
    def makeStringFromHexArray(hexArr):
        str = ""
        for el in hexArr:
            str += chr(el)
        return str

