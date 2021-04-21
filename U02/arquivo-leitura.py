# Abertura de arquivo em modo r (leitura), exige que o arquivo exista
filename = "/Users/Jandl/Desktop/Oficina Python/opy2/Notebooks U02/arquivos/programacao.txt"
arquivo1 = open(filename, "r")

# Leitura e exibição do conteúdo do arquivo
print('Conteúdo do arquivo:', arquivo1)
print(40*'=')
print(arquivo1.read())
print(40*'=')

# tell() retorna posição de leitura no arquivo (= tamanho lido)
print('Tamanho =', arquivo1.tell())

# Novas leitura após atingir final não retornam conteúdo
print(40*'=')
print(arquivo1.read())
print(40*'=')

# tell() retorna a mesma posição (= tamanho lido)
print('Tamanho =', arquivo1.tell())

# seek() movimenta o cursor e retorna sua posição após movimentação
# primeiro argumento: posição
# segundo argumento: referência, início (0), fim (1), posição atual (2)
print('Movimentação para', arquivo1.seek(0, 0)) # início do arquivo

# tell() retorna a mesma posição
print('Posição =', arquivo1.tell())

# nova movimentação
print('Movimentação para', arquivo1.seek(28, 0)) # posição 28 a partir do início do arquivo
# tell() retorna a mesma posição
print('Posição =', arquivo1.tell())

# read() também efetua a leitura de um número determinado de caracteres
print(40*'=')
trecho = arquivo1.read(8)
print(trecho)
print(40*'=')

# fechamento do arquivo
arquivo1.close()
print('Arquivo fechado')

