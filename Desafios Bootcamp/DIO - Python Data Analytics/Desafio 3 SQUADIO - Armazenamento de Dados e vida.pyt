'''
Descrição
Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético,
agora a mineração está muito mais eficiente! Com isso, os CodeMiners logo terão que aumentar a capacidade de
armazenamento de dados em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade!
Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

Entrada
Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço.

Saída
A nova capacidade total em teraflops.

----------Código Fornecido-------------
capacidade_atual, aumento_percentual = map(int, input().split())

// TODO: Calcule a nova capacidade do disco de Mithril
// TODO: Imprima a nova capacidade

----------Entradas Fornecidas----------
100 20
50 10
200 50

----------Saídas Esperadas-------------
120
55
300

'''

#Resposta para a plataforma de testes da DIO
#Desafio: Armazenamento de Dados é Vida!

capacidade_atual, aumento_percentual = map(int, input().split())

capacidade_nova = capacidade_atual + (capacidade_atual * (aumento_percentual/100))

print(int(capacidade_nova))
#Aprovado

