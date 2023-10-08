def soma(a, b):
    return a + b

def diferenca(a, b):
    if a > b:
        return a - b
    else:
        return b - a

def produto(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

opcao = int(input("Opção: "))

if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = soma(num1, num2)
    print("Resultado:", resultado)
elif opcao == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = diferenca(num1, num2)
    print("Resultado:", resultado)
elif opcao == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = produto(num1, num2)
    print("Resultado:", resultado)
elif opcao == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número (diferente de zero): "))
    resultado = divisao(num1, num2)
    print("Resultado:", resultado)
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
