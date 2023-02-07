reta1 = float(input('Primeira reta: '))
reta2 = float(input('Sgunda reta: '))
reta3 = float(input('Terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas formam um triângulo', end='')
    if reta1 == reta2 == reta3:
        print(' EQUILÁTERO')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('As retas não formam um triângulo.')