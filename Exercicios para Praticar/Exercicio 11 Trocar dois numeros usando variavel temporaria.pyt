''' Programa para trocar dois numeros usando uma variavel temporaria

Com ajuda do fluxograma, crie um programa para trocar dois numeros usando uma variavel temporaria

Informe o valor num1: 5
Informe o valor de num2: 8
Depois da troca:
num1 = 8
num2 = 5

Etapa 1 - Iniciar
Etapa 2 - Ler Num1, Num2
Etapa 3 - Exibir Num1, Num2 antes da troca
Etapa 4 - Temp = num1, num1 = num2, num2 = temp
Etapa 5 - Exibir num1, num2 depois da troca
Etapa 6 - Fim

'''

#Solicite ao usuário que insira os valores
num1 = int(input("Informe o valor de num1: "))
num2 = int(input("Informe o valor de num2: "))

#Troca dos numeros usando uma variavel temporaria
temp = num1
num1 = num2
num2 = temp

#Exibicao do resultado
print("Depois da troca:")
print("num1 =", num1)
print("num2 =", num2)