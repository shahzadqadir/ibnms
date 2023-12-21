from network_devices import Router, Switch, ASAFirewall
from device_discovery import EasySNMPDiscovery
from src.connectivity import Connectivity


def load_devices_from_text_file(filename):
    """Loads Network devices from source file
    expects file to be in the format of
    device_type(router/switch/firewall), serial_number, vendor, management_ip, modules/ports, ios
    returns a list of Devices (Router/Switch/Firewall)
    """
    devices = []
    with open(filename) as file:
        for line in file:
            row = line.split(",")
            serial_number = row[1]
            vendor = row[2]
            mgmt_ip = row[3]
            modules = row[4]
            os = row[5]
            if "router" in row[0]:
                devices.append(Router(serial_number, vendor, mgmt_ip))
            elif "switch" in row[0]:
                devices.append(
                    Switch(
                        serial_number,
                        vendor,
                        mgmt_ip,
                        no_of_ports=row[6],
                        layer3_support=row[7],
                    )
                )
            elif "firewall" in row[0]:
                devices.append(
                    ASAFirewall(
                        serial_number, vendor, mgmt_ip, modules, os, mode=row[6]
                    )
                )
    return devices


def load_device_with_snmp(ip_address, community):
    """
    Load device information using SNMP (currently only v2 is supported).

    Args:
        ip_address (String): A valid and reachable device IP address.
        community (String): SNMP community to use to connect to remote device.

    Returns:
        Device: returns a subclass of type Device. Can be a Router/Switch/Firewall

    Raises:
        ConnectionError: If device is not reachable via icmp
        EasySNMPTimeoutError: If device is reachable not respond to snmp
    """
    device = EasySNMPDiscovery(ip_address, community)
    print(device.get_serial_no())


if __name__ == "__main__":
    load_device_with_snmp("192.168.201.1", "cisco123")
    load_device_with_snmp("192.168.201.2", "cisco123")
