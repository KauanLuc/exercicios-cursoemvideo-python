primeiro_termo = int(input('Digite o primeiro termo de uma razão: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
print('FIM')
