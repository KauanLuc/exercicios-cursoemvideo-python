numero = int(input('Digite um número inteiro: '))
print('ESCOLHA A CONVERSÃO:\n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL')
opcao = int(input('SUA OPÇÃO: '))

if opcao == 1:
    print('O número {} convertido em binário é {}'.format(numero, bin(numero)[2:]))

elif opcao == 2:
    print('O número {} convertido em octal é {}'.format(numero, oct(numero)[2:]))

elif opcao == 3:
    print('O número {} convertido em hexadecimal é {}'.format(numero, hex(numero)[2:]))

else:
    print('Opção inválida ou não encontrada. TENTE NOVAMENTE.')