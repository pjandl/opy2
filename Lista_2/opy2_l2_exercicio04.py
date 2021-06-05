if __name__ == '__main__':
    print('Escrita de Arquivo JSON')
    nome = input('Nome completo? ')
    idade = int(input('Idade (anos completos)? '))
    cidade = input('Cidade natal? ')
    estado = input('Estado natal? ')

    # Abertura do arquivo para escrita
    arquivo = open(nome + '.json', 'w')

    # Escrita do conteúdo
    arquivo.write('{\n')
    arquivo.write(f'\t"NOME" : "{nome}",\n')
    arquivo.write(f'\t"IDADE" : "{idade}",\n')
    arquivo.write(f'\t"CIDADE" : "{cidade}",\n')
    arquivo.write(f'\t"UF" : "{estado.upper()}"\n')
    arquivo.write('}\n')

    # Fechamento do arquivo
    arquivo.close()
