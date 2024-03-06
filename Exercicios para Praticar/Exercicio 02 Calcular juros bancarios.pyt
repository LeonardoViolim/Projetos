'''Calcular os juros de um deposito bancario

#### Solucao 1 ####
Etapa 1 - Iniciar
Etapa 2 - Receber valor
Etapa 3 - Receber valor Juros
Etapa 4 - Calcular
Etapa 5 - Exibir novo valor
Etapa 6 - Fim

valor_devido = float(input("Informe o valor devido: "))
juros_mensais = float(input("Informe juros mensais em decimais: "))
valor_juros = valor_devido * juros_mensais
valor_devido_atualizado = valor_juros + valor_devido
print(valor_devido_atualizado)



#### Solucao 2 ####
Etapa 1 - Iniciar
Etapa 2 - Receber valor, anos, taxa
Etapa 4 - Calcular(juros = valor*ano*taxa/100)
Etapa 5 - Exibir juros
Etapa 6 - Fim

valor_inicial = float(input("Informe o valor inicial: "))
periodo_aplicacao = int(input("Informe o periodo da aplicação em meses: "))
taxa_aplicacao = float(input("Informe a taxa da aplicação: "))
juros = (valor_inicial*periodo_aplicacao*taxa_aplicacao)/100
valor_atualizado = valor_inicial+juros
print("O valor atualizado com juros e: ",valor_atualizado)
'''


#### Solucao 3 ####
#Etapa 1 - Iniciar
#Etapa 2 - Receber valor, anos, taxa
#Etapa 4 - Calcular(juros = valor*ano*taxa/100)
#Etapa 5 - Exibir juros
#Etapa 6 - Garanta que o cliente irá informar um valor válido
#Etapa 7 - Fim


#funcao para verificar se e um valor valido
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
#Solicitacao dos dados de entrada
while True:
    valor_inicial = float(input("Digite o valor inicial(R$): "))
    if is_number(valor_inicial):
        valor_inicial = float(valor_inicial)
        break
    else:
        print("Por favor, insira um valor numérico.")

while True:
    periodo_aplicacao = int(input("Digite o número de anos: "))
    if is_number(periodo_aplicacao):
        periodo_aplicacao = int(periodo_aplicacao)
        break
    else:
        print("Por favor, insira um valor numérico.")

while True:
    taxa_aplicacao = float(input("Digite a taxa de juros anual(%): "))
    if is_number(taxa_aplicacao):
        taxa_aplicacao = float(taxa_aplicacao)
        break
    else:
        print("Por favor, insira um valor numérico.")

#Calculo dos juros e do valor atualizado
juros = (valor_inicial*periodo_aplicacao*taxa_aplicacao)/100
valor_atualizado = valor_inicial+juros

#Impressao do Resultado
print(f"O valor atualizado após {periodo_aplicacao} anos e R${valor_atualizado:.2f}")
print(f"Os juros acumulados nesse período são R${juros}")