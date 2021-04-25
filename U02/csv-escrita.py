import math

# Exemplo do uso de with na escrita de um arquivo CSV
with open('arquivos/tabela.csv', 'wt') as f:
    print(f)
    # gravação do cabeçalho (opcional) do arquivo CSV
    f.write('#;angulo;seno;cosseno\n')
    i = 1
    for e in range(0, 51, 5):
        a = math.pi * e / 100
        # os valores de cada registro (linha) são separados por ;
        linha = f'{i};{a:.3f};{math.sin(a):.6f};{math.cos(a):.6f}'
        f.write(linha)
        f.write('\n')
        print(linha)
        i += 1
