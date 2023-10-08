import random

def gerar_numero_aleatorio():
    return random.randint(1, 100)

def realizar_prova(num_perguntas):
    acertos = 0
    for _ in range(num_perguntas):
      
        a = gerar_numero_aleatorio()
        b = gerar_numero_aleatorio()

        resposta_correta = a + b

        print(f"Pergunta: Qual é a soma de {a} + {b}?")

        resposta_aluno = int(input("Resposta: "))

        if resposta_aluno == resposta_correta:
            print("Resposta correta!\n")
            acertos += 1
        else:
            print(f"Resposta incorreta. A resposta correta era {resposta_correta}.\n")

    return acertos

numero_de_perguntas = 5
acertos = realizar_prova(numero_de_perguntas)

print(f"Você acertou {acertos} de {numero_de_perguntas} perguntas.")
