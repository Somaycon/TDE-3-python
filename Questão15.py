#Usando match, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
#correspondente a este número. Isto e, domingo se 1, segunda-feira se 2, e assim por diante.

dia = int(input("Digite um dia da semana(1 a 7): "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido")
