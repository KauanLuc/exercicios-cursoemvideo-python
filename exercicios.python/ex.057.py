homem = 'M'
mulher = 'F'

sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]

if sexo == homem or sexo == mulher:
    print('SUCESSO')
else:
    while sexo != homem or sexo != mulher:
        sexo = str(input('Opção invalida. Tente novamente:')).upper().strip()[0]
        if sexo == homem or sexo == mulher:
            print('AGORA, SIM. SUCESSO.')
            break
