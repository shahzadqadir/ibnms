from src.connectivity import Connectivity


def main():
    connection = Connectivity("192.168.0.1", "cisco", "cisco123")
    print(connection.send_show_command_cisco("show inventory"))


if __name__ == "__main__":
    main()
