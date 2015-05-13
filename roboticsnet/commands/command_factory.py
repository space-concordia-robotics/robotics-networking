from roboticsnet.commands.command_validator import validate

class CommandFactory:
    """
    author: psyomn

    Consumes strings or byte arrays sent to service, and returns a command
    specific to that request
    """

    @staticmethod
    def make_from_str(str):
        """ Pass the string that is received from the listener here, and the
        appropriate command will be created and returned"""

        if not validate(str):
            print "Received erroneous command: {", str, "}"
            return

        str_arr = str.split()

    @staticmethod
    def make_from_byte_array(bytes):
        pass

