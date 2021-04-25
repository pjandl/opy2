# Abertura de arquivo em modo w (escrita), arquivo não precisa existir
arquivo2 = open("arquivos/opy2-contagem.txt", "w")
print(arquivo2)

# write grava/escreve (qualquer) conteúdo no arquivo.
arquivo2.write("Contagem progressiva\n")

# Escrita de texto pode incluir quebras de linha e outros caracteres especiais
arquivo2.write("---- INÍCIO ----\n")

# uso de laço para inclusão sistematizada de conteúdo
for c in range(50): 
    # Escrita da contagem
    arquivo2.write(str(c) + '\n')

# Finalização do conteúdo
arquivo2.write("----- FIM ------\n")

# Fechamento do arquivo
arquivo2.close()
print('Arquivo fechado')
