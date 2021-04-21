if __name__ == '__main__':
    # A diretiva try-except pode ser combinada com outras para
    # oferecer um controle mais efetivo dos problemas possíveis
    while True:
        try:
            # Aqui vão as diretivas sujeitas à ocorrência de exceções
            x = int(input('Digite um valor inteiro: '))
            # Se chegamos aqui, a entrada deu certo
            break
        except:
            # Aqui vai o tratamento do erro ou a orientação para o usuário
            print('Ops! Não é um valor inteiro. Vamos tentar de novo!')

    # Variável x contém inteiro
    print('x =', x)

