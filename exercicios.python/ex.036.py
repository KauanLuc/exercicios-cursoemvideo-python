valorcasa = float(input('Qual é o valor a ser pago pela casa? Digite aqui: R$'))
salario = float(input('Qual o salário do comprador? Digite aqui: R$'))
anos = int(input('Quantos anos de financiamento? Digite aqui: R$'))
prestacao = valorcasa / (anos * 12)
porcentagemmaxima = salario * 30 / 100
print()

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação sera de: R${:.2f}'.format(valorcasa,anos,prestacao))
if prestacao <= porcentagemmaxima:
    print('Parabéns, o empréstimo foi aceito com sucesso.')
else:
    print('Infelizmente seu empréstimo foi negado.')






print()

