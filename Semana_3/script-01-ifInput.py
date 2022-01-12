
timeout = 30
timeout_inp = int(input('Insira o timeout esperado: '))

if timeout_inp > timeout:
    print("[-] Timeout escedido!")
else:
    print("[+] Timeout dentro do limite!")
