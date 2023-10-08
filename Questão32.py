cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hamburguer", 1.20),
    104: ("Cheeseburguer", 1.70),
    105: ("Suco", 2.20),
    106: ("Refrigerante", 1.00)
}

print("Código | Especificação | Preço")
for codigo, (especificacao, preco) in cardapio.items():
    print(f"{codigo:6} | {especificacao:13} | R$ {preco:.2f}")

codigo_produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

if codigo_produto in cardapio:
   
    especificacao, preco_unitario = cardapio[codigo_produto]
    
    valor_total = preco_unitario * quantidade
    print(f"Produto: {especificacao}")
    print(f"Valor a ser pago: R$ {valor_total:.2f}")
else:
    print("Código do produto inválido. Por favor, escolha um código válido do cardápio.")

