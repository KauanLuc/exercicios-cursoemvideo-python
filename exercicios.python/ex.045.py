from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0, 2)

print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogada = int(input('Faça sua jogada: '))

print(f'Computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogada]}')

if computador == 0:
    if jogada == 0:
        print('Deu empate')
    elif jogada == 1:
        print('jogador ganhou')
    else:
        print('computador ganhou')

elif computador == 1:
    if jogada == 1:
        print('deu empate')
    elif jogada == 0:
        print('computador ganhou')
    else:
        print('jogador ganhou')

elif computador == 2:
    if jogada == 2:
        print('deu em empate')
    elif jogada == 1:
        print('computador ganhou')
    else:
        print('jogador ganhou')


