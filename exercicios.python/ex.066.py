numero = contador = soma = 0

while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'A soma dos {contador} números foi {soma}!')