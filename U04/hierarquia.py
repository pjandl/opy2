# Classe para definir uma entidade
class Pessoa:
    def __init__(self, nome='Anônimo'):
        self.nome = nome
        
    def __str__(self):
        return f'Pessoa[nome={self.nome}]';


# Herança (direta, primeiro nível)
class Funcionario(Pessoa):
    def __init__(self, nome, lotacao):
        # aciona construtor da superclasse
        super().__init__(nome)
        self.lotacao = lotacao
    
    def __str__(self):
        return f'Funcionario[nome={self.nome},' \
               f'lotacao={self.lotacao}]'

# Herança (indireta, segundo nível)
class Gerente(Funcionario):
    def __init__(self, nome, lotacao, depto):
        # aciona construtor da superclasse
        super().__init__(nome, lotacao)
        self.depto = depto
    
    def __str__(self):
        return f'Gerente[nome={self.nome},' \
               f'lotacao={self.lotacao},depto={self.depto}]'
