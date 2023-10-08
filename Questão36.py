valor_venda = float(input("Digite o valor da venda: "))

comissao = 0

if valor_venda >= 100000:
    comissao = 700 + (0.16 * valor_venda)
elif 80000 <= valor_venda < 100000:
    comissao = 650 + (0.14 * valor_venda)
elif 60000 <= valor_venda < 80000:
    comissao = 600 + (0.14 * valor_venda)
elif 40000 <= valor_venda < 60000:
    comissao = 550 + (0.14 * valor_venda)
elif 20000 <= valor_venda < 40000:
    comissao = 500 + (0.14 * valor_venda)
else:
    comissao = 400 + (0.14 * valor_venda)

print(f"A comissão a ser paga ao vendedor é: R$ {comissao:.2f}")
