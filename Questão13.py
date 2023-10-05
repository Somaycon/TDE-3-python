#Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm
#peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou
#reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.



nota_prova1 = float(input("Digite a nota da primeira prova: "))
nota_prova2 = float(input("Digite a nota da segunda prova: "))
nota_prova3 = float(input("Digite a nota da terceira prova: "))

# Calcula a média ponderada com pesos 1, 1 e 2 para as três provas, respectivamente
media_pond = (nota_prova1 * 1 + nota_prova2 * 1 + nota_prova3 * 2) / 4

# Verifica se a média é maior ou igual a 60 para determinar se o aluno foi aprovado ou reprovado
if media_pond >= 60:
    print(f"Média do aluno: {media_pond}")
    print("Aluno aprovado!")
else:
    print(f"Média do aluno: {media_pond}")
    print("Aluno reprovado.")
