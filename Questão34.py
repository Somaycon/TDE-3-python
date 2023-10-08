nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

if faltas <= 20:
    if 9.0 <= nota <= 10.0:
        conceito = "A"
    elif 7.5 <= nota < 9.0:
        conceito = "B"
    elif 5.0 <= nota < 7.5:
        conceito = "C"
    elif 4.0 <= nota < 5.0:
        conceito = "D"
    elif 0.0 <= nota < 4.0:
        conceito = "E"
    else:
        conceito = "Nota inválida"
else:
    if 9.0 <= nota <= 10.0:
        conceito = "B"
    elif 7.5 <= nota < 9.0:
        conceito = "C"
    elif 5.0 <= nota < 7.5:
        conceito = "D"
    elif 4.0 <= nota < 5.0:
        conceito = "E"
    elif 0.0 <= nota < 4.0:
        conceito = "E"
    else:
        conceito = "Nota inválida"

print(f"Conceito do aluno: {conceito}")
