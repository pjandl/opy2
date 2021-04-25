class Papagaio:
    '''Uma classe simples para entender OO.'''

    def __init__(self):
        '''Construtor, método especial que cria objeto desta classe.'''
        print('Papagaio.__init__()')
        # define nome como atributo de instância (para cada um dos objetos desta classe)
        self.nome = 'Papagaio'

# Programa: processado apenas quando este arquivo é executado,
# mas não quando o arquivo é importado
if __name__ == '__main__':
    # Instanciação de objeto Papagaio
    louro = Papagaio()
    
    # Obtém e imprime atributo do objeto
    print('louro.nome:', louro.nome)

    # Atributos/campos podem ser modificados
    louro.nome = 'Louro'
    print('louro.nome:', louro.nome)

    # Outros objetos (tantos quantos necessários) podem ser criados
    penacho = Papagaio();
    penacho.nome = 'Penacho'
    print('penacho.nome:', penacho.nome)

    # Como Python é sensível ao caixa, isto é possível (e útil para dar clareza)
    papagaio = Papagaio();
    papagaio.nome = 'Godofredo'    
    print('papagaio.nome:', papagaio.nome)

    # Então são considerados distintos
    print('louro == penacho?', louro == penacho)
    print('louro == papagaio?', louro == papagaio)
    print('papagaio == penacho?', papagaio == penacho)

    # Um objeto pode ser atribuído à outra variável
    outroLouro = louro
    # Com isso, duas variáveis fazem referência ao mesmo objeto
    print('louro == outroLouro?', louro == outroLouro)
