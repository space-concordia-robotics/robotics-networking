from roboticsnet.commands.command_validator import CommandValidator

class CommandFactory:
    """
    author: psyomn

    Consumes strings sent to service, and returns a command specific to that
    request
    """

    def make_from_str(str):
        """ Pass the string that is received from the listener here, and the
        appropriate command will be created and returned"""

        if not CommandValidator.validate(str):
            print "Received erroneous command: {", str, "}"
            return

        str_arr = str.split()

