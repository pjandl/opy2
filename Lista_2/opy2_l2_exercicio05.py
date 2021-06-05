if __name__ == '__main__':
    print('Escrita de Arquivo CSV')

    # Abertura do arquivo para escrita
    arquivo = open('temperaturas.csv', 'w')

    # Escrita do conteúdo
    arquivo.write('id;K;C;F\n')
    id = 1
    for temp_k in range(0, 501, 5):
        temp_c = temp_k - 273
        temp_f = (9/5)*temp_c + 32
        saida = f'{id};{temp_k};{temp_c};{temp_f:.1f}\n'
        arquivo.write(saida)
        print(saida, end='')
        id += 1

    # Fechamento do arquivo
    arquivo.close()
