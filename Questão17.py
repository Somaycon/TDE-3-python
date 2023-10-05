#Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
#BM+bm*h/2
#Lembre-se a base maior a base menor e a altura devem ser números maiores que zero.

base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))

if base_maior > 0 and base_menor > 0 and altura > 0:
    area_trapezio = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é: {area_trapezio}")
else:
    print("Valores inválidos. Certifique-se de que a base maior, a base menor e a altura são maiores que zero.")
