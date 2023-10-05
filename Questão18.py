#Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por
#exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza
#a operação, mostrando o resultado e saindo.


def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

print("Escolha uma operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = int(input("Digite o número da operação desejada: "))

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if opcao == 1:
    resultado = soma(valor1, valor2)
elif opcao == 2:
    resultado = subtracao(valor1, valor2)
elif opcao == 3:
    resultado = multiplicacao(valor1, valor2)
elif opcao == 4:
    resultado = divisao(valor1, valor2)
else:
    resultado = "Opção inválida!"

print(f"Resultado: {resultado}")
