primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
#DESCOBRINDO O MENOR
if primeiro<segundo and primeiro<terceiro:
    menor=primeiro
if segundo<primeiro and segundo<terceiro:
    menor=segundo
if terceiro<primeiro and terceiro<segundo:
    menor=terceiro
    print('O menor valor é igual a {}'.format(menor))
#DESCOBRINDO O MAIOR
if primeiro>segundo and primeiro>terceiro:
    maior=primeiro
if segundo>primeiro and segundo>terceiro:
    maior=segundo
if terceiro>primeiro and terceiro>segundo:
        maior=terceiro
print('O maior valor é igual {}'.format(maior))