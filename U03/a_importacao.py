import Papagaio as ppg

# Programa principal
if __name__ == '__main__':
    # Instancia objeto Papagaio
    umPapagaio = ppg.Papagaio()

    # Obtém e imprime atributo do objeto
    print('umPapagaio.nome:', umPapagaio.nome)

    # Altera nome
    umPapagaio.nome = 'Heraldo'

    # Obtém e imprime atributo do objeto
    print('umPapagaio.nome:', umPapagaio.nome)

    # Usa métodos
    umPapagaio.meu_nome()
    umPapagaio.minha_idade()
    umPapagaio.fala('tá se achando!')
