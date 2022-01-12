contador = 1

with open('userPass.txt', 'r') as f:
    for i in f:
        i = i.strip()
        i = i.split(":")
        u = i[0]
        p = i[1]
        print(f'[+] O usuário numero {contador} da lista é: {u}, e sua senha é: {p}')
        contador += 1