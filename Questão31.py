altura = float(input("Digite a altura (em metros): "))
peso = float(input("Digite o peso (em quilogramas): "))

if altura < 1.20:
    if peso <= 60:
        classificacao = "A"
    elif peso <= 90:
        classificacao = "D"
    else:
        classificacao = "G"
elif altura <= 1.70:
    if peso <= 60:
        classificacao = "B"
    elif peso <= 90:
        classificacao = "E"
    else:
        classificacao = "H"
else:
    if peso <= 60:
        classificacao = "C"
    elif peso <= 90:
        classificacao = "F"
    else:
        classificacao = "I"

print(f"A classificação da pessoa é: {classificacao}")
