import random
from emoji import emojize

print(emojize(':space_invader:',language='alias')*40)

numerosorteado = random.randint(0,5)

chute = int(input('Tente advinhar o número de 0 a 5, na qual o computador esta pensando: '))

if chute == numerosorteado:
    print('Parabéns!!! Você venceu. O número correto realmente é {}'.format(numerosorteado))

else:
    print('Xiii... você perdeu. O número correto era {}.'.format(numerosorteado))

print(emojize(':space_invader:',language='alias')*40)