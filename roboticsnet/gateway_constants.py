"""
Store the constants for the whole project here. Other parts of the project can
use these constants to interface to appropriate modules if necessary.

Author:
    psyomn
"""

# The listener listens to this port if we specify nothing else
ROBOTICSNET_PORT = 5000
# The command bound to this hex for a graceful shutdown in the main server loop.
ROBOTICSNET_COMMAND_GRACEFUL  = 0xFF

ROBOTICSNET_COMMAND_MOVE      = 0x01
ROBOTICSNET_COMMAND_TURN      = 0x02
ROBOTICSNET_COMMAND_QUERYPROC = 0x03
ROBOTICSNET_COMMAND_REVERSE   = 0x04

ROBOTICSNET_STRCMD_LOOKUP = {
          'graceful': ROBOTICSNET_COMMAND_GRACEFUL
        , 'move': ROBOTICSNET_COMMAND_MOVE
        , 'turn': ROBOTICSNET_COMMAND_TURN
        , 'queryproc': ROBOTICSNET_COMMAND_QUERYPROC
        }


ROBOTICSNET_PROCESS_IDS_TO_LABEL = {
          0x00: "rovercore"
        , 0x01: "camera1"
        , 0x02: "camera2"
        , 0x03: "camera3"
        }

ROBOTICSNET_PROCESS_STATUS_IDS_TO_LABEL = {
          0x00: "dead"
        , 0x01: "running"
        , 0x02: "badstate"
        }
