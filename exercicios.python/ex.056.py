soma_idade = 0
media_idade = 0
maior_idade_homem = 0
homem_mais_velho = ''
total_mulher_20 = 0
for p in range(1, 5):
    print(f'------ {p}ª PESSOA ------')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    soma_idade += idade
    if p == 1 and sexo in 'M':
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo in 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo in 'F' and idade < 20:
        total_mulher_20 += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade:.0f} anos. ')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {homem_mais_velho}.')
print(f'Ao todo são {total_mulher_20} mulher(es) com menos de vinte anos.')