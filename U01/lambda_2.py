import random as rnd

if __name__ == '__main__':
    print('Lambdas 2\n')

    # Expressões lambda são apropriadas para criar funções simples
    first = lambda lista : lista[0]
    last = lambda lista : lista[-1]

    # Uso de list comprehension para criar lista com conteúdo aleatório
    lista = [rnd.randint(0, 11) for x in range(5)]

    # Exibe lista e usa funções criadas como lambdas
    print('lista:\n', lista)
    print('first...last:\n', first(lista), '...', last(lista))

    # Definição de lambda com dois parâmetros
    razao = lambda x, y : (x*y)/(x+y)
    print()
    
    # uso da função lambda com laços for
    dados = []
    for x in range(1, 4):
        for y in range(1, 4):
            dados.append(razao(x, y))
    print('dados (com lambda):\n', dados)

    # uso da função lambda em list comprehension
    dados = [razao(x, y) for x in range(1,4) for y in range(1,4)]
    print('dados (com lambda e list comprehension):\n', dados)
    print()

    # Definição de lambda contendo condicional
    print('lambda com condicional')
    menor = lambda x, y : x if x < y else y

    a = 100
    b = 33

    print(f'O menor valor entre {a} e {b} é {menor(a, b)}.')

    # Expressões lambda com condicionais
    first = lambda lista : lista[0] if len(lista) > 0 else None
    last = lambda lista : lista[-1] if len(lista) > 0 else None

    lista = []
    print(lista, ':', first(lista), '...', last(lista))
    lista = ['único']
    print(lista, ':', first(lista), '...', last(lista))
    lista = ['primeiro', 2, 3, 4, 5, 'último']
    print(lista, ':', first(lista), '...', last(lista))
