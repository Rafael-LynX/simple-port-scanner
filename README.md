# simple-port-scanner

<img src="assets/port-scanner.png" alt="" style="display: block; margin: 20px auto; max-width: 80%; height: auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">

## Overview

A varredura de portas é o processo de sondar um host alvo para determinar quais portas TCP ou UDP estão aceitando conexões. Cada porta contém um número desde (1-65535) e elas podem ter um serviço em execução, como apache, ssh, etc. Portas de (1-1024) são portas padrões de serviços e que normalmente podem revelar alguma coisa.

### How to function?

A varredura de portas TCP explora o mecanismo de handshake de 3 vias, ele funciona assim, o nosso script envia a requisição `SYN` como uma tentativa de conexão ao alvo, se ele aceitar ele devolve `SYN-ACK` falando que porta está aberta e o serviço está ouvindo, então devolvemos `RST` para abortar o scanner e não completar o handshake, por que não queremos a conexão e sim informações. Nesse processo conseguimos as informações.

Agora quando enviamos `SYN` e ele devolve `RST` podemos dizer que a porta está fechada.

Ou quando enviamos `SYN` e ele não devolve nada, fica completamente em silêncio, quer dizer que ele bateu no firewall e o pacote dropou o pacote fazendo o script ficar esperando alguma resposta. Isso é uma das estratégias de defesa mais comuns.

## Key Features

- `scan_port()`:
- `execute_scan`:
- `help_and_parameters`:

## Installation & Setup

### 1. Clone the repository and navigate to the directory

```bash
git clone https://github.com/Rafael-LynX/simple-port-scanner.git
cd simple-port-scanner
```

### 2. Run the script

```bash
python3 portscan.py <port> <target>
```

## Screenshots

Em breve

## Built with

[![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Project Structure

```text
├── assets/
├── docs/
├── venv/
├── LICENSE
├── README.md
└── portscan.py
```

## Copyright & License

### MIT License

Copyright (c) 2026 **simple-port-scanner Author**. All Rights Reserved. [MIT licensed](./LICENSE)

## Author

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/109623407?s=400&u=19dac11507a1cbd81c5c6ceb1526c24eb6033cce&v=4" width=115><br><sub>Rafael Vieira</sub>](https://github.com/Rafael-LynX)
