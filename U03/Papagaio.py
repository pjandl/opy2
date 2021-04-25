class Papagaio:
    '''Uma classe simples para entender OO.'''

    def __init__(self):
        '''Construtor, método especial que cria objeto desta classe.'''
        # define nome como atributo de instância (para cada um dos objetos desta classe)
        self.nome = 'Papagaio'
        # define idade como atributo de instância (para cada um dos objetos desta classe)
        self.idade = None
        print('Papagaio criado por __init__()')
        
    def meu_nome(self):
        '''Este método realiza uma ação (não tem retorno de valor).'''
        print('Meu nome é', self.nome)

    def minha_idade(self):
        '''Este método efetua retorno de valor, a idade.'''
        return self.idade

    def fala(self, frase):
        '''Este método usa um parâmetro para realizar sua ação.'''
        for c in range(2):
            print(self.nome, frase)  
