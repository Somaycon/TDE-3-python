peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do Peso"
elif 18.6 <= imc <= 24.9:
    classificacao = "Saudável"
elif 25.0 <= imc <= 29.9:
    classificacao = "Peso em Excesso"
elif 30.0 <= imc <= 34.9:
    classificacao = "Obesidade Grau I"
elif 35.0 <= imc <= 39.9:
    classificacao = "Obesidade Grau II (severa)"
else:
    classificacao = "Obesidade Grau III (mórbida)"

print(f"O IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
