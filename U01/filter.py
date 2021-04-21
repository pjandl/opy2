# Uma função lógica
def impar(valor):
    if valor % 2 == 1:
        return True
    else:
        return False

# Outra função lógica
def maior50(valor):
    return valor > 50

    
if __name__ == '__main__':
    print('Filter\n')

    # Uma lista com inteiros
    lista = [97, 70, 10, 44, 79, 2]
    print('lista:\n', lista)
    print()

    # Filtragem da lista com função lógica ímpar
    filter(impar, lista)

    # A função filter retorna um iterator que pode transformado em uma lista
    print('Filtragem ímpares:\n', list(filter(impar, lista)))
    print()

    # O iterator retornado por filter pode ser percorrido diretamente num laço for
    for v in filter(maior50, lista):
        print('Filtragem maior 50:\n', v)
    print()

    # Pode ser empregada uma lambda
    for v in filter(lambda x : x >= 10 and x <=20, lista):
        print('Filtragem com lambda:\n', v)
