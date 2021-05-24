from hierarquia import Pessoa, Funcionario, Gerente

def secao(nome):
    print(20*'-')
    print(nome)
    print(20*'-')
    
secao('Pessoa')
# Instanciação de objeto tipo Pessoa
alguem = Pessoa()
print('Nome:', alguem.nome)
print(alguem)

# Instanciação de outro objeto tipo Pessoa
prof = Pessoa('Peter')
print('Nome:', prof.nome)
print(prof)

secao('Funcionario')
# Instanciação de objetos tipo Funcionario
func1 = Funcionario('Peter Jandl Jr', 114)
func2 = Funcionario('Claudio Oliveira', 114)
func3 = Funcionario('Viviane Ramalho', 183)
func4 = Funcionario('Cristina Becker', 183)

print('Lista')
# Criação de lista de objetos Funcionario
listaFunc = [func1, func2, func3, func4]
for f in listaFunc:
    print(f)

print('Filtragem')
# Filtragem de funcionários da lista
for f in filter(lambda i : i.lotacao == 183, listaFunc):
    print(f)

secao('Gerente')
# Instanciação de objetos tipo Gerente
diretor1 = Gerente('Francesco Bordignon', 0, 114)
diretor2 = Gerente('Marcos Maia', 0, 183)

print('Lista')
# Criação de lista de objetos Gerente
listaDir = [diretor1, diretor2]
for d in listaDir:
    print(d)

print('Filtragem')
# Listagem dos funcionários de cada gerente (for aninhados)
for d in listaDir:
    print(d)
    for f in listaFunc:
        if f.lotacao == d.depto:
            print('\t', f)

# Listagem dos funcionários de cada gerente (for e filtragem)
for d in listaDir:
    print(d)
    for f in filter(lambda i : i.lotacao == d.depto, listaFunc):
        print('\t',f)
