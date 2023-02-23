zero_a_vinte = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while escolha <0 or escolha >20:
    escolha = int(input('Número não suportado. Digite um número entre 0 e 20: '))
print(zero_a_vinte[escolha])