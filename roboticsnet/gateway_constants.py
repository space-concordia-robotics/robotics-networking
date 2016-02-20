"""
Store the constants for the whole project here. Other parts of the project can
use these constants to interface to appropriate modules if necessary.

Author:
    psyomn
"""

# The listener listens to this port if we specify nothing else
ROBOTICSNET_TCP_PORT =          10666
ROBOTICSNET_UDP_PORT =          10667

# Drive Commands (Range: 0x00 - 0x1F)
DRIVE_STOP =                    0x00
DRIVE_FORWARD =                 0x01
DRIVE_REVERSE =                 0x02
DRIVE_FORWARDLEFT =             0x03
DRIVE_FORWARDRIGHT =            0x04
DRIVE_REVERSELEFT =             0x05
DRIVE_REVERSERIGHT =            0x06

# Camera Commands (Range: 0x20 - 0x2F)
CAMERA_STARTVID =               0x20
CAMERA_STOPVID =                0x21
CAMERA_SNAPSHOT =               0x22
CAMERA_PANORAMICSNAPSHOT =      0x23

# Sensor Commands (Range: 0x30 - 0x5F)
SENSOR_INFO =                   0x30
SENSOR_INFORESP =               0x31

# Arm Commands (Range: 0x60 - 0x7F)
#ARM_STOP =                     0X60
#ARM_DRILL                      0X6D
#ARM_GRAB =                     0X7E
#ARM_RESET =                    0x7F

# Client Commands (Range: 0xE0 - 0xEF)
CLIENT_KILLCLIENT =             0xE0
#CLIENT_SETPORT =               0xE1
#CLIENT_SETHOST =               0xE2
#CLIENT_GETPORT =               0xE3
#CLIENT_GETHOST =               0xE4

# System Commands (Range: 0xF0 - 0xFF)
SYSTEM_QUERYPROC =              0xF0
SYSTEM_PING =                   0xF1
SYSTEM_GRACEFUL =               0xFF


ROBOTICSNET_STRCMD_LOOKUP = {
          'stop':                       DRIVE_STOP
        , 'forward':                    DRIVE_FORWARD
        , 'reverse':                    DRIVE_REVERSE
        , 'forwardLeft':                DRIVE_FORWARDLEFT
        , 'forwardRight':               DRIVE_FORWARDRIGHT
        , 'reverseLeft':                DRIVE_REVERSELEFT
        , 'reverseRight':               DRIVE_REVERSERIGHT

        , 'startvid':                   CAMERA_STARTVID
        , 'stopvid':                    CAMERA_STOPVID
        , 'snapshot':                   CAMERA_SNAPSHOT
        , 'panoramicsnapshot':          CAMERA_PANORAMICSNAPSHOT

        , 'sensorinfo':                 SENSOR_INFO
        , 'sensorinforesp':             SENSOR_INFORESP

#        , 'armstop':                    ARM_STOP
#        , 'armdrill':                   ARM_DRILL
#        , 'armgrab':                    ARM_GRAB
#        , 'armreset':                   ARM_RESET

        , 'killclient':                 CLIENT_KILL

#        , 'setport':                    CLIENT_SETPORT
#        , 'sethost':                    CLIENT_SETHOST
#        , 'getport':                    CLIENT_GETPORT
#        , 'gethost':                    CLIENT_GETHOST

        , 'queryproc':                  SYSTEM_QUERYPROC
        , 'ping':                       SYSTEM_PING
        , 'graceful':                   SYSTEM_GRACEFUL
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
