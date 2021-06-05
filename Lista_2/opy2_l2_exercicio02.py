if __name__ == '__main__':
    print('Escrita de Arquivo Texto')
    nome = input('Nome completo? ')
    idade = int(input('Idade (anos completos)? '))
    cidade = input('Cidade natal? ')
    estado = input('Estado natal? ')

    # Abertura do arquivo para escrita
    arquivo = open(nome + '.txt', 'w')

    # Escrita do conteúdo
    arquivo.write(f'NOME: {nome}\n')
    arquivo.write(f'IDADE: {idade}\n')
    arquivo.write(f'CIDADE: {cidade} - {estado.upper()}\n')

    # Fechamento do arquivo
    arquivo.close()
