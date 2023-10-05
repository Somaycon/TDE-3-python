#A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
#respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das
#três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral:3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9),
#de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.


nota_laboratorio = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
nota_semestral = float(input("Digite a nota da avaliação semestral (0 a 10): "))
nota_final = float(input("Digite a nota do exame final (0 a 10): "))

media = (nota_laboratorio * 2 + nota_semestral * 3 + nota_final * 5) / 10

if 0 <= media <= 2.9:
    situacao = "Reprovado"
elif 3 <= media <= 4.9:
    situacao = "Em recuperação"
else:
    situacao = "Aprovado"

print(f"Média final: {media}")
print(f"Situação do aluno: {situacao}")
