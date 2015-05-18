class RoverUtils:

    @staticmethod
    def hexArr2Str(hexArr):
        str = ""
        for el in hexArr:
            str += chr(el)
        return str

