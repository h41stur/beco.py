# importando as libs
import socket
import sys

# checa a quantidade de argumentos
if len(sys.argv) < 2:
    print(f"""
        Modo de uso:
            {sys.argv[0]} <port>
            """)
    sys.exit()

# recebe os argumentos
port = int(sys.argv[1])
host = '' # mesma coisa que 0.0.0.0

# abre o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1) # quantas conexões vou aguardar antes de parar de ouvir

print('[+] Ouvindo conexões...')

while True:
    con, client = s.accept()
    print(f"[+] Recebendo conexão de {client}")

    while True:
        msg = input("> ")
        if msg == 'sair':
            con.close()
            break
        con.send(msg.encode() + b'\n')
        resp = con.recv(1024)
        print(resp.decode())
    con.close()
    break