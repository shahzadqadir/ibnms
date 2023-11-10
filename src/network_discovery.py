from easysnmp import Session
from easysnmp import exceptions as easysnmp_exceptions

from connectivity import Connectivity


class EasySNMPDiscovery:
    def __init__(self, ip_address, snmp_community):
        if not Connectivity.check_connectivity(ip_address):
            raise ConnectionError(f"{ip_address} not reachable!")
        self.session = Session(
            hostname=ip_address, community=snmp_community, version=2
        )

    def get_hostname(self):
        try:
            return self.session.get("iso.3.6.1.2.1.1.5.0").value
        except easysnmp_exceptions.EasySNMPTimeoutError:
            raise RuntimeError("snmp community invalid or not configured correctly (get-hostname)")

    def get_version(self):
        try:
            version = self.session.get("iso.3.6.1.2.1.1.1.0").value
            for word in version.split(","):
                if "version" in word.lower():
                    return word.split()[1]
        except easysnmp_exceptions.EasySNMPTimeoutError:
            raise RuntimeError("SNMP community invalid or not configured correctly (get-version)")

        return None

    def get_serial_no(self):
        try:
            return self.session.get("iso.3.6.1.2.1.47.1.1.1.1.11.1").value
        except easysnmp_exceptions.EasySNMPTimeoutError:
            raise RuntimeError("SNMP Community invalid or not configured correctly (get-serial-number)")

    def get_vendor(self):
        try:
            vendor = self.session.get("iso.3.6.1.2.1.1.1.0").value
            if "cisco" in vendor.lower():
                return "cisco"
            elif "juniper" in vendor.lower():
                return "juniper"
        except easysnmp_exceptions.EasySNMPTimeoutError:
            raise RuntimeError("SNMP community either not configured or is incorrect (get-vendor)")

    # def __str__(self):
    #     return (
    #         f"hostname: {self.get_hostname()}, vendor: {self.get_vendor()}, "
    #         f"serial: {self.get_serial_no()}, {self.get_version()} "
    #     )


if __name__ == "__main__":
    device = EasySNMPDiscovery("192.168.0.2", "shahzad")
    print(device)
