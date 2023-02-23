precos = ('Monitor', 1.525, 'Processador', 959, 'Cooler', 20, 'Teclado', 204,
          'Mesa Digitalizadora', 280)
print('='*60)
print(f'{"LISTAGEM DE PREÇOS":^60} ')
print('='*60)
for posicao in range(0, len(precos)):
    if posicao % 2 == 0:
        print(f'{precos[posicao]:.<30}', end='')
    else:
        print(f'R${precos[posicao]:<10}')
print('='*60)

