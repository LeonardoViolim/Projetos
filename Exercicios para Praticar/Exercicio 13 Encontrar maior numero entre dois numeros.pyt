''' Programa para encontrar o maior numero entre dois numeros

Etapa 1 - Iniciar
Etapa 2 - Ler Num1, Num2
Etapa 3 - Se A > B
Etapa 4 - True exibir A, False exibir B
Etapa 6 - Fim

'''

#Solicite ao usuário que insira dois valores numericos
num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))

if num1 > num2:
    print(f"O numero {num1} e maior do que {num2}")
else:
    print(f"O numero {num2} e maior do que {num1}")


###Solucao alternativa
num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))

if num1 > num2:
    maior = num1
else:
    maior = num2

#Exibicao do resultado
print("O maior numero e: ", maior)