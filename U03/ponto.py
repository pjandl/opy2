class Ponto:
    '''Representação de um ponto num plano cartesiano por meio
       de coordenadas x e y.'''

    def __init__(x = 0, y = 0):
        '''Construtor'''
        self.x = x
        self.y = y

    def translate(x, y):
        '''Move ponto para coordenada'''
        self.x = x
        self.y = y
        
