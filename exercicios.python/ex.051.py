contador = 0
primeiro_termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{c}', end='-> ')
print('CABOU')


