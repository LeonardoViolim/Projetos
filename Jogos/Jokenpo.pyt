from random import randint

def user_interface(options):
    
    #Função apresentando opções e pedindo feedback do jogador
    #retorna inteiro.
    
    for index,option in enumerate(options):
        print(f"{index} = {option}")

    user_input = int(input("O que você escolhe?"))
    return user_input


def computer_choice(content):
    
    #função que gera um número aleatório com base nas opções disponíveis.
    #retorna int aleatório
    
    computer_chose = randint(0,len(content)-1)
    return computer_chose
    

def check_results(choices, player, computer):
    
    #função que verifica quem ganhou.
    #retorna string
    
    if player == computer:
        return 'Empate'
    elif (player == 0 and computer == len(choices)-1) or (player>computer and not(player==len(choices)-1 and computer==0)):
        return 'Player Ganhou'
    return 'Player Perdeu'


def play():
    print('''
    ---------------------------------
    Bem-vindo ao Pedra, Papel e Tesoura.
    Por favor, faça a sua escolha.
    ''')

    #defina as opções e peça aos concorrentes que escolham uma
    options_list = ["Pedra", "Papel" , "Tesoura"]
    player_result = user_interface(options_list)
    computer_result = computer_choice(options_list)
    
    #representação visual no terminal para que possamos ver o que ambas as partes escolheram
    print(f" Escolha do Jogador: {options_list[player_result]}")
    print(f"Escolha do computador: {options_list[computer_result]}")

    #confira os resultados entre os dois e imprima o vencedor
    results = check_results(options_list,player_result,computer_result)
    print (f'\n{results}')

def main():

    #forçar o jogador a entrar no loop de reprodução
    play_again = ""
    while play_again.lower() != "n":
        play()
        print (f"Você quer jogar de novo?")
        play_again = input("Escreva\'S\' para SIM ou \'N\' para NAO: ")

main()