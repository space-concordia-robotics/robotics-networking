import roboticsrov
from roboticsrov.stream.video_stream import VideoStream 
from roboticsrov.umanager import UManager


class Commands:
    def __init__(self):
        self.umanager = self.webcam_stream = None
        try:
            self.uManager = UManager()
        except Exception as e:
            print e.message
        
        try:
            self.webcam_stream = VideoStream('/dev/video0',8081)
        except Exception as e:
            print e.message

    def execute(bytes):
        cmd = ord(bytes[0])
        
        
        if cmd == ROBOTICSNET_DRIVE_FORWARD:
            self.umanager.forward({'value':ord(bytes[1], 'timediff':ord(bytes[2])})
            
        elif cmd == ROBOTICSNET_DRIVE_REVERSE:
            self.umanager.reverse({'value':ord(bytes[1], 'timediff':ord(bytes[2])})
        
        elif cmd == ROBOTICSNET_DRIVE_FORWARDLEFT:
            self.umanager.forwardleft({'value':ord(bytes[1], 'timediff':ord(bytes[2])})
        
        elif cmd == ROBOTICSNET_DRIVE_FORWARDRIGHT:
            self.umanager.forwardright({'value':ord(bytes[1], 'timediff':ord(bytes[2])})
        
        elif cmd == ROBOTICSNET_DRIVE_REVERSELEFT:
            self.umanager.reverseleft({'value':ord(bytes[1], 'timediff':ord(bytes[2])})
        
        elif cmd == ROBOTICSNET_DRIVE_REVERSERIGHT:
            self.umanager.reverseright({'value':ord(bytes[1], 'timediff':ord(bytes[2])})
        
        elif cmd == ROBOTICSNET_DRIVE_STOP:
            self.umanager.stop()
        
        elif cmd == ROBOTICSNET_CAMERA_START_VID:
            self.webcam_stream.start()
        
        elif cmd == ROBOTICSNET_CAMERA_START_VID:
            self.webcam_stream.end()
        
        elif cmd == ROBOTICSNET_CAMERA_SNAPSHOT:
            pass
        
        elif cmd == ROBOTICSNET_CAMERA_PANORAMICSNAPSHOT:
            pass
        
        
            
            
            
                    
