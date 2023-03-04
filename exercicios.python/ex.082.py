numero = []
par = []
impar = []
while True:
    numero.append(int(input('Digite um valor: ')))
    pergunta = str(input('Você deseja continuar? [S/N]: ')).lower().strip()[0]
    while pergunta not in 'sn':
        pergunta = str(input('Você deseja continuar? [S/N]: ')).lower().strip()[0]
    if pergunta == 'n':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é {numero}')
print(f'Os pares são {par}')
print(f'Os impares são {impar}')