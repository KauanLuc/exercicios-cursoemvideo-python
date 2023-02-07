nota1 = float(input('PRIMERA NOTA: '))
nota2 = float(input('SEGUNDA NOTA: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('passou de ano, sua media foi {:.1f}'.format(media))

elif media >= 5:
    print('recuperação, sua media foi {:.1f}'.format(media))

elif media < 5:
    print('reprovou, sua media foi {:.1f}'.format(media))