from time import sleep
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
opcao= 0
while opcao != 8:
    print('''    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Maior
    [5] Novos Valores
    [6] Dividir
    [7] Porcentagem
    [8] Sair do Programa''')
    opcao = int(input('Qual é a sua opção? '))
    print('>>>'*15)
    if opcao == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma de {primeiro_valor} e {segundo_valor} é igual a {soma}')
    elif opcao == 3:
        multiplicado = primeiro_valor * segundo_valor
        print(f'A multiplicação de {primeiro_valor} e {segundo_valor} é igual a {multiplicado}')
    elif opcao == 4:
        if primeiro_valor > segundo_valor:
            print(f'{primeiro_valor} é maior que {segundo_valor}')
        elif segundo_valor > primeiro_valor:
            print(f'{segundo_valor} é maior que {primeiro_valor}')
        else:
            print(f'Os valores {primeiro_valor} e {segundo_valor} são iguais.')
    elif opcao == 5:
        print('Informe os números novamente.')
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
    elif opcao == 6:
        divisao = primeiro_valor / segundo_valor
        print(f'A divisão de {primeiro_valor} e {segundo_valor} é igual a {divisao:.2f}')
    elif opcao == 8:
           print('processando...')
    elif opcao == 7:
        porcentagem = primeiro_valor * segundo_valor / 100
        print(f'{primeiro_valor}% de {segundo_valor} é igual a {porcentagem}')
    elif opcao == 2:
        subtrair = primeiro_valor - segundo_valor
        print(f'A subtração de {primeiro_valor} por {segundo_valor} é igual a {subtrair} ')
    else:
        print('Opção invalida. Tente novamente.')
    print('>>>'*15)
    sleep(2)

print('Fim, volte sempre.')