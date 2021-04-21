# Uso de try-except para controlar erros na entrada de dados
try:
    # No try são colocadas as diretivas sujeitas à ocorrência de exceções
    valor = int(input('Digite um valor inteiro: '))
    # Se chegamos aqui, a entrada deu certo
    print(f'Valor fornecido ({valor}) em uso!')
except:
    # Aqui vai o tratamento do erro ou a orientação para o usuário
    valor = 1
    print('Entrada incorreta. Valor default 1 em uso!')

# Aqui o programa segue com a entrada correta ou com valor default
print('Valor =', valor)
