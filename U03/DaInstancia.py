class DaInstancia:
    def __init__(self, nome, a):
        # define variáveis de instância públicas
        self.nome = nome
        self.valor_publico = a
        # define variável de instância privada
        self.__valor_privado = 1

    def set_valor_privado(self, valor):
        if (valor > self.__valor_privado):
            self.__valor_privado = valor

    def __str__(self):
        aux = f'{self.nome}[valor_publico={self.valor_publico},' \
            + f'valor_privado={self.__valor_privado}]'
        return aux
