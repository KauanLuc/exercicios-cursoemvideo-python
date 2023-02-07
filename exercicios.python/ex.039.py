from datetime import date
anoatual = date.today().year
nascimento = int(input('Qual seu ano de nascimento? '))
idade = anoatual - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,idade,anoatual))

if idade == 18:
    print('vc deve se aprensentar ao quartel')

elif
