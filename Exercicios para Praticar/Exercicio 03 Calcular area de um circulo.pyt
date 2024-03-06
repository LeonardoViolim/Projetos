#Calculando area de Circulo

#Solucao 1
#Etapa 1 - Iniciar
#Etapa 2 - Receber valor de raio
#Etapa 4 - Calcular(Area = PI*r^2)
#Etapa 5 - Exibir area
#Etapa 6 - Fim

#Solicite ao usuário que insira o valor do raio do círculo
raio = float(input("Informe o valor do raio da circunferência: "))

#Calcule a área do círculo
area = 3.14159*raio*raio

#Exiba a área do círculo na tela
print(area)

#Utilizando a funcao math
import math

area2 = math.pi * raio ** 2
print(math.pi)

#Limitando numero de casas após a vírgula na resposta
print(f"A area da circunferencia e {area2:.2f}")
