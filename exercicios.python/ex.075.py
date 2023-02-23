n = []
numero = (int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')))
print(f'Você digitou os valores {numero}')
if 9 in numero:
    print(f'O valor 9 aparece {numero.count(9)} vez(es)')
else:
    print('Não tem 9.')
if 3 in numero:
    print('O valor 3 aparece na posição: ', numero.index(3)+1)
else:
    print('Não tem 3.')
print('Os valores pares são: ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')



