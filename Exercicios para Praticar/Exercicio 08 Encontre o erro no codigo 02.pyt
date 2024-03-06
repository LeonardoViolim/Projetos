'''Identifique o erro no programa e corrija-o. Além disso, demonstre a saída esperada quando o programa estiver corrigido.

Programa para calcular a raiz quadrada de um número

#Solicitar ao usuário para inserir um número

numero = input("Digite um número: ")

#Calcula a raiz quadrada
raiz = numero ** 0.5

#Exibe a raiz quadrada
print("A raiz quadrada é: " + raiz)

Saída esperada(após a correção do código)
Se o usuário inserir o número 16, a saída esperada deve ser:
A raiz quadrada e: 4.0 '''


#Para realizar uma raiz quadrada e necessario chamar a funcao math, transformar o numero recebido de str em int e corrigir a exibicao da raiz
import math

numero = int(input("Digite um número: "))

#Calcula a raiz quadrada
raiz = numero ** 0.5
#raiz = math.sqrt(numero)

#Exibe a raiz quadrada
print("A raiz quadrada é: ", raiz)