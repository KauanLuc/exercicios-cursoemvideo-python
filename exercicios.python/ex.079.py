valor = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in valor:
        valor.append(numero)
    else:
        print('Valor já existente. Não adicionado.')
    pergunta = str(input('Você deseja continuar? [S/N]: ')).lower().strip()[0]
    while pergunta not in 'sn':
        pergunta = str(input('Você deseja continuar? [S/N]: ')).lower().strip()[0]
    if pergunta == 'n':
        break
valor.sort()
print(f'Os valores digitados foram {valor}')