import random
print('digite o nome dos alunos.')
aluno1 = str(input('digite o nome do primeiro aluno: '))
aluno2 = str(input('digite o nome do segundo aluno: '))
aluno3 = str(input('digite o nome do terceiro aluno: '))
aluno4 = str(input('digite o nome do quarto aluno: '))
lista = [aluno1,aluno2,aluno3,aluno4]
sorteado = random.choice(lista)
print('o sorteado foi {}.'.format(sorteado))
