
"""author: msnidal"""

from time import time
import glob
import sys
import serial

class RoverUtils:

    @staticmethod
    def hexArr2Str(hexArr):
        """
        NB: join MUST have no spaces in between. This makes a hex array
        into a string (so you should not pass values per element which exceed
        255, or 0xFF
        """
        return ''.join(map(lambda x: chr(x), hexArr))

    @staticmethod
    def hexArrToTimestampedString(hexArr):
        """
        Similar to hexArr2Str, but includes a byte-sized (he he he) timestamp
        used for diffs along with the message.
        """
        hexArr.append(RoverUtils.timeModulusToHex())
        return RoverUtils.hexArr2Str(hexArr)

    @staticmethod
    def hexArrToHumanReadableString(hexArr):
        """
        Parameters:
            hexArr - is an array that is known to contain byte data.
        Return:
            a string representing the bytes, in human readable form (this is
            used when you want to print the information)
        """
        return ' '.join(map(lambda x: hex(ord(x)), hexArr))

    @staticmethod
    def timeModulusToHex():
        """
        This gets the system time mod 256 as a hex, for attaching to messages
        sent over roboticsnet. I'm using a bitwise operator here since I suspect
        it might be a bit (he he he) faster.
        """
        return int(time()) & 255
    
    @staticmethod
    def findPorts():
        """Lists serial ports
                
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of available serial ports
        """
        if sys.platform.startswith('win'):
            ports = ['COM' + str(i + 1) for i in range(256)]

        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')

        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')

        else:
            raise EnvironmentError('Unsupported platform')

        result = [] 
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass

        return result
