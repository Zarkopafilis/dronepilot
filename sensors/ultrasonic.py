from sensors.base import Sensor


class Ultrasonic(Sensor):
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        """TODO: Initialize pins"""

    def poll_measure(self):
        """TODO: Send pulse and wait for response with timeout"""

        self.measure_lock.acquire()

        self.measure_lock.release()

    def read_values(self):
        self.measure_lock.acquire()
        ret = self.values.copy()
        self.measure_lock.release()
        return ret
