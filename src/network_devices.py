from src.device import Device


class Switch(Device):
    """Network switch"""
    def __init__(
        self,
        serial_number=None,
        vendor="cisco",
        mgmt_ip=None,
        no_of_ports=24,
        layer3_support=False,
        *args,
        **kwargs
    ):
        super().__init__(serial_number, vendor, mgmt_ip)
        self._no_of_ports = no_of_ports
        self._layer3_support = layer3_support

    @property
    def no_of_ports(self):
        return self._no_of_ports

    @no_of_ports.setter
    def no_of_ports(self, no_of_ports):
        self._no_of_ports = no_of_ports

    @property
    def layer3_support(self):
        return self._layer3_support

    @layer3_support.setter
    def layer3_support(self, is_layer3):
        self.layer3_support = is_layer3

    def __str__(self):
        return self.vendor.upper() + " Switch, Mgmt IP: " + self.mgmt_ip


class Router(Device):
    """Network Router"""
    def __init_(self, serial_number="", vendor="cisco", mgmt_ip="", os="ios", ios_version=None, *args, **kwargs):
        super().__init__(serial_number, vendor, mgmt_ip)
        self.os = os
        self.ios_version = ios_version

    def __str__(self):
        return self.vendor.upper() + " Router, Mgmt IP: " + self.mgmt_ip


# Firewalls are still under active consideration, not decided what should go into firewalls class
# Following code is just a starter.
class ASAFirewall(Device):
    def __init__(
        self,
        serial_number="",
        vendor="cisco",
        mgmt_ip="",
        modules=1,
        os="ios",
        mode="routed",
    ):
        super().__init__(serial_number, vendor, mgmt_ip)
        self._mode = mode

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new_mode):
        self._mode = new_mode

    def __str__(self):
        return self.vendor.upper() + " Firewall, Mgmt IP: " + self.mgmt_ip
