soma = 0
contador = 0

for numero in range(1, 501, 2):

    if numero % 3 == 0:
        contador += 1
        soma += numero

print(f'A soma dos {contador} números resultam em {soma}')