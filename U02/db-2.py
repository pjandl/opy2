# importação do módulo SQLite3
import sqlite3

# Define função para exibir dados da tabela Estacoes
def lista_estacoes(dados):
    # Exibição dos dados consultados de maneira tabular
    print('| %-8s | %-40s | %-12s | %-12s | %-8s |' % ('Código', 'Nome', 'Latitude', 'Longitude', 'Altitude'))
    print('+-%8s-+-%40s-+-%12s-+-%12s-+-%8s-+' % (8*'-', 40*'-', 12*'-', 12*'-', 8*'-'))
    for registro in dados:
        print('| %-8s | %-40s | %12.6f | %12.6f | %8d |' % registro)
    print('+-%8s-+-%40s-+-%12s-+-%12s-+-%5s-+' % (8*'-', 40*'-', 12*'-', 12*'-', 8*'-'))
    return


# Conexão com banco de dados SQLite
# Se o banco de dados não existir, ele será criado
con = sqlite3.connect('metereologia.db')
print('Conexão:', con)

# A partir da conexão, usualmente cria-se um cursor para
# possibilitar a execução de comandos SQL no BD.
cursor = con.cursor()
print('Cursor:', cursor)

# SQL DQL (consulta a dados)
sql4 = 'SELECT Codigo, Nome, Latitude, Longitude, Altitude FROM ESTACOES'

# Realização de consulta também emprega cursor
cursor.execute(sql4)
print('Executado:', sql4)

# Dados da consulta realizada devem ser recuperados
dados = cursor.fetchall()
print('type(dados):', type(dados))

# Mostra dados da tabela estações
lista_estacoes(dados)

# Inserçao de dados em tabela
# SQL DDL (inserção/criação de dados)
sql5 = "INSERT INTO ESTACOES(Codigo, Nome, Latitude, Longitude, Altitude) "\
        "VALUES('A744', 'BRAGANCA PAULISTA', -22.951944, -46.530556, 891)"
# Observe o uso de aspas duplas (para definir a string Python)
# e aspas simples (para delimitar string no SQL)

# Realização de inserção, como sempre, emprega cursor
cursor.execute(sql5)
print('Executado:', sql5)

# Consolida inserção
con.commit()

# Realização de consulta também emprega cursor
cursor.execute(sql4)
# Dados da consulta realizada devem ser recuperados
dados = cursor.fetchall()
print('type(dados):', type(dados))

# Mostra dados da tabela estações
lista_estacoes(dados)

sql6 = "INSERT INTO ESTACOES(Codigo, Nome, Latitude, Longitude, Altitude) "\
        "VALUES('A706', 'CAMPOS DO JORDAO', -22.7502777, -45.6038888, 891)"
sql7 = "INSERT INTO ESTACOES(Codigo, Nome, Latitude, Longitude, Altitude) "\
        "VALUES('A701', 'SAO PAULO - MIRANTE', -23.496294, 46.620088, 786)"

# Realização de inserção, como sempre, emprega cursor
cursor.execute(sql6)
print('Executado:', sql6)
cursor.execute(sql7)
print('Executado:', sql7)

# Consolida inserção
con.commit()

# Realização de consulta também emprega cursor
cursor.execute(sql4)
# Dados da consulta realizada devem ser recuperados
dados = cursor.fetchall()
# Mostra dados da tabela estações
lista_estacoes(dados)

# Fechar a conexão encerra os cursores abertos.
cursor.close() # opcional
con.close()
