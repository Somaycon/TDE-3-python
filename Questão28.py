# Função para calcular a média geométrica
def media_geometrica(a, b, c):
    return (a * b * c) ** (1/3)

# Função para calcular a média ponderada
def media_ponderada(a, b, c):
    return (a + 2 * b + 3 * c) / 6

# Função para calcular a média harmônica
def media_harmonica(a, b, c):
    return 3 / (1/a + 1/b + 1/c)

# Função para calcular a média aritmética
def media_aritmetica(a, b, c):
    return (a + b + c) / 3

# Solicita ao usuário os três números
a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))
c = int(input("Digite o terceiro número inteiro positivo: "))

opcao = input("Escolha a média (a - Geométrica, b - Ponderada, c - Harmônica, d - Aritmética): ")

if opcao == 'a':
    resultado = media_geometrica(a, b, c)
    tipo_media = "Geométrica"
elif opcao == 'b':
    resultado = media_ponderada(a, b, c)
    tipo_media = "Ponderada"
elif opcao == 'c':
    resultado = media_harmonica(a, b, c)
    tipo_media = "Harmônica"
elif opcao == 'd':
    resultado = media_aritmetica(a, b, c)
    tipo_media = "Aritmética"
else:
    print("Opção inválida.")
    resultado = None

if resultado is not None:
    print(f"A média {tipo_media} dos números {a}, {b} e {c} é {resultado:.2f}.")
