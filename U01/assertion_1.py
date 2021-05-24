# Asserção que verifica o valor de uma variável.
# Execute para qualquer caso VÁLIDO (a != 0)
print('Execute esse programa duas vezes:' \
      '\n\t(1) para um valor DIFERENTE de zero' \
      '\n\t(2) para um valor IGUAL a zero'

a = int(input('Digite um valor inteiro: '))
assert a != 0
print(f'a = {a} e 1/{a} = {1/a}')
