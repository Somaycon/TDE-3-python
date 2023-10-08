valor_produto = float(input("Digite o valor do produto: "))

estado_destino = input("Digite o estado destino (MG, SP, RJ, MS): ")

taxas_imposto = {
    "MG": 0.07,
    "SP": 0.12,
    "RJ": 0.15,
    "MS": 0.08
}

if estado_destino in taxas_imposto:
    
    taxa = taxas_imposto[estado_destino]
    preco_final = valor_produto * (1 + taxa)
    print(f"O preço final do produto em {estado_destino} é R$ {preco_final:.2f}.")
else:
    print("Estado destino inválido. Por favor, digite um estado válido (MG, SP, RJ, MS).")
