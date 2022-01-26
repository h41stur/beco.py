#!/usr/bin/python3

import mysql.connector as mysql
import sys
from getpass import getpass
import csv

banner = '''
 ██████╗ █████╗ ██████╗ ██████╗ ███████╗████████╗██╗███╗   ██╗██╗  ██╗ █████╗ 
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║████╗  ██║██║  ██║██╔══██╗
██║     ███████║██████╔╝██████╔╝█████╗     ██║   ██║██╔██╗ ██║███████║███████║
██║     ██╔══██║██╔══██╗██╔══██╗██╔══╝     ██║   ██║██║╚██╗██║██╔══██║██╔══██║
╚██████╗██║  ██║██║  ██║██║  ██║███████╗   ██║   ██║██║ ╚████║██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                              
 ██████╗███████╗██╗   ██╗                                                     
██╔════╝██╔════╝██║   ██║                                                     
██║     ███████╗██║   ██║                                                     
██║     ╚════██║╚██╗ ██╔╝                                                     
╚██████╗███████║ ╚████╔╝                                                      
 ╚═════╝╚══════╝  ╚═══╝       

'''

print(banner)

host = input("Informe o host: ")
usr = input("Informe o usuario: ")
passwd = getpass("Informe a senha: ")
block = ["update", "insert", "delete", "drop", "create", "alter", "grant"]
cont = ""

def databases(host, usr, passwd):
    try:
        db = mysql.connect(
                host = host,
                user = usr,
                passwd = passwd,
                use_pure = True,
                charset = 'utf8'
                )
        print("\nConectando ao banco...")
        cursor = db.cursor()
        print("\nDatabases:\n")
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        for database in databases:
            print(database)
    except mysql.errors.ProgrammingError:
        print("\nErro ao conectar com o banco!")
        sys.exit()
    db.close()

def query(host, usr, passwd, dbname, tables, path):
    try:
        db = mysql.connect(
                host = host,
                user = usr,
                passwd = passwd,
                db = dbname,
                use_pure = True,
                charset = 'utf8'
                )
        cursor = db.cursor()
        if tables == "s":
            cursor.execute("SHOW TABLES")
            tabelas = cursor.fetchall()
            for i in tabelas:
                print(i)
        sql = input("\nDigite a query: ")
        sql = sql.lower()
        
        for i in block:
            if i in sql:
                print(f"\nVoce não pode executar comandos de {i}!")
                db.close()
                sys.exit()
        
        cursor.execute(sql)
        result = cursor.fetchall()
        
        arquivo = csv.writer(open(path, "w", newline=''))
        for i in result:
            arquivo.writerow(i)
        print("Exportado com sucesso!")
    except mysql.errors.ProgrammingError:
        print("\nErro ao conectar com o banco!")
        sys.exit()
    db.close()
    print("\nObrigado!")

def export():
    global cont
    cont = input("\nDeseja exportar dados para um csv?[s/n]: ")
    path = input("\nInforme o caminho e nome para salvar o CSV: ")
    if cont == "s":
        dbname = input("\nQual database deseja utilizar? ")
        tables = input("\nDeseja listar as tabelas?[s/n]: ")
        query(host, usr, passwd, dbname, tables, path)
    elif cont == "n":
        print("\nObrigado!")
    else:
        print('\nEscolha "s" ou "n"!')
        export()

databases(host, usr, passwd)
export()
sys.exit()
