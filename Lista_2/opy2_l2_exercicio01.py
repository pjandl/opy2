if __name__ == '__main__':
    print('Leitura de Arquivo Texto')
    nome_arquivo = input('Nome do arquivo? ')

    # Abertura do arquivo para leitura
    arquivo = open(nome_arquivo, 'r')

    # Leitura do conteúdo
    conteudo = arquivo.read()
    print('Conteúdo', 20*'-')
    print(conteudo)
    print(29*'-')
    print('Tamanho:', arquivo.tell())

    # Fechamento do arquivo
    arquivo.close()
