# Definição de função que produz exceção quando a=0 ou b=0 
def razao(a, b):
    '''Calcula a razão da soma pelo produto.'''
    try:
        return (a + b) / (a * b)
    except TypeError as exc:
        raise ValueError('Argumento(s) inválido(s).')


# Chamada da função com argumentos válidos
print(20*'-')
print('Chamada da função com argumentos válidos')
a = 5
b = 21
res = razao(a, b)
print(f'({a} + {b}) / ({a} * {b}) = {res}')
print(20*'-')

# Chamada da função com um argumento inválido (b=0)
# Exceção ZeroDivisionError é admissível
print('Chamada da função com um argumento inválido (b=0)')
a = 5
b = 0
try:
    res = razao(a, b)
    print(f'({a} + {b}) / ({a} * {b}) = {res}')
except Exception as e:
    print(e)
print(20*'-')

# Chamada da função com um argumento inválido (b='21')
# Exceção TypeError não é adequada, ValueError seria melhor
print("Chamada da função com um argumento inválido (b='21')")
a = 5
b = '21'
try:
    res = razao(a, b)
    print(f'({a} + {b}) / ({a} * {b}) = {res}')
except Exception as e:
    print(e)
print(20*'-')
