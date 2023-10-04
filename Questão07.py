a = int(input("Digite um numero inteiro: "))
b = int(input("Digite outro numero inteiro: "))

if a > b:
  print(a)
  print("A diferença entre eles é de " , a - b)
elif a < b:
    print(b)
    print("A diferença entre eles é de " , b - a)
else:
  print("Os numeros iguais")