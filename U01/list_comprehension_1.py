if __name__ == '__main__':
    print('List Comprehension 1 (*)\n')

    # Criação padrão de uma lista com o uso de colchetes
    lista1 = []

    # Preenchimento da lista com uso de for+range
    for n in range(10):
        lista1.append(n)
    print('lista1 :\n', lista1)


    # Recria lista com valores de 0 a 9 com uso de list comprehension onde:
    # n é a expressão (que tem a variável n apenas)
    # for n in range(10) é o laço que dá valores para n
    lista1 = [n for n in range(10)]
    print('lista1*:\n', lista1)

    # Cria lista com valores pares de 0 a 20  com uso de for e range
    lista2 = []
    for n in range(10+1):
        lista2.append(2*n)
    print('lista2 :\n', lista2)

    # Recria lista com valores pares de 0 a 20 com uso de list comprehension onde:
    # 2*n é a expressão (que tem a variável n apenas)
    # for n in range(10+1) é o laço que dá valores para n
    lista2 = [2*n for n in range(10+1)]
    print('lista2*:\n', lista2)
