#!/usr/bin/env python2.7

"""
This is an example script, showing users of the library how you may attach
hooks to the commands that the rover may receive. This way you can 'inject'
behavior to the library without modifying it.

The difference to this approach is that you'll need to first create a CommandHook
object, where you assign all the hooks you are interested in, within.
The CommandHook object will then need to be passed to the RoverListener object, via
constructor injection. This should suffice to get things working :o).

The particular example this script demonstrates, is how we can spawn a server, and
add hooks which simply count how many times certain requests have been sent. When
The server gracefully shuts down, the vaulues are printed on screen. Below exists
sample output:

...

BYE.
The server is completely oblivious to the following information:
  - move commands received:  1
  - turn commands received:  44
  - query commands received:  31
  - reverse commands received:  18

Author: psyomn
"""

import roboticsnet
from roboticsnet.command_hook import CommandHook
from roboticsnet.rover_listener import RoverListener

move_count = 0
turn_count = 0
qp_count   = 0
rev_count  = 0
svid_count = 0

def _moveHook():
    global move_count
    print "This is my custom move hook!"
    move_count += 1

def _turnHook():
    global turn_count
    print "This is my turn hook!"
    turn_count += 1

def _queryProcHook():
    global qp_count
    print "This is my queryproc hook!"
    qp_count += 1

def _reverseHook():
    global rev_count
    print "This is my reverse hook!"
    rev_count += 1

def _startVideoCount():
    global svid_count
    print "This is the startvid hook!"
    svid_count += 1

# First you would need to define your hooks using CommandHook
cmd_hook = CommandHook(
        move=_moveHook,
        turn=_turnHook,
        queryproc=_queryProcHook,
        reverse=_reverseHook,
        startVideo=_startVideoCount
        )

l = RoverListener(hooks=cmd_hook)

print roboticsnet.__appname__, " ",  roboticsnet.__version__
print "Starting command dispatcher..."
l.listen()

print "The server is completely oblivious to the following information:"
print "  - move commands received: ", move_count
print "  - turn commands received: ", turn_count
print "  - query commands received: ", qp_count
print "  - reverse commands received: ", rev_count
print "  - startvid commands received: ", svid_count


