"""
Store the constants for the whole project here. Other parts of the project can
use these constants to interface to appropriate modules if necessary.

Author:
    psyomn
"""

# The listener listens to this port if we specify nothing else
ROBOTICSNET_TCP_PORT = 10666
ROBOTICSNET_UDP_PORT = 10667

# Drive Commands (Range: 0x00 - 0x1F)
ROBOTICSNET_DRIVE_STOP =                0x00
ROBOTICSNET_DRIVE_FORWARD =             0x01
ROBOTICSNET_DRIVE_REVERSE =             0x02
ROBOTICSNET_DRIVE_FORWARDLEFT =         0x03
ROBOTICSNET_DRIVE_FORWARDRIGHT =        0x04
ROBOTICSNET_DRIVE_REVERSELEFT =         0x05
ROBOTICSNET_DRIVE_REVERSERIGHT =        0x06

# Camera Commands (Range: 0x20 - 0x2F)
ROBOTICSNET_CAMERA_START_VID =          0x20
ROBOTICSNET_CAMERA_STOP_VID =           0x21
ROBOTICSNET_CAMERA_SNAPSHOT =           0x22
ROBOTICSNET_CAMERA_PANORAMICSNAPSHOT =  0x23

# Sensor Commands (Range: 0x30 - 0x5F)
ROBOTICSNET_SENSOR_INFO =               0x30
ROBOTICSNET_SENSOR_INFO_RESP =          0x31

# Arm Commands (Range: 0x60 - 0x7F)
#ROBOTICSNET_ARM_STOP =                  0X60
#ROBOTICSNET_ARM_DRILL                   0X6D
#ROBOTICSNET_ARM_GRAB =                  0X7E
#ROBOTICSNET_ARM_RESET =                 0x7F

# Client Commands (Range: 0xE0 - 0xEF)
ROBOTICSNET_SYSTEM_SET_PORT =            0xE0
ROBOTICSNET_SYSTEM_SET_HOST =            0xE1
ROBOTICSNET_SYSTEM_GET_PORT =            0xE2
ROBOTICSNET_SYSTEM_GET_HOST =            0xE3
ROBOTICSNET_SYSTEM_KILL_CLIENT =         0xE4

# System Commands (Range: 0xF0 - 0xFF)
ROBOTICSNET_SYSTEM_QUERYPROC =          0xF0
ROBOTICSNET_SYSTEM_PING =               0xF1
ROBOTICSNET_SYSTEM_GRACEFUL =           0xFF


ROBOTICSNET_STRCMD_LOOKUP = {
          'stop':                       ROBOTICSNET_DRIVE_STOP
        , 'forward':                    ROBOTICSNET_DRIVE_FORWARD
        , 'reverse':                    ROBOTICSNET_DRIVE_REVERSE
        , 'forwardLeft':                ROBOTICSNET_DRIVE_FORWARDLEFT
        , 'forwardRight':               ROBOTICSNET_DRIVE_FORWARDRIGHT
        , 'reverseLeft':                ROBOTICSNET_DRIVE_REVERSELEFT
        , 'reverseRight':               ROBOTICSNET_DRIVE_REVERSERIGHT

        , 'startVid':                   ROBOTICSNET_CAMERA_START_VID
        , 'stopVid':                    ROBOTICSNET_CAMERA_STOP_VID
        , 'snapshot':                   ROBOTICSNET_CAMERA_SNAPSHOT
        , 'panoramicSnapshot':          ROBOTICSNET_CAMERA_PANORAMICSNAPSHOT

        , 'sensorInfo':                 ROBOTICSNET_SENSOR_INFO
        , 'sensorInfoResp':             ROBOTICSNET_SENSOR_INFO_RESP

#        , 'armstop':                    ROBOTICSNET_ARM_STOP
#        , 'armdrill':                   ROBOTICSNET_ARM_DRILL
#        , 'armgrab':                    ROBOTICSNET_ARM_GRAB
#        , 'armreset':                   ROBOTICSNET_ARM_RESET

        , 'setPort':                    ROBOTICSNET_SYSTEM_SET_PORT
        , 'setHost':                    ROBOTICSNET_SYSTEM_SET_HOST
        , 'getPort':                    ROBOTICSNET_SYSTEM_GET_PORT
        , 'getHost':                    ROBOTICSNET_SYSTEM_GET_HOST
        , 'killClient':                 ROBOTICSNET_SYSTEM_KILL_CLIENT

        , 'queryproc':                  ROBOTICSNET_SYSTEM_QUERYPROC
        , 'ping':                       ROBOTICSNET_SYSTEM_PING
        , 'graceful':                   ROBOTICSNET_SYSTEM_GRACEFUL
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
