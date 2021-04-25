# importação do módulo SQLite3
import sqlite3

# Conexão com banco de dados SQLite
# Se o banco de dados não existir, ele será criado
con = sqlite3.connect('metereologia.db')
print('Conexão:', con)

# A partir da conexão, usualmente cria-se um cursor para
# possibilitar a execução de comandos SQL no BD.
cursor = con.cursor()
print('Cursor:', cursor)

# SQL DDL (remoção das tabelas) 
sql0 = ['DROP TABLE ESTACOES',
        'DROP TABLE PARAMETROS',
        'DROP TABLE DADOS']

# Execução de comando SQL requer um cursor pré-definido.
for cmd in sql0:
    try:
        # o mesmo cursor é usado para executar vários comandos
        cursor.execute(cmd)
    except Exception as exc:
        print(exc)
# SQL DTL (consolidação de operações)
con.commit()

# SQL DDL (criação de tabela)
sql1 = '''CREATE TABLE ESTACOES (
    Codigo varchar(8) PRIMARY KEY,
    Nome varchar(40) not null,
    Latitude float not null,
    Longitude float not null,
    Altitude integer not null
)'''
# Execução do comando SQL é feita com cursor
cursor.execute(sql1)
print('Executado:', sql1)

# SQL DDL (criação de tabela)
sql2 = '''CREATE TABLE PARAMETROS (
    Coluna varchar(15) PRIMARY KEY,
    Descricao varchar(40) not null,
    Unidade varchar(5) not null
)'''
# Execução do comando SQL é feita com cursor
cursor.execute(sql2)
print('Executado:', sql2)

# SQL DDL (criação de tabela)
sql3 = '''CREATE TABLE DADOS (
    Codigo varchar(8),
    Data date not null,
    Precip_Tot float null,
    Temp_Max float null,
    Temp_Med float null,
    Temp_Min float null,
    Umid_Relat float null,
    PRIMARY KEY (Codigo, Data), 
    FOREIGN KEY (Codigo) references Estacoes(Codigo)
)'''
# Execução do comando SQL é feita com cursor
cursor.execute(sql3)
print('Executado:', sql3)

# SQL DTL (consolidação de operações)
con.commit()

# Fechar a conexão encerra os cursores abertos.
cursor.close() # opcional
con.close()
