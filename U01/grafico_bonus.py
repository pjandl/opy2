import matplotlib as mpl
import matplotlib.pyplot as plt

# Pode ser aplicado um condicional para filtrar os elementos do for
polinomio = lambda x : -1.5*x**2 + 3.7*x + 4.5
x = [v/10 for v in range(-50, 101, 5)]
print('x\n', x)
y = [polinomio(v) for v in x]
print('y\n', y)

# O método plot() autodefine as escalas dos eixos do gráfico
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polinômio')
plt.scatter(x, y, color = 'r', marker = 'o', s = 10)
plt.show()
