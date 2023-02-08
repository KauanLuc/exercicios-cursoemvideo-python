from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for pessoas in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoas}ª pessoa nasceu? '))
    idade = atual - nascimento

    if idade >= 21:
        totalmaior += 1

    else:
        totalmenor += 1

print(f'Ao todo tivemos {totalmaior} pessoas maior(es) de idade e, {totalmenor} menor(es) de idade')

