# PORTSCANNER

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

# Colors
GREEN = "\033[92m"
RED = "\033[91m"

# ip = "50.116.1.184"


# Ele faz a conexão com alvo logo após receber a porta de execute_scan.
# realizando o processo de handshake de conexão e devolvendo as portas abertas e fechadas
# se o alvo retornar SYN-ACK vai nos retornar True, porta aberta
# se o alvo retornar RST vai nos retornar False, porta fechada
def scan_port(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            s.connect((ip, port))
            return True
    except (socket.timeout, OSError):
        return False


# ELe é o motor do código que utiliza as threads para fazer um trabalho mais rápido de scan
# os valores são atribúidos ao executor, que realiza 100 scan por vez e armazena o resultado
# na lista tasks.
def execute_scan(ip: str, ports: range):
    print("Starting port scan")
    try:
        with ThreadPoolExecutor(max_workers=100) as executor:
            tasks = []
            for port in ports:
                task = executor.submit(scan_port, ip, port)
                tasks.append((port, task))

            for port, task in tasks:
                open_port = task.result()
                if open_port:
                    print(f"{GREEN}[+] Port {port} is open")
                    # else:
                    # print(f"{RED}[!] Port {port} is closed")
    except KeyboardInterrupt:
        print("\nProgram Terminated by user.")
    finally:
        print("Exiting program")


# Parâmetros de ajuda e o que precisa para executar o programa.
def help_and_parameters():
    parser = argparse.ArgumentParser(
        description="Port Scanner in python, created for Rafael-LynX"
    )
    parser.add_argument("-p", "--port", dest="port", type=int, help="specify a port")
    parser.add_argument(
        "-p-", "--ports", dest="all_ports", action="store_true", help="all ports"
    )
    parser.add_argument("target", help="IP address ou domain")
    args = parser.parse_args()

    ip = args.target

    if args.port:
        port = range(args.port, args.port + 1)
        output_decoration(ip, port)
        execute_scan(args.target, port)
    elif args.all_ports:
        print("Scan the all ports")
        ports = range(1, 65536)
        output_decoration(ip, ports)
        execute_scan(ip, ports)
    else:
        print("Scan the 1024 ports")
        default_ports = range(1, 1025)
        output_decoration(ip, default_ports)
        execute_scan(ip, default_ports)


def output_decoration(target, port):
    line = "-" * 35
    print(line)
    print(f"Target: {target}")
    print(f"Port: {port}")
    print(line)


def main():
    print("Executing main...")
    help_and_parameters()


if __name__ == "__main__":
    main()
