# Função SEM controle de erros
def dividir(a, b):
    return a / b


if __name__ == '__main__':
    print('Leitura de valor para divisão.\nExperimente digitar:')
    print('\t- uma string (provocará ValueError)')
    print('\t- zero (ZeroDivisionError)')
    print('\t- um valor inteiro ou real qualquer (resultado é exibido).')
    
    # Podem existir duas ou mais cláusulas except no try, que pode ser
    # qualificadas para apanhar um exceção específica.
    try:
        x = int(input('Digite um número: '))
        resultado = dividir(1, x)
    except ZeroDivisionError as zde:
        print('Mensagem:', zde)
        print('Verifique o número fornecido. Não é possível dividir por zero!')
    except ValueError as ve:
        print('Mensagem:', ve)
        print('Deve ser fornecido um número inteiro ou real válido.')
    except Exception as exc:
        print('Opa! Aconteceu um erro imprevisto:')
        print(type(exc))
    else:
        print(f'1/{x} = {resultado}')
