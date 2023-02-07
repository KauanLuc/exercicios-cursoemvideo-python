from datetime import datetime
dataAtual = datetime.today().year
nascimento = int(input('ano de nascimento: '))
idade = dataAtual - nascimento

print('O atleta tem {} anos em {} e nasceu em {}'.format(idade,dataAtual,nascimento))

if idade <= 9:
    print('MIRIM')

elif idade >9 and idade <=14:
    print('INFANTIL')

elif idade >14 and idade <=19:
    print('JÚNIOR')

elif idade >=19 and idade <=25:
    print('SÉNIOR')

else:
    print('MASTER')