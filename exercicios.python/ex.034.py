salario = float(input('Qual o salário do funcionário? '))
salarioalto = salario + (salario*10/100)
salariobaixo = salario + (salario*15/100)
if salario <= 1250:
    print('O novo salário do funcionário é {:.2f}'.format(salariobaixo))
else:
    print('O novo salário do funcionário é {:.2f}'.format(salarioalto))