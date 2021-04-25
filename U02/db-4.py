# importação do módulo SQLite3
import sqlite3

# Define função para exibir dados da tabela Dados
def lista_dados(dados):
    # Exibição dos dados consultados de maneira tabular
    print('| %-8s | %-10s | %-10s | %-10s | %-10s | %-10s | %-10s |' %
          ('Estacao', 'Data', 'Precip', 'TMax', 'TMed', 'TMin', 'Umid'))
    print('+-%8s-+-%10s-+-%10s-+-%10s-+-%10s-+-%10s-+-%10s-+' % 
          (8*'-', 10*'-', 10*'-', 10*'-', 10*'-', 10*'-', 10*'-'))
    for registro in dados:
        print('| %-8s | %-10s | %10s | %10s | %10s | %10s | %10s |' % registro)
    print('+-%8s-+-%10s-+-%10s-+-%10s-+-%10s-+-%10s-+-%10s-+' % 
          (8*'-', 10*'-', 10*'-', 10*'-', 10*'-', 10*'-', 10*'-'))
    return


# Obtenção de conexão
con = sqlite3.connect('metereologia.db')
print('Conexão:', con)

# Criação do cursor
cursor = con.cursor()
print('Cursor:', cursor)

# SQL DQL (consulta a dados)
sql9 = 'SELECT * FROM DADOS'
# Execução do comando SQL
cursor.execute(sql9)
print('Executado:', sql9)

# Recuperação dos dados
dados = cursor.fetchall()

# Listagem parcial dos dados (usa fatiamento e soma de listas)
lista_dados(dados[:10]+dados[-10:])

# Nova consulta com filtragem de dados
sql10 = "SELECT * FROM DADOS WHERE Precip_Tot > 40"
cursor.execute(sql10)
print('Executado:', sql10)
dados_parciais = cursor.fetchall()
lista_dados(dados_parciais)

# Não esqueça de consolidar as ações realizadas.
# Fechar a conexão encerra os cursores abertos.
cursor.close() # opcional
con.close()
