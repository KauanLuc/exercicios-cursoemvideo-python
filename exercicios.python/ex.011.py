largura = float(input(' digite a largura da parede:'))
altura = float(input('digite a altura da parede:'))
area =  largura * altura
tinta = area / 2
print('sua parede tem a dimensao de {}x{} e sua area é de {}m2. Para pintar a parede voce precisara de {}L de tinta'.format(largura,altura,area,tinta))