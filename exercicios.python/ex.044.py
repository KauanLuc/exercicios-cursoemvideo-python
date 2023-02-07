novo_valor = []


preco_produto = float(input('Informe o valor do produto: R$'))


print('[1] DINHEIRO/CHEQUE\n[2] À vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')


forma_de_pagamento = int(input('SELECIONE A FORMA DE PAGAMENTO: '))


if forma_de_pagamento == 1:
    novo_valor = preco_produto - (preco_produto * 10 / 100)
    print(f'Sua compra, anteriormente R${preco_produto:.2f}, agora com 10% de desconto, sai por R${novo_valor:.2f}')


elif forma_de_pagamento == 2:
    novo_valor = preco_produto - (preco_produto * 5/ 100)
    print(f'Sua compra, anteriormente R${preco_produto:.2f}, agora com 5% de desconto, sai por R${novo_valor:.2f}')


elif forma_de_pagamento == 3:
    em_2x = preco_produto / 2
    print(f'Sua compra em 2x no cartão sai por R${preco_produto:.2f}, R${em_2x:.2f} por mês')


elif forma_de_pagamento == 4:
    juros = preco_produto + (preco_produto * 20 / 100)
    parcelas = int(input('Em quanto será parcelada a sua compra? '))
    total = juros / parcelas
    print(f'Sua compra em {parcelas}x no cartão, com 20% de juros, sai por R${juros:.2f}. R${total:.2f} ao mês.')


else:
    print('Opcão inválida. Tente novamente.')

