#!/usr/bin/env python2.7

"""
Simple example demonstrating services being runned in order to poll different
aspects of a system. These are intended

Author: psyomn
"""

import roboticsnet
from roboticsnet.command_hook import CommandHook
from roboticsnet.rover_listener import RoverListener

forward_count = 0

def _forwardHook():
    global forward_count
    print "This is my custom forward hook!"
    forward_count += 1

def polling_service():
    """ Returns the same number all the time; for testing purposes """
    return 42

# First you would need to define your hooks using CommandHook
cmd_hook = CommandHook(
        forward=_forwardHook
        )

l = RoverListener(hooks=cmd_hook, monitorProcs=[polling_service])

print roboticsnet.__appname__, " ",  roboticsnet.__version__
print "Starting command dispatcher..."
l.listen()

print "The server is completely oblivious to the following information:"
print "  - forward commands received: ", forward_count


