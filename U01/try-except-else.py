# Função SEM controle de erros
def dividir(a, b):
    return a / b


if __name__ == '__main__':
    # A diretiva try-except pode ser combinada com outras para
    # oferecer um controle mais efetivo dos problemas possíveis
    while True:
        try:
            # Aqui vão as diretivas sujeitas à ocorrência de exceções
            x = int(input('Digite um valor inteiro: '))
            y = int(input('Digite outro valor inteiro: '))
            # Se chegamos aqui, a entrada deu certo
            break
        except:
            # Aqui vai o tratamento do erro ou a orientação para o usuário
            print('Ops! Um dos valoes não é inteiro. Vamos tentar de novo!')

    # Variáveis x e y contêm inteiros
    print('x =', x, '\ny =', y)

    try:
        resultado = dividir(x, y)
    except:
        print(f'Erro na divisão de {x} por {y}.')
    else:
        print(f'A divisão de {x} por {y} resulta em {resultado}.')        

