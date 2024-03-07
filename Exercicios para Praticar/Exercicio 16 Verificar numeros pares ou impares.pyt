'''Programa para verificar se o numero e par ou impar

Etapa 1 - Iniciar
Etapa 2 - Ler numero
Etapa 3 - Se (numero%2==0)
Etapa 4 - True imprimir o numero e par
Etapa 5 - False imprimir o numero e impar
Etapa 6 - Fim

'''

#Entrada de dados
numero = int(input("Informe um número inteiro: "))

#Verificação se o número e par ou ímpar
if numero % 2 == 0:
    print("O número e par.")
else:
    print("O número e ímpar.")