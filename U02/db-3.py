# importação do módulo SQLite3
import sqlite3
# importação de módulo para leitura de CSV
from csv import reader

# Definição de comando SQL parametrizável
sql8 = 'INSERT INTO Dados (Codigo,Data,Precip_Tot,Temp_Max,Temp_Med,Temp_Min,Umid_Relat) ' \
       'values (?, ?, ?, ?, ?, ?, ?)'

# Funcão que efetua leitura do arquivo CSV inserindo
def inserir_dados(nome_arquivo, estacao):
    with open(nome_arquivo, 'r') as file_reader:
        # Usa file handler para criação de um leitor de CSV
        csv_reader = reader(file_reader, delimiter=';')
        # Usa objeto reader para criar lista de listas com list()
        list_of_rows = list(csv_reader)
        list_of_rows.pop(0) # remove o cabeçalho
        # Percorre lista de listas, efetuando uma inserçao
        for row in list_of_rows:
            print(row)
            # Executa instrução SQL inserindo parâmetros
            cursor.execute(sql8, row)
            print('Executado:', sql8)
    # Consolida transação
    cursor.connection.commit()
    return


# Obtenção de conexão
con = sqlite3.connect('metereologia.db')
print('Conexão:', con)

# Criação do cursor
cursor = con.cursor()
print('Cursor:', cursor)

# Inserção de dados
inserir_dados('arquivos/dados_A701_D_2021-01-01_2021-03-06.csv', 'A701')
inserir_dados('arquivos/dados_A744_D_2021-01-01_2021-03-06.csv', 'A744')

# Fechar a conexão encerra os cursores abertos.
cursor.close() # opcional
con.close()
