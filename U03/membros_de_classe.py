import DaClasse as dc

print('Cria objetos DaClasse')
# Cria um objeto com nome obj1
obj1 = dc.DaClasse('obj1')
print(obj1)

# Cria um segundo objeto com nome obj2
obj2 = dc.DaClasse('obj2')
print(obj2)

print('\nAltera var pública de instância em obj1')
# Altera variável de instância pública do obj1
obj1.nome = 'Objeto 1'
# Alteração no obj1 pode ser observada
print(obj1)
# Alteração no obj1 não produz efeito no obj2
print(obj2)

print('\nAltera var pública de instância em obj2')
# Altera variável de instância pública do obj2
obj2.nome = 'Objeto 2'
# Alteração no obj2 pode ser observada
print(obj2)
# Alteração no obj2 não produz efeito no obj1
print(obj1)

print('\nAltera var pública de classe')
# Altera variável de classe pública de DaClasse
dc.DaClasse.classe_publico = 'INCOMUM'
# Alteração na classe produz efeito no obj1
print(obj1)
# Alteração na classe produz efeito no obj2
print(obj2)

print('\nAltera var privada de classe')
# Altera variável de classe privada de DaClasse
dc.DaClasse.set_classe_privado('RESTRITO')
# Alteração na classe produz efeito no obj1
print(obj1)
# Alteração na classe produz efeito no obj2
print(obj2)
