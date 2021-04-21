# Abertura de arquivo em modo r (leitura), exige que o arquivo exista
nome_arquivo = "/Users/Jandl/Desktop/Oficina Python/opy2/Notebooks U02/arquivos/pessoas.txt"

# abertura e utilização do arquivo
with open(nome_arquivo, 'r') as f:
    # leitura do arquivo
    conteudo = f.read();
    tamanho = f.tell();
# o arquivo é fechado automaticamente

print(f'Arquivo: {nome_arquivo} ({tamanho} bytes)')
print(30*'-')
print(conteudo)
print(30*'-')
