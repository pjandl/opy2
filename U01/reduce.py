# Importação da função reduce do módulo functools
from functools import reduce

# Definição de função tradicional com dois parâmetros
def menor(x, y):
    if x < y:
        return x
    else:
        return y

    
if __name__ == '__main__':
    print('Reduce\n')

    # Definição de função com lambda com dois parâmetros
    soma = lambda x, y : x + y

    # Considere a lista de inteiros que segue
    valor = [31, 35, 64, 68, 95]
    print('valor:\n', valor)
    print()

    # Redução da lista valor com aplicação da função soma
    resultado = reduce(soma, valor)
    print('reduce: soma da lista =', resultado)
    
    # Definição de função com lambda com dois parâmetros
    produto = lambda x, y : x * y

    # Redução da lista valor com aplicação da função produto
    resultado = reduce(produto, valor)
    print('reduce: produto da lista =', resultado)

    print('reduce: valor mínimo da lista =', reduce(menor, valor))

    # Definição de lambda contendo condicional
    maior = lambda x, y : x if (x > y) else y

    print('reduce: valor máximo da lista =', reduce(maior, valor))
