# PORTSCANNER

import socket

ip = "50.116.1.184"


def scan_port(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2.0)
            s.connect((ip, port))
            return True
    except (socket.timeout, OSError):
        return False


def default_scan_port_1024(ip: str):
    for port in range(1, 1025):
        if scan_port(ip, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")


default_scan_port_1024(ip)
