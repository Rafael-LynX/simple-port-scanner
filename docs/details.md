# Details

0-65535 portas
1-1023 portas conhecidas

Porta aberta: algo está escutando, está seria a superfície de ataque.
Porta fechada: host está ativo e acessível, mas nada está escutando nessa porta.
Filtrada: um firewall ou filtro de pacotes fica entre você e o alvo. Pode impedir o scan, mas pode revelar vulnerabilidades de configuração.

Funções:

- 1 detecção de porta aberta
- 2 detecção de porta fechada
- 3 detecção de porta Filtrada
- 4 ler os banners, dados iniciais, revelar services versions

Erros:

- 1 confundir fechado com filtrado
- 2 não tratar os falsos positivos

alvo: <http://scanme.nmap.org/>
Non-authoritative answer:
Name: <http://scanme.nmap.org>
Address: 50.116.1.184
Name: <http://scanme.nmap.org>
Address: 2600:3c01:e000:3e6::6d4e:7061

preciso que ele faça o scan em todas as portas

se ele colocar -p- todas as portas sem limite
se ele colocar -p somente uma porta
se ele não colocar porta, o scan é feito em todas 1024 portas conhecidas
