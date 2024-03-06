# Crie um programa que calcula o custo total e troco de itens comprados

#Etapa 1 - Iniciar
#Etapa 2 - Leia o PreçoPorUnidade
#Etapa 3 - Ler quantidade, valor_pago
#Etapa 4 - Calcular Custo Total(Custo_total = Quantidade * PreçoPorUnidade)
#Etapa 5 - Calcular Troco(Troco = Valor_pago - Custo Total)
#Etapa 6 - Exibir quantidade de itens comprados, custo total e troco
#Etapa 7 - Fim


#Solicite ao usuário que informe o preço por unidade e a quantidade
preco_produto1 = float(input("Informe o valor do produto em R$:"))
quantidade_produto1 = int(input("Informe a quantidade do produto escolhido:"))

#Calcule o custo total da compra
custo_total = preco_produto1 * quantidade_produto1

#Garantir que o valor pago seja maior que o valor a ser cobrado

valor_pago = float(input("Informe o valor ofertado para o pagamento:"))
while True:
    if valor_pago>=custo_total:
        break
    else:
        print("Valor insuficiente")
        valor_pago = float(input("Informe um valor igual ou maior que o custo total: "))

#Calcule o troco
troco = valor_pago - custo_total

#Exibir quantidade de itens comprados, custo total e troco
print(f"A quantidade de itens comprado foi de {quantidade_produto1}. O custo total foi de R${custo_total:.2f} e seu troco foi R${troco:.2f}. Obrigado pela compra!")