# PORTSCANNER

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

# Colors
GREEN = "\033[92m"
RED = "\033[91m"

ip = "50.116.1.184"


def scan_port(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2.0)
            s.connect((ip, port))
            return True
    except (socket.timeout, OSError):
        return False


def execute_scan(ip: str, ports: range):
    print("Starting port scan")
    with ThreadPoolExecutor(max_workers=100) as executor:
        tasks = []
        for port in ports:
            task = executor.submit(scan_port, ip, port)
            tasks.append((port, task))

        for port, task in tasks:
            open_port = task.result()
            if open_port:
                print(f"{GREEN}[+] Port {port} is open")
            else:
                print(f"{RED}[!] Port {port} is closed")


def parameters():
    parser = argparse.ArgumentParser(
        description="Port Scanner in python, created for Rafael-LynX"
    )
    parser.add_argument("-p", "--port", dest="port", type=int, help="specify a port")
    parser.add_argument(
        "-p-", "--ports", dest="all_ports", action="store_true", help="all ports"
    )
    parser.add_argument("target", help="IP address ou domain")
    args = parser.parse_args()

    if args.port:
        print("Scan the specify port...")
        unique_port = int(args.port)
        port = range(unique_port, unique_port + 1)
        execute_scan(args.target, port)
    elif args.all_ports:
        print("Scan the all ports")
        ports = range(1, 65536)
        execute_scan(ip, ports)
    else:
        print("Scan the 1024 ports")
        default_ports = range(1, 1025)
        execute_scan(ip, default_ports)


parameters()
