from sensors.base import Sensor
import serial


class GPS(Sensor):

    def __init__(self, serial_port, rate):
        self._ser = serial.Serial(serial_port, rate)
        """TODO: Add 5Hz update rate, add gps lat lng parser"""
        return

    def wait_for_satellite(self):
        print('Waiting for satellite lock')

    def poll_measure(self):
        data = self._ser.read(32)
        self._measure_lock.acquire()
        self._values = (data)
        self._measure_lock.release()
        print(f"Gps raw measure: {data}")

    def read_values(self):
        self._measure_lock.acquire()
        ret = self._values.copy()
        self._measure_lock.release()
        return ret

    def dispose(self):
        self._ser.close()

    def get_delay_between_measurements(self):
        return 200
