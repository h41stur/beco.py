# importando as libs
import socket
import sys

# checa a quantidade de argumentos
if len(sys.argv) < 2:
    print(f"""
        Modo de uso:
            {sys.argv[0]} <host> 
            """)
    sys.exit()

# recebe os argumentos
host = str(sys.argv[1])

# para cada porta, abre um socket e checa a resposta
for i in range(20, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    resp = s.connect_ex((host, i))
    s.close()
    if resp == 0:
        print(f"[+] PORTA ABERTA -> {i}")
