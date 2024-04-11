# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

carnes = {
    "fileduplo": {
        "5kg_ou_menos": 4.90,
        "mais_de_5kg": 5.80,
    },
    "alcatra": {
        "5kg_ou_menos": 5.90,
        "mais_de_5kg": 6.80,
    },
    "picanha": {
        "5kg_ou_menos": 6.90,
        "mais_de_5kg": 7.80,
    },
}

tipo_carne = input("Qual carne você deseja? (fileduplo, alcatra, picanha): ")

quantidade_carne = float(input("Digite a quantidade de carne em kg: "))

if tipo_carne not in carnes:
    print("Tipo de carne inválido.")
    exit()

preco_total = 0

if quantidade_carne <= 5:
    preco_total = quantidade_carne * carnes[tipo_carne]["5kg_ou_menos"]
else:
    preco_total = quantidade_carne * carnes[tipo_carne]["mais_de_5kg"]


tipo_pagamento = input("Digite o tipo de pagamento (cartaotabajara, outro): ")


if tipo_pagamento == "cartaotabajara":
    desconto = preco_total * 0.05
    preco_total = preco_total - desconto

    
print("Hipermercado Tabajara: NOTA FISCAL")
print("-----------------------------------------------------")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade_carne}, kg")
print(f"Preço total: {preco_total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")

if tipo_pagamento == "cartaotabajara":
    print(f"Desconto: {desconto:.2f}")
    print(f"Valor a pagar: {preco_total:.2f}")
print("-----------------------------------------------------")
