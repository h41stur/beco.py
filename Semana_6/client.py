# importando as libs
import socket
import sys

# checa a quantidade de argumentos
if len(sys.argv) < 2:
    print(f"""
        Modo de uso:
            {sys.argv[0]} <host> <port>
            """)
    sys.exit()

# recebe os argumentos
host = str(sys.argv[1])
port = int(sys.argv[2])

# abre o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# loop infinito para troca de mensagens
while True:
    msg = input("> ")
    if msg == 'sair':
        s.close()
        break
    s.send(msg.encode() + b'\n')
    while True:
        resp = s.recv(2048)
        print(resp.decode())
        break
    

s.close()