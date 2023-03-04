valor = []
elementos = 0 # len() pode ser usado de forma mais fácil.
while True:
    numero = int(input('Digite um valor: '))
    valor.append(numero)
    elementos += 1 # len() pode ser usado de forma mais fácil.
    pergunta = str(input('Você deseja continuar? [S/N]: ')).lower().strip()[0]
    while pergunta not in 'sn':
        pergunta = str(input('Você deseja continuar? [S/N]: ')).lower().strip()[0]
    if pergunta == 'n':
        break
valor.sort(reverse= True)
print('-==-'*30)
print(f'Você digitou {elementos} elementos.')
print(f'Os valores em ordem decrescente: {valor}')
if 5 in valor: print('Tem 5 na lista.')
else: print('5 não foi encontrado.')

