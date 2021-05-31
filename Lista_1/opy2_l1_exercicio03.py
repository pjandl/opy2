if __name__== '__main__':
    print('OPY2/L1/Exercício 2')
    a2 = float(input('Digite coeficiente real "a2": '))
    a1 = float(input('Digite coeficiente real "a1": '))
    a0 = float(input('Digite coeficiente real "a0": '))

    ini = float(input('Digite real inicial (ini): '))
    fim = float(input('Digite real final   (fim): '))

    # Função lambda
    f = lambda a2, a1, a0, x : a2 * x**2 + a1 * x + a0
    
    print('\nLista x -> (x,y) -> (x,y>0)')
    lista_xy_pos = [t
                    for t in [(x, round(f(a2, a1, a0, x), 2))
                             for x in [round(x * 0.1, 2)
                                      for x in range(int(10*ini), int(10*fim + 1), 1) ]]
                    if t[1] > 0]
    print(lista_xy_pos)
