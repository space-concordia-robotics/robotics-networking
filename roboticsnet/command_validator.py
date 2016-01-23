
from roboticsnet.rover_utils import RoverUtils

"""
author: psyomn
This will take in the string that is sent to the networking gateway, and
check if it's in understandable format. Any checks should be done in this
file for now
"""

def validate(cmd_str):
    return _valid_arg_size(cmd_str) and _command_exists(cmd_str)

def _valid_arg_size(args):
    # TODO this might need fixing/removing
    """ Is the command 2 or more? """
    return len(args.split()) >= 2

def _command_exists(args):
    """ Is this a command that exists? """
    cmds = ['forward', 'reverse', 'forwardLeft', 'forwardRight','reverseLeft','reverseRight', 'stop']
    cmd = args.split()[0]
    return cmd in cmds


def calculate_time_diff(string):
    """ Gets time diff on timestamped command. """
    diff = (RoverUtils.timeModulusToHex() - string)
    return diff
