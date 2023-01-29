quilometros = float(input('Qual a distâcia da viagem em Quilômetros(km)?: '))
viagemcurta = quilometros*0.50
viagemlonga = quilometros*0.45
if quilometros <=200:
    print('A sua taxa é de R${:.2f}'.format(viagemcurta))
else:
    print('A sua taxa é de R${:.2f}'.format(viagemlonga))


