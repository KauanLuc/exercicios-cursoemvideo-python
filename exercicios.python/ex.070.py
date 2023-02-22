soma = caro = menor = contador = 0
barato = ''
while True:
    print('===== LOJAS KAUAN LINDO =====')
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    contador += 1
    soma += preco
    if preco > 1000:
        caro += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
print('===== LOJAS KAUAN LINDO =====')
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {caro} produto(s) custando mais de R$1.000')
print(f'O produto mais barato é {barato} seu preço é R${menor:.2f}')