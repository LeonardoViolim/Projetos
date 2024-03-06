'''Identifique o erro no programa e corrija-o. Alem disso, demonstre a saída esperada quando o programa estiver corrigido.

#Solicita ao usuário para inserir três números
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
numero3 = input("Digite o terceiro número: ")

#Calcula a média dos três números
media = (numero1 + numero2 + numero3)/3

#Exiba a média
print("A média é: " + media)

#Erro: TypeError: unsupported operand type(s) for /: 'str' and 'int'
'''

#Esta acontecendo um erro pelas informacoes recebidas estarem sendo tratadas como str ao inves de inteiro para realizar a conta.
#Se nao for alterar o codigo. Podemos apenas trasnformar o tipo de dados antes do calculo e consertar a exibicao do resultado.

#Solicita ao usuário para inserir três números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

#Calcula a média dos três números
media = (numero1 + numero2 + numero3)/3

#Exiba a média
print("A média é: " , media)