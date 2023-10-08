preco_antigo = float(input("Digite o preço antigo do produto: "))

if preco_antigo <= 50:
    percentual_aumento = 5
elif preco_antigo <= 100:
    percentual_aumento = 10
else:
    percentual_aumento = 15

preco_novo = preco_antigo + (preco_antigo * percentual_aumento / 100)

if preco_novo <= 80:
    mensagem = "Barato"
elif preco_novo <= 120:
    mensagem = "Normal"
elif preco_novo <= 200:
    mensagem = "Caro"
else:
    mensagem = "Muito caro"

print(f"Preço novo: R$ {preco_novo:.2f}")
print(f"Classificação: {mensagem}")
