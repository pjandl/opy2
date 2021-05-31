if __name__== '__main__':
    print('OPY2/L1/Exercício 1')
    ini = int(input('Digite inteiro inicial (ini): '))
    fim = int(input('Digite inteiro final (fim): '))

    print('Lista SEM comprehension')
    lista_sem_comprehension = []
    for n in range(ini, fim+1):
        if n % 2 == 1:
            lista_sem_comprehension.append(n)
    print('lista_sem_comprehension:', lista_sem_comprehension)
    
    print('Lista COM comprehension')
    lista_com_comprehension = [n for n in range(ini, fim+1) if n % 2 == 1]
    print('lista_sem_comprehension:', lista_sem_comprehension)

