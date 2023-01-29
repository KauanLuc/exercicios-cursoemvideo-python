velocidade = float(input('Qual a velocidade do carro atualmente?: '))
multa = (velocidade - 80) * 7
pontosnacarteira = (velocidade - 80) * 0.1
if velocidade >80:
    print('MULTADO! Você terá que pagar R${:.2f} a o DETRAN.\nVocê também perdeu {:.0f} pontos na carteira.'.format(multa,pontosnacarteira))
else:
    print('Tenha um bom dia, siga bem caminhoneiro.')