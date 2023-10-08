A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))


if A + B > C and A + C > B and B + C > A:
    
    if A == B and B == C:
        print("É um triângulo equilátero.")
   
    elif A == B or A == C or B == C:
        print("É um triângulo isósceles.")
    
    else:
        print("É um triângulo escaleno.")
else:
    print("Os valores não formam um triângulo.")
