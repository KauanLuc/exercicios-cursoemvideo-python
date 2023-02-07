peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / (altura ** 2)
print('O seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print('você está abaixo do peso')

elif imc <= 25:
    print('você está no peso ideal.')

elif imc <= 30:
    print('você está acima do peso ideal.')

elif imc <= 40:
    print('você está com OBESIDADE.')

else:
    print('você está com OBESIDADE MÓRBIDA, se cuide.')


