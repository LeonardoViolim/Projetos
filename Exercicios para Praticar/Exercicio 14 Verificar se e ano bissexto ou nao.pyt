'''Programa para verificar se o ano e bissexto ou nao

Etapa 1 - Iniciar
Etapa 2 - Ler ano
Etapa 3 - Se (ano%4==0)
Etapa 4 - True imprimir o ano e bissexto
Etapa 5 - False imprimir o ano nao e bissexto
Etapa 6 - Fim

'''

#Solicite ao usuário que insira o ano
ano = int(input("Insira o ano: "))
'''
#solucao sem levar em conta a regra dos anos bissextos
if (ano%4==0):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")
'''
#Resposta alternativa
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")

'''Esta parte verifica se o ano é divisível por 4 e não é divisível por 100.
Isso é necessário porque a maioria dos anos divisíveis por 4 são bissextos, exceto os anos múltiplos de 100,
que não são bissextos, a menos que também sejam múltiplos de 400. Ou seja, essa condição verifica a regra comum dos anos bissextos,
onde são divisíveis por 4, mas não por 100.'''