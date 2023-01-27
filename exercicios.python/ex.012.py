preco = float(input('valor do produto em R$:'))
comdesconto = preco - (preco*5/100)
print('o preço do produto, agora atualizado com desconto, é {:.2f}.'.format(comdesconto))