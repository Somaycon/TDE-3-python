#Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a ́ soma de todos os
#seus algarismos. Por exemplo, ao número 251 corresponderá o valor ́ 8 (2 + 5 + 1). Se o número lido não for
#maior do que zero, o programa terminará com a mensagem “Número inválido”.

def soma_alg(numero):
#palavra-chave para  definir uma função.
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero = numero // 10
    return soma
numero = int(input("Digite um número inteiro maior do que zero: "))

if numero <= 0:
    print("Número inválido")
else:

    resultado = soma_alg(numero)
    print(f"A soma dos algarismos do número {numero} é: {resultado}")
