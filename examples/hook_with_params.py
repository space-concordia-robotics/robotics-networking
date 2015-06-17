#!/usr/bin/env python2.7

"""
Hooks, but which can get params so that they do something with them.

Right now, to get the particular values you can use:

    def myhook(params):
        val = params["value"]
        ...
as the hook sets 'params' to the hash:

    {"value":<some-value>}

with respect to whatever you receive.

Author: psyomn
"""

import roboticsnet
from roboticsnet.command_hook import CommandHook
from roboticsnet.rover_listener import RoverListener

forward_count = 0

class Counter:
    def __init__(self):
        self.count = 0

    def incr(self):
        self.count += 1

    def get(self):
        return self.count

def _forwardHook(params):
    print "This is my custom forward hook!"
    print "And in my custom forward hook, the params I receive are: ", params
    print "And I extract the value of interest: ", params['value']

def _turnHook():
    print "This is turn hook, where I don't care about the params (even though"
    print "we actually do receive params"

# If you try to pass this, then you're going to get an exception
# def _someOtherHook(a,b,c,d,e):
#     pass

myCounter = Counter()

# First you would need to define your hooks using CommandHook
cmd_hook = CommandHook(
        forward=_forwardHook,
        turn=_turnHook,
        # reverse=_someOtherHook,
        startVideo=myCounter.incr
        )

l = RoverListener(hooks=cmd_hook)

print roboticsnet.__appname__, " ",  roboticsnet.__version__
print "Starting command dispatcher..."
l.listen()

print "The startvideo command was received this many times: ", myCounter.get()

