homens = maioridade = mulher = 0
while True:
    print('-----CADASTRE UMA PESSOA-----')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-----------------------------')
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
       homens += 1
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('===== FIM DOS CADASTROS =====')
print(f'Temos {maioridade} pessoas com mais de 18 anos.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'Temos {mulher} mulheres com menos de 20 anos.')
print('=============================')