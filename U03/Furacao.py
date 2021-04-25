import datetime as dt

class Furacao:
    '''Representa um furacão (tempestade tropical ou ciclone).'''
    
    def __init__(self, nome, ano, categoria):
        '''Construtor requer nome, ano e categoria.'''
        # valida parâmetro nome
        self.__setNome(nome)
        # valida parâmetro ano
        self.setAno(ano)
        # valida parâmetro categoria
        self.setCategoria(categoria)
        
    def __setNome(self, nome):
        '''Valida atribuição de nome ao furacão. '''
        if type(nome) != str:
            raise ValueError(f'nome \'{nome}\' não é de tipo string')
        if len(nome) < 2:
            raise ValueError(f'nome \'{nome}\' deve possuir 2 ou mais caracteres')
        # define/modifica atributo privado contendo nome
        self.__nome = nome

    def getNome(self):
        '''Obtém nome do furacão.'''
        return self.__nome

    def setAno(self, ano):
        '''Valida atribuição de ano ao furacão. '''
        # obtém ano corrente
        currentYear = dt.datetime.now().year
        if ano <= 0 or ano > currentYear:
            raise ValueError(f'ano \'{ano}\' inválido')
        # define/modifica atributo privado contendo ano
        self.__ano = ano

    def getAno(self):
        '''Obtém ano do furacão.'''
        return self.__ano

    def setCategoria(self, categoria):
        '''Valida atribuição de categoria ao furacão. '''
        if categoria < 1 or categoria > 5:
            raise ValueError(f'categoria \'{categoria}\' inválida')
        # define/modifica atributo privado contendo categoria
        self.__categoria = categoria

    def getCategoria(self):
        '''Obtém categoria do furacão.'''
        return self.__categoria

