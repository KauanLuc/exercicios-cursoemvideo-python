parada = 999
numero = contador = soma = 0

numero = int(input('Digite um número [999 para parar]: '))
while numero != parada:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'A soma dos {contador} números é igual a {soma}')