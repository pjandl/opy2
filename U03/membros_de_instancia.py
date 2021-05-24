import DaInstancia as di

print('Cria objetos DaInstancia')
# Cria um objeto com valor inicial 10
obj1 = di.DaInstancia('obj1', 10)
print(obj1)

# Cria um segundo objeto com valor inicial 20
obj2 = di.DaInstancia('obj2', 20)
print(obj2)

print('\nAltera var pública de instância em obj1')
# Altera variável de instância pública de obj1 para valor 15
obj1.valor_publico = 15
print(obj1)
# Alteração no obj1 não produz efeito no obj2
print(obj2)

print('\nAltera var pública de instância em obj2')
# Altera variável de instância pública de obj2 para valor 25
obj2.valor_publico = 25
# Alteração no obj1 não produz efeito no obj2
print(obj1)
print(obj2)

print('\nAltera var privada de instância em obj1')
# Altera variável de instância privada de obj1 para valor 2
# com uso de método público de instância.
obj1.set_valor_privado(2)
print(obj1)
# Alteração no obj1 não produz efeito no obj2
print(obj2)

print('\nAltera var privada de instância em obj2')
# Altera variável de instância privada de obj2 para valor 5
# com uso de método público de instância.
obj2.set_valor_privado(5)
print(obj2)
# Alteração no obj2 não produz efeito no obj1
print(obj1)
