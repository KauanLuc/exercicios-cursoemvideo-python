print('-=-=-=-= FIBONACCI =-=-=-=-')
numero = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
contador = 3
print(f'{termo1} ->{termo2} ', end='->')
while contador <= numero:
    termo3 = termo1 + termo2
    print(f'{termo3} ->' , end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(' FIM')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')