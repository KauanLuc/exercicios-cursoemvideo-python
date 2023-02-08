numero = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\33[34m',end=' ')
        total += 1
    else:
        print('\33[31m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\33[mO número {numero} foi divisivel {total} vezes')
if total == 2:
    print(f'{numero} É primo ')
else:
    print(f'{numero} Não é primo')