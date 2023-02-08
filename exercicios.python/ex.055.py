maior_peso = 0
menor_peso = 0

for peso in range(1, 6):
    quilos = float(input(f'Peso da {peso}ª pessoa: '))
    if peso == 1:
        maior_peso = quilos
        menor_peso = quilos
    else:
        if quilos > maior_peso:
            maior_peso = quilos
            if quilos < menor_peso:
                menor_peso = quilos

print(f'''Analisando os pesos, o maior foi de {maior_peso}
E o menor foi de {menor_peso}''')