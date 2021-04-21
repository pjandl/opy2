# Leitura de arquivo CSV é como leitura de arquivos de texto.
nome_arquivo = 'tabela.csv'

with open(nome_arquivo, 'rt') as f:
    # leitura do arquivo
    conteudo = f.read();
# o arquivo é fechado automaticamente

# função split permite dividir conteúdo em uma lista de linhas (registros)
lista = conteudo.split();
print(lista)

# extração do cabeçalho e divisão em campos com split(separador)
cabecalho = lista[0].split(';')
print('Cabeçalho:\n\t', cabecalho)

# fatiamento para obtenção das linhas 1 e 2
registro = lista[1:3]
print('Registros 1 e 2:\n\t', registro)

# cada registro, ou seja, tanto o cabeçalho como cada linha,
# podem ser dividido em campos com split(separador)  
for r in registro:
    print('Registro:', r)
    campos = r.split(';') # separador é o ;
    for c in range(len(cabecalho)):
        print(f'\t{cabecalho[c]} : {campos[c]}') 
