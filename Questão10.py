#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando
#as seguintes fórmulas (onde h corresponde à altura):
#       • Homens: (72.7∗ h) − 58
#       • Mulheres: (62,1∗ h) − 44,7

nome = input("Digite seu nome: ")

sexo = input("Digite seu sexo (M para masculino, F para feminino): ")

h = float(input("Digite sua altura em metros: "))

if sexo.upper()== "M":
    peso_ideal = (72.7*h)-58
    genero = "masculino"

elif sexo.upper()=="F":
    peso_ideal = (62.1*h)-47
    genero = "femenino"
else:
    print("Sexo inválido. Digite apenas, 'Femenino' ou 'Masculino'")
    peso_ideal = None
    genero = None

if peso_ideal is not  None:
    print(f"Olá, {nome}! Seu peso ideal para um(a) individuo(a) {genero} com  a altura {h}m é aproximadamente {peso_ideal}kg. ")

