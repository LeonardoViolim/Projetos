#Converter temperatura de Fahrenheit para Celsius

#Pseudocodigo
#Etapa 1 - Iniciar
#Etapa 2 - Receber valor de Fahrenheit
#Etapa 4 - Calcular(C=5/9*(F-32))
#Etapa 5 - Exibir Celsius
#Etapa 6 - Fim


#Solicite ao usuário que insira a temperatura em graus Fahrenheit
print("Olá. seja bem vindo ao conversor de temperaturas")
Temp_F = float(input("Qual o valor em Fahrenheit que gostaria de converter? "))

#Converta a temperatura de Fahrenheit para Celsius
Temp_C = 1.8*(Temp_F-32)

#Exiba a temperatura em graus Celsius na tela
print(f"A temperatura em Celsius é: {Temp_C:.2f} graus Celsius")