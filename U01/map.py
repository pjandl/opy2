import math

# Dada a definição da função que segue
def volume(raio):
    volumeEsfera = (4 / 3) * math.pi * raio**3
    return volumeEsfera


if __name__ == '__main__':
    print('Map\n')

    # Lista de medidas de raios de várias esferas
    raio = [1.6, 2.8, 6.5, 1.0, 3.7]

    # Mapeamento: aplica função volume(raio) aos elementos da lista raio
    # e retorna um iterator
    print(map(volume, raio))

    # Mapeamento: transformação do iterator em uma lista
    print(list(map(volume, raio)))

    # Atribuição da lista para outros usos
    volumes = list(map(volume, raio))

    # Laço de repetição for para exibir conteúdo da lista
    print(f'{"Raio":10s} | {"Volume":10s}')
    for i in range(len(volumes)):
        print(f'{raio[i]:10.3f} | {volumes[i]:10.3f}')
    print()
    
    # Consideremos agora duas listas (com tamanhos diferentes)
    listaA = [23, 54, 4, 35, 49, 19]
    listaB = [63, 16, 6, 28, 19, 30, 99]
    print('listaA:\n', listaA)
    print('listaB:\n', listaB)
    print()
    
    # Os elementos destas listas podem ser somados gerando uma nova lista
    listaC = list(map(lambda x,y : x + y, listaA, listaB))
    print('listaC = listaA + listaB:\n', listaC)

    # Soma dos elementos das listas indicadas em ordem diferente
    listaC = list(map(lambda x,y : x + y, listaB, listaA))
    print('listaC = listaB + listaA:\n', listaC)
