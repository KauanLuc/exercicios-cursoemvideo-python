from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os cincos valores sorteados foram ', end='')
for numero in tupla:
    print(f'{numero}', end=' ')
print(f'\nO maior valor é: {max(tupla)}')
print(f'O menor valor é: {min(tupla)}')
