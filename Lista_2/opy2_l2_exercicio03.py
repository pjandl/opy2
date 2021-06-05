if __name__ == '__main__':
    print('Escrita de Arquivo HTML')
    nome = input('Nome completo? ')
    idade = int(input('Idade (anos completos)? '))
    cidade = input('Cidade natal? ')
    estado = input('Estado natal? ')

    # Abertura do arquivo para escrita
    arquivo = open(nome + '.html', 'w')

    # Escrita do conteúdo
    arquivo.write('<HTML>\n<HEAD>\n')
    arquivo.write(f'\t<TITLE>{nome}</TITLE>\n')
    arquivo.write('</HEAD>\n<BODY>\n')
    arquivo.write('\t<TABLE border="1">\n')
    arquivo.write(f'\t\t<TR><TD>NOME</TD><TD>{nome}</TD></TR>\n')
    arquivo.write(f'\t\t<TR><TD>IDADE</TD><TD>{idade}</TD></TR>\n')
    arquivo.write('\t\t<TR><TD>CIDADE</TD>')
    arquivo.write(f'<TD>{cidade} - {estado.upper()}</TD></TR>\n')
    arquivo.write('\t</TABLE>\n')
    arquivo.write('</BODY>\n</HTML>\n')

    # Fechamento do arquivo
    arquivo.close()
