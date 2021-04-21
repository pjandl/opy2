# Funções podem ser usadas na list comprehension
# Uma função
def fahrenheit_para_celsius(f):
    return 5*(f - 32)/9


if __name__ == '__main__':
    print('Usos de List Comprehension 2 (*)\n')

    # List comprehension pode usar expressões complexas
    lista3 = [(9/5)*c + 32 for c in range(0, 101, 10)]
    print('lista3*:\n', lista3)

    # Uma lista existente pode fornecer os valores para a expressão da list comprehension
    lista2 = [2*n for n in range(10+1)]
    lista4 = [x + 1 for x in lista2]
    print('lista4*:\n', lista4)

    # Strings podem se transformar numa lista de seus caracteres
    lista5 = [c for c in 'Oficina Python 2']
    print('lista5*:\n', lista5)

    # Pode ser aplicado um condicional para filtrar os elementos do for
    dados = [78, -91, 15, 0, -5, 88 , 97]
    print('dados  :\n', dados)    
    lista6 = [x/2 for x in dados if x > 0]
    print('lista6*:\n', lista6)

    # É possível aninhar operações de list comprehension
    lista7 = [f/2 for f in [(9/5)*c + 32 for c in range(0, 101, 10)]]
    print('lista7*:\n', lista7)

    # List comprehension com função
    lista8 = [fahrenheit_para_celsius(f) + 273 for f in lista7]
    print('lista8*:\n', lista8)
