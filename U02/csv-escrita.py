import math

# Exemplo do uso de with na escrita de um arquivo CSV
with open('tabela.csv', 'wt') as f:
    # gravação do cabeçalho (opcional) do arquivo CSV
    f.write('#;angulo;seno;cosseno\n')
    i = 1
    for e in range(0, 51, 5):
        a = math.pi * e / 100
        # os valores de cada registro (linha) são separados por ;
        f.write(f'{i};{a:.3f};{math.sin(a):.6f};{math.cos(a):.6f}\n')
        i += 1
