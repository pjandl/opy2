class DaClasse:
    classe_publico = 'Comum'
    __classe_privado = 'Privado'
    
    def __init__(self, nome):
        # define variável de instância pública
        self.nome = nome
        
    def get_classe_privado():
        return DaClasse.__classe_privado
    get_class_privado = staticmethod(get_classe_privado)

    @staticmethod
    def set_classe_privado(valor):
        if (valor > DaClasse.__classe_privado):
            DaClasse.__classe_privado = valor

    def __str__(self):
        aux = f'{self.nome}[classe_publico={DaClasse.classe_publico},' \
        + f'classe_privado={DaClasse.__classe_privado}]'
        return aux
