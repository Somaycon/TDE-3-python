salario_atual = float(input("Digite o valor do salário atual do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário (em anos): "))

reajuste = 0
bonus = 0

if salario_atual <= 500:
    reajuste = salario_atual * 0.25
elif salario_atual <= 1000:
    reajuste = salario_atual * 0.20
elif salario_atual <= 1500:
    reajuste = salario_atual * 0.15
elif salario_atual <= 2000:
    reajuste = salario_atual * 0.10

if tempo_servico < 1:
    bonus = 0
elif tempo_servico <= 3:
    bonus = 100
elif tempo_servico <= 6:
    bonus = 200
elif tempo_servico <= 10:
    bonus = 300
else:
    bonus = 500
    
salario_reajustado = salario_atual + reajuste + bonus

if reajuste == 0:
    print("O funcionário não tem direito a aumento.")
else:
    print(f"Salário final reajustado: R$ {salario_reajustado:.2f}")
