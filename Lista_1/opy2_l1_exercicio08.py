def soma_quadrados(lista):
    '''Função que retorna a soma dos quadrados dos elementos da lista'''
    # Verifica se lista vazia
    if len(lista) == 0:
        raise ValueError('lista vazia')
    # Calcula soma dos quadrados
    soma = 0
    for e in lista:
        try:
            soma += e**2
        except:
            # Elemento na lista não é numérico
            raise TypeError(f"'{e}' não é valor numérico.")
    # Retorna soma dos resultados        
    return soma

def teste(nome, lista):            
    print(nome, '\nLista:', lista)
    try:
        print('Soma dos quadrados:', soma_quadrados(lista))
    except Exception as exc:
        print('Exceção: ', exc)
    print(40*'-')

if __name__ == '__main__':
    # lista vazia
    teste('Teste::lista vazia', [])

    # lista com elementos inválidos
    teste('Teste::lista com elementos inválidos', [1, 2.3, '4'])

    # lista com elementos válidos
    teste('Teste::lista com elementos inválidos', [1, 2.3, 4.5, 6])
