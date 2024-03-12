'''
Desafio
Em um jogo de RPG, os personagens geralmente possuem uma lista de itens que podem ser utilizados durante o jogo.
Esses itens podem ser armas, armaduras, poções de cura, entre outros.
É importante que o jogador tenha um controle desses itens para poder utilizá-los no momento adequado.
Crie um programa que permita cadastrar uma lista de itens que o personagem possui.
A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

Entrada
O programa deve solicitar ao usuário o nome dos 3 itens que o personagem possui.
Cada item deve ser cadastrado separadamente.

Saída
Após receber os itens cadastrados pelo usuário, o programa deve exibir na tela a lista de itens que o personagem possui.
A saída deve ter o seguinte formato:

Lista de itens:
- [item1]
- [item2]
- [item3]

----------Código Fornecido-------------
# Lista para armazenar os itens
itens = []

//TODO: Solicite os itens ao usuário

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")

----------Entradas Fornecidas----------
Espada
Escudo
Poção

Gema
Flecha
Capa

Masterball
Potion
Elixir

----------Saídas Esperadas-------------
Lista de itens:
- Espada
- Escudo
- Poção

Lista de itens:
- Gema
- Flecha
- Capa

Lista de itens:
- Masterball
- Potion
- Elixir

'''

#Resposta para a plataforma de testes da DIO
#Desafio: Lista de itens

itens = []

item1 = input()
item2 = input()
item3 = input()
itens.append(item1)
itens.append(item2)
itens.append(item3)

print("Lista de itens:")
for item in itens:
    print(f"- {item}")
#Aprovado
    

