# Definição de função que produz exceção quando a=0 ou b=0 
def razao(a, b):
    '''Calcula a razão da soma pelo produto.'''
    assert a != 0, 'a == 0'
    assert b != 0, 'b == 0'
    
    return (a + b) / (a * b)


# Teste o uso da função para qualquer caso!
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
res = razao(a, b)
print(f'({a} + {b}) / ({a} * {b}) = {res}')
