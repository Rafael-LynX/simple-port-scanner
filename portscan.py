# PORTSCANNER

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
import os

# Colors
GREEN = "\033[92m"
RED = "\033[91m"


def scan_port(ip: str, port: int):
    """
    Ele faz a conexão com alvo logo após receber a porta de execute_scan.
    realizando o processo de handshake de conexão e devolvendo as portas abertas e fechadas
    se o alvo retornar SYN-ACK vai nos retornar True, porta aberta
    se o alvo retornar RST vai nos retornar False, porta fechada
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            s.connect((ip, port))
            # Se passou do connect, a porta está aberta
            # Agora tentamos pegar o banner com timeout menor
            try:
                s.settimeout(0.5)
                banner = s.recv(1024).decode(errors="replace").strip()
                return banner if banner else True
            except (socket.timeout, OSError):
                return True
    except (socket.timeout, OSError):
        # timeout no recv, mas a porta continua aberta
        return False


def execute_scan(ip: str, ports: range):
    """
    ELe é o motor do código que utiliza as threads para fazer um trabalho mais rápido de scan
    os valores são atribúidos ao executor, que realiza 100 scan por vez e armazena o resultado
    na lista tasks.
    """
    print("Starting port scan")
    try:
        with ThreadPoolExecutor(max_workers=100) as executor:
            try:
                tasks = []
                for port in ports:
                    task = executor.submit(scan_port, ip, port)
                    tasks.append((port, task))

                for port, task in tasks:
                    open_port = task.result()
                    if open_port:
                        print(f"{GREEN}[+] Port {port} is open: {open_port}")
            except KeyboardInterrupt:
                print("\n[!] Program Terminated by user.")
                executor.shutdown(wait=False, cancel_futures=True)
                os._exit(1)
    finally:
        print("Exiting program")


# Parâmetros de ajuda e o que precisa para executar o programa.
def help_and_parameters():
    """
    O garçom do código, trata exclusivamente da interface de linha de comandos, adicionando parâmetros
    """
    parser = argparse.ArgumentParser(
        description="Port Scanner in python, created for Rafael-LynX"
    )
    parser.add_argument("-p", "--port", dest="port", type=int, help="specify a port")
    parser.add_argument(
        "-p-", "--ports", dest="all_ports", action="store_true", help="all ports"
    )
    parser.add_argument("target", help="IP address ou domain")
    return parser.parse_args()


def output_decoration(target, port):
    """
    Gera um cabeçalho visual para o utilizador
    """
    line = "-" * 35
    print(line)
    print(f"Target: {target}")
    print(f"Port: {port}")
    print(line)


def main(args):
    """
    O gerente do código, coordena as variáveis recebidas da interface com a excecução do motor
    """
    print("Executing main...")
    ip = args.target
    if args.port:
        print("Scan the specify port")
        ports = range(args.port, args.port + 1)
        # output_decoration(ip, port)
        # execute_scan(args.target, port)
    elif args.all_ports:
        print("Scan the all ports")
        ports = range(1, 65536)
        # output_decoration(ip, ports)
        # execute_scan(ip, ports)
    else:
        print("Scan the 1024 ports")
        ports = range(1, 1025)
        # output_decoration(ip, defaut_ports)
        # execute_scan(ip, defaut_ports)
    output_decoration(ip, ports)
    execute_scan(ip, ports)
    print("\nScan finished. Exiting Program")


# Ponto de entrada padrão do python (garante que só roda se chamado pelo terminal)
if __name__ == "__main__":
    args = help_and_parameters()
    main(args)
