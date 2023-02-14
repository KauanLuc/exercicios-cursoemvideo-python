import random
xablau = random.randint(0, 10)
tentativas = 0

print('''Sou a Xablau, sua assistente virtual...
Vamos brincar?
Estou pensando em um número entre 0 e 10.
Você consegue advinhar?''')
print('-=-'*13)

palpite = int(input('Qual é o seu palpite? '))
tentativas += 1

while palpite != xablau:

    palpite = int(input('Qual é o seu palpite? '))
    tentativas +=1

print(f'CERTO! Com {tentativas} tentativas você acertou.')
