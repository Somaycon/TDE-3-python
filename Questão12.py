# Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número inválido”. Se o número
#for positivo, calcular o logaritmo deste número.

import math

numero = int(input("Digite um numero inteiro: "))

if numero < 0:
    print("Numero Inválido")
else:
    resultado = math.log(numero)
    print(f"O logaritmo de {numero} é: {resultado}")
