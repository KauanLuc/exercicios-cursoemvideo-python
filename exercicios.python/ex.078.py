numero =[int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: '))]
print(f'Você selecionou os valores {numero}')
print(f'O maior valor digitado foi {max(numero)}, nas posições ', end='')
for i, v in enumerate(numero):
    if v == max(numero):
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min(numero)}, nas posições ', end='')
for i, v in enumerate(numero):
    if v == min(numero):
        print(f'{i}...', end='')


