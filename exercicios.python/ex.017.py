catetoA = float(input('digite o valor do cateto oposto:'))
catetoB = float(input('digite o valor do cateto adjacente:'))
hipotenusa = (catetoA ** 2 + catetoB ** 2) ** (1/2)
print('a hipotenusa da soma dos quadrados dos catetos é: {:.2f}'.format(hipotenusa))