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
  - forward commands received:  1
  - turn commands received:  44
  - query commands received:  31
  - reverse commands received:  18

Author: psyomn
"""

import roboticsnet
from roboticsnet.command_hook import CommandHook
from roboticsnet.rover_listener import RoverListener

forward_count = 0

def _forwardHook(params):
    print "This is my custom forward hook!"
    print "And in my custom forward hook, the params I receive are: ", params
    print "And I extract the value of interest: ", params['value']


# First you would need to define your hooks using CommandHook
cmd_hook = CommandHook(
        forward=_forwardHook,
        )

l = RoverListener(hooks=cmd_hook)

print roboticsnet.__appname__, " ",  roboticsnet.__version__
print "Starting command dispatcher..."
l.listen()

