if __name__ == '__main__':
    lista = []
    # Entrada de dados
    while len(lista) < 10:
        try:
            msg = f'Digite {len(lista) + 1}o valor inteiro: '
            valor = int(input(msg))
            lista.append(valor)
        except:
             print('Valor inválido como inteiro!')

    print(lista)
