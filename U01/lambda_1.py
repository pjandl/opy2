if __name__ == '__main__':
    print('Lambdas 1\n')

    # Definição de função para calcular o triplo de um valor
    def triplo(v):
        resultado = 3 * v
        return resultado

    # Uso da função
    print('triplo de 3:', triplo(3))
    print('triplo de X:', triplo('X'))

    # Redução da função, com retorno direto do resultado do cálculo
    def triplo(v):
        return 3 * v

    # Uso da função (como antes)
    print('triplo de 3:', triplo(3))
    print('triplo de X:', triplo('X'))

    # Definição da função em uma linha
    def triplo(v): return 3 * v

    # Uso da função (não muda)
    print('triplo de 11:', triplo(11))
    print('triplo de Rs:', triplo('Rs'))

    # Expressão lambda define função in-line, i.e., no local de uso
    triplo = lambda x : 3 * x

    # Uso é o mesmo (independe da definição típica ou como lambda)
    print(triplo(123))
    print(triplo('\o/'))
