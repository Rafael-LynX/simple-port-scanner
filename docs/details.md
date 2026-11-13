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

DRY - don't reapeat yourself

A leitura do python acontece de cima para baixo, mas ele não inicia na primeira função, ele registra ela, depois registra a segunda e assim vai, mas quando ele encontra uma função sendo chamada como port_scanner(ip) logo após as duas funções, ele é executado entrando primeiro na port_scanner() e dentro da função quando for vai percorrendo as portas a outra função é chamada scan_port() e ai elá entra nessa função e começa percorrer seu código chegando na s.connect(ip de algo, 1), 1 é equivalente ao for da outra função.

linkar os dias dentro de uma página só 100 days of cybersecurity

mostrar quais portas foram paradas pelo firewall e quais estavam fechadas, caso o usuário queira.

KeyboardInterrupt ocorre quando um usuário interrompe manualmente a execução de um programa python geralmente pressionando ctrl+c.

# testes

O uso ThreadPoolExecutor permite o parelismo de código, e o python possui duas maneiras de alcançar esse paralelismo. Primeiro o multithreading ideal para acelerar tarefas com uso intensivo de entrada/saída como requisições web. São tarefas que exigem mais de CPU.

ThreadPoolExecutor é usada para gerenciar e criar threads de forma eficiente. Criar grandes quantidades é ineficiente. O pool monitora e gerencia o ciclo de vida dos threads.

- max_workers: é numero de threads, também conhecido como tamanho do pool. Esse é o limite máximo de trabalhadores que poderão ser utilizados.
- thread_name_prefix: o parâmetro thread_name_prefix foi adicionado.
- Inicializador: o inicializador recebe uma função que é invocada.
- initargs: É uma tupla de argumentos passados para o inicializador.
- submit: executa uma função ou um método e retorna um objeto future representado o estado de execução do método. O future representa uma tarefa submetida, permitindo consultar posteriormente.

Função Main é comumente usada para organizar a lógica principal de um programa.

**main** é o nome do ambiente onde o código de nível superior é executado.
**name** é uma variável especial do python.
**name** == **main**, se for verdadeiro ele executa o código dentro do if, se for falso não executa.

## Missão

- resolver o bug de python3 portscan.py 127.0.0.1, executa sem opção porta
- precisamos tirar ip global do código X
- resolver a lógica de if e else em parameters. X
- adicionar a devolução de banners
- adicionar main function X
