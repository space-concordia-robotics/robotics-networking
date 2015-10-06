"""
Store the constants for the whole project here. Other parts of the project can
use these constants to interface to appropriate modules if necessary.

Author:
    psyomn
"""

# The listener listens to this port if we specify nothing else
ROBOTICSNET_PORT = 5000
# The command bound to this hex for a graceful shutdown in the main server loop.
ROBOTICSNET_COMMAND_GRACEFUL = 0xFF

ROBOTICSNET_COMMAND_FORWARD = 0x01
ROBOTICSNET_COMMAND_REVERSE = 0X02
ROBOTICSNET_COMMAND_FORWARDLEFT = 0X03
ROBOTICSNET_COMMAND_FORWARDRIGHT = 0X04
ROBOTICSNET_COMMAND_REVERSELEFT = 0X09
ROBOTICSNET_COMMAND_REVERSERIGHT = 0X10
ROBOTICSNET_COMMAND_STOP = 0x05

ROBOTICSNET_COMMAND_QUERYPROC = 0x06

ROBOTICSNET_COMMAND_START_VID = 0x07
ROBOTICSNET_COMMAND_STOP_VID = 0x08

ROBOTICSNET_COMMAND_SENSEINFO = 0x11
ROBOTICSNET_COMMAND_SENSEINFO_RESP = 0x12

ROBOTICSNET_STRCMD_LOOKUP = {
          'graceful': ROBOTICSNET_COMMAND_GRACEFUL

        , 'forward': ROBOTICSNET_COMMAND_FORWARD
        , 'reverse': ROBOTICSNET_COMMAND_REVERSE
        , 'forwardLeft': ROBOTICSNET_COMMAND_FORWARDLEFT
        , 'forwardRight': ROBOTICSNET_COMMAND_FORWARDRIGHT
        , 'reverseLeft': ROBOTICSNET_COMMAND_REVERSELEFT
        , 'reverseRight': ROBOTICSNET_COMMAND_REVERSERIGHT
        , 'stop': ROBOTICSNET_COMMAND_STOP

        , 'queryproc': ROBOTICSNET_COMMAND_QUERYPROC

        , 'startvid': ROBOTICSNET_COMMAND_START_VID
        , 'stopvid': ROBOTICSNET_COMMAND_STOP_VID
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
