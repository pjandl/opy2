import random as rnd

# Abertura de arquivo em modo a (anexacao), arquivo não precisa existir
arquivo2 = open("opy2-contagem.txt", "a")

# write grava/escreve (qualquer) conteúdo no arquivo.
arquivo2.write("-- CONTINUACAO -\n")

# Uma lista de linguagens de programação
lp = ['Python', 'Java', 'C', 'C++', 'C#', 'Scala', 'Pascal', 'Modula', 'Fortran', 
      'PHP', 'JavaScript', 'Visual Basic', 'Prolog', 'Lisp', 'Pascal', 'Haskell']
# Gravar uma lista requer sua transformação em texto
arquivo2.write(str(lp))
# Lembre-se das quebras de linha
arquivo2.write('\n\n')

# uso de laço para inclusão sistematizada de conteúdo
for i in range(10):
    arquivo2.write(lp[rnd.randrange(0, len(lp))])
    arquivo2.write('\n')
    
# Finalização do conteúdo
arquivo2.write("\n--- NOVO FIM ----\n")

# Fechamento do arquivo
arquivo2.close()
print('Arquivo fechado')
