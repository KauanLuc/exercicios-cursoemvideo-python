while True:
    numero = int(input('Digite um número para ter sua tabuada: '))
    if numero < 0:
        break
    for multiplicador in range(1, 11):
        print(f'{numero} X {multiplicador} = {numero*multiplicador}')
print('Fim')
