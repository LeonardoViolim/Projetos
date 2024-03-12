'''
Desafio
Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes.
Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos
por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

Entrada
Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo,
representando a quantidade de passos que o explorador deve dar na floresta.

Saída
O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta.
Utilize um laço de repetição para simular os passos do explorador.
A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

----------Código Fornecido-------------
#Desafio: A Aventura do Explorador

#Entrada
quantidade_passos = int(input())

//TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
// Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
// Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

----------Entradas Fornecidas----------
2
3
0

----------Saídas Esperadas-------------
Explorador: 1 passo
Explorador: 2 passos

Explorador: 1 passo
Explorador: 2 passos
Explorador: 3 passos

Nenhum passo dado na floresta.

'''

#Resposta para a plataforma de testes da DIO
#Desafio: A Aventura do Explorador

quantidade_passos = int(input())

if quantidade_passos > 0:
    palavraPasso = "passo"
    
    for contador in range(quantidade_passos):
        if contador > 0:
            palavraPasso = "passos"
        else:
            palavraPasso = "passo"
        print("Explorador: ", contador + 1, palavraPasso)
else:
    print("Nenhum passo dado na floresta.")
#Aprovado