import struct

nome_arquivo = 'red.png'
i = 0
with open(nome_arquivo, 'rb') as f:
    byte = f.read(1)
    while byte:
        i += 1
        #
        print(f'{byte.hex().upper():2s}', end=' ')
        if i == 16:
            print()
            i = 0
        byte = f.read(1)

i = 0
with open(nome_arquivo, 'rb') as f:
    signature = f.read(8)
    if signature.hex() == '89504e470d0a1a0a':
        print('PNG')
        f.read(8) # descarta chunck type (IHDR)
        data = f.read(8)
        w, h = struct.unpack('>LL', data)
        print(f'width x height = {int(w)} x {int(h)}')
    else:
        print('Arquivo não contém imagem PNG.')

