class Device:
    """Represents a network device"""

    def __init__(self, serial_number=None, vendor=None, mgmt_ip=""):
        self._serial_number = serial_number
        self._vendor = vendor
        self._mgmt_ip = mgmt_ip

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial):
        self._serial_number = serial

    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        self._vendor = vendor

    @property
    def mgmt_ip(self):
        return self._mgmt_ip

    @mgmt_ip.setter
    def mgmt_ip(self, mgmt_ip):
        self._mgmt_ip = mgmt_ip

    def __str__(self):
        device_str = (
            "{ " + self.vendor + ", " + self.serial_number + ", " + self.mgmt_ip + " }"
        )
        return device_str

    def __eq__(self, other):
        return self.serial_number == other.serial_number
