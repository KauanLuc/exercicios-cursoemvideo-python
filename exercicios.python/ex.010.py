real = float(input(' saldo da conta em real (R$):'))
doloar = real / 5.11
euro = real / 5.50
print('{} reais compram {:.2f} dolares e {:.2f} euros.'.format(real,doloar,euro))