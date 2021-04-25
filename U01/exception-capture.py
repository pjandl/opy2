# Função SEM controle de erros
def dividir(a, b):
    return a / b


if __name__ == '__main__':
    print('Leitura de valor para divisão.\nExperimente digitar:')
    print('\t- uma string (provocará ValueError)')
    print('\t- zero (ZeroDivisionError)')
    print('\t- um valor inteiro ou real qualquer (resultado é exibido).')
    
    try:
        x = float(input('Digite um número: '))
        resultado = dividir(1, x)
    # Captura da exceção para uso de suas informações
    except Exception as exc:
        print('Tipo:', type(exc))
        print('Mensagem:', exc)
    else:
        print(f'1/{x} = {resultado}')
