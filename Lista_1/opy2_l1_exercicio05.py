# Importação da função reduce do módulo functools
from functools import reduce

def totalizar(x, y):
    return (0, x[1] + y[1], x[2] + y[2], x[3] + y[3])

def calc_media(tupla):
    '''Recebe tupla (RA,P1,P2) e produz tupla (RA,P1,P2,Média)'''
    ra, p1, p2 = tupla
    return (ra, p1, p2, (p1 + p2) / 2)

if __name__ == '__main__':
    # Entrada de dados
    print('Dados dos Alunos')
    alunos = []
    resp = 'S'
    while resp.upper() == 'S':
        RA = input('RA? ')
        try:
            P1 = float(input('P1? '))
            P2 = float(input('P2? '))
            alunos.append((RA, P1, P2))
            resp = input('Outro aluno [S|N]? ')
        except:
            # quando ocorre erro, repete entrada
            resp = 'S'
    print(alunos)

    # Mapeamento
    print('Médias Individuais dos Alunos')
    # map aplica função calc_media aos elementos da lista alunos
    resultados = list(map(calc_media, alunos))
    print(resultados)

    # Redução
    print('Médias Gerais dos Alunos')
    # reduce aplica função totalizar aos elementos da lista resultados
    totais = reduce(totalizar, resultados)
    rotulos = ['P1', 'P2', 'Média']
    for i in range(len(rotulos)):
        print(f'Média {rotulos[i]} = {totais[i+1]/len(resultados):.3f}')
