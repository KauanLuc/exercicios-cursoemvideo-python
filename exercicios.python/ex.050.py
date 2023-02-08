soma = 0
contador = 0

for c in range(1, 7):
    numero = int(input(f'Digite um número inteiro: '))
    if numero % 2 == 0:
        
        soma += numero
        contador += 1
print(f'A soma dos {contador} números é {soma}')