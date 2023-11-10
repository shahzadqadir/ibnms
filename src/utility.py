from network_devices import IOSRouter, IOSSwitch, ASAFirewall
from src.connectivity import Connectivity


def load_devices_from_text_file(filename):
    """Loads Network devices from source file"""
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
                devices.append(IOSRouter(serial_number, vendor, mgmt_ip))
            elif "switch" in row[0]:
                devices.append(
                    IOSSwitch(
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


def parse_cisco_router_inventory(hostname, username, password, enable_secret=None):
    connection = Connectivity(hostname, username, password, enable_secret)
    inventory = connection.send_show_command_cisco("show inventory")[0]
    return {"serial_number": inventory["sn"], "pid": inventory["pid"]}


inventory = parse_cisco_router_inventory("192.168.0.1", "cisco", "cisco123")
print(inventory)
