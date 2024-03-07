'''Programa para verificar se o numero e par ou impar

Etapa 1 - Iniciar
Etapa 2 - Ler n
Etapa 3 - Se (n == 0)
Etapa 4 - True imprimir o numero e zero
Etapa 5 - False se (n > 0)
Etapa 6 -   True Imprima e positivo
Etapa 7 -   False Imprima e negativo
Etapa 8 - Fim

'''

#Solicitar um número
numero = float(input("Digite um número: "))

#Verificar se o número é positivo, negativo ou zero
if numero > 0:
    print("O número e positivo.")
elif numero < 0:
    print("O número e negativo.")
else:
    print("O número e zero.")