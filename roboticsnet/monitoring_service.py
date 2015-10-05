import time
import threading
from threading import Thread

class MonitoringService(Thread):
    """
    This is some service that runs in the background, and records some value.
    This value can be later retrieved.

    Due to the abstract nature of this module,
    author: psyomn
    """

    def __init__(self, container, monitoringCall):
        """
        container:
            The container is the value we're going to be setting in the
            monitoring call, and returning whenever we're requesting sensor
            info.

        monitoringCall:
            A code block we pass, which monitors some aspect of the running
            system.
        """
        super(MonitoringService, self).__init__()
        self._stop = threading.Event()
        self.container = container
        self.monitoringCall = monitoringCall
        self.sleeptime = 1 # one second sleep

    def run(self):
        """ The service should be running here """
        while not self.stopped():
            self._poll()
            time.sleep(self.sleeptime)

    def _poll(self):
        self.container = self.monitoringCall()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def getValue(self):
        self.container
