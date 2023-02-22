from random import randint
vitoria = rodada = 0
while True:
    rodada += 1
    print('---'*15)
    numero = int(input(f'{rodada}.Escolha um número para o par ou ímpar: '))
    escolha = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    computador = randint(0, 10)
    resultado = numero + computador
    print('---' * 15)
    print(f'Você jogou {numero}\no computador jogou {computador}\no resultado é {resultado}')
    if escolha == 'P':
        resultado %= 2
        if resultado == 0:
            print('Deu par, você ganhou.')
            vitoria += 1
        else:
            print('Deu ímpar, você perdeu.')
            break
    if escolha == 'I':
        resultado %= 2
        if resultado != 0:
            print('Deu ímpar, você ganhou.')
            vitoria += 1
        else:
            print('Deu par, você perdeu.')
            break
print('---'*15)
print(f'Você venceu {vitoria} vez(es).')