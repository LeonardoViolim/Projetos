''' Programa para trocar dois numeros sem usar uma variavel temporaria

Informe o valor a: 5
Informe o valor de b: 8
Depois da troca:
a = 8
b = 5

Etapa 1 - Iniciar
Etapa 2 - Ler Num1, Num2
Etapa 3 - Exibir Num1, Num2 antes da troca
Etapa 4 - (A = A + B)(B = A - B)(A = A - B)
Etapa 5 - Exibir A, B. Depois da troca
Etapa 6 - Fim

'''

#Trocar dois numero sem variavel temporaria
a = 5
b = 8

#Exibir numero antes da troca
print("a =", a)
print("b =", b)

#Primeiro somamos e armazenamos em A. Em seguida, subtraimos B de A e armazenamos o resustado em b.
#Por fim, subtraimos o novo valor de b em A para obter o valor original de A.
#Isso efetivamente trocara os valores de A e B sem uso de variavel temporaria.
a = a + b
b = a - b
a = a - b

#Exibir depois da troca
print("\nDepois da troca:")
print("a =", a)
print("b =", b)
