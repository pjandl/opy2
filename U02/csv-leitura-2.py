from csv import reader

nome_arquivo = 'tabela.csv'

# Lê arquivo csv como um lista de listas
with open(nome_arquivo, 'r') as file_reader:
    # Usa o file handler para criar um leitor CSV
    csv_reader = reader(file_reader, delimiter=';')
    print(csv_reader)
    # Usa o reader para obter uma lista of listas
    lista_de_registros = list(csv_reader)
# Arquivo é fechado, mantendo lista de registros
print(lista_de_registros)

# Laço permite processar campos individualmente
for registro in lista_de_registros:
    campos = list(registro)
    print(campos)
