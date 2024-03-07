'''rograma para verificar o numero positivo ou negativo

Etapa 1 - Iniciar
Etapa 2 - Ler numero
Etapa 3 - Se (numero>0)
Etapa 4 - True imprimir o numero e positivo
Etapa 5 - False imprimir o numero e negativo
Etapa 6 - Fim

'''

#Entrada de dados
numero = float(input("Informe um numero: "))

#Verificacao se o numero e positivo, negativo ou zero
if numero > 0:
    print("O numero e positivo.")
elif numero < 0:
    print("O numero e negativo")
else:
    print("O numero e zero.")