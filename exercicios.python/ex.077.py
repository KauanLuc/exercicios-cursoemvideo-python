palavras = ('Alvissaras',
'Balaustre',
'Beneplacito',
'Cornucopia',
'Cuntatorio',
'Deleterio',
'Desasnado')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')