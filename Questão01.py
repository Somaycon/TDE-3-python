num1 = float(input("Digite um numero:"))
num2 = float(input("Digite outro numero:"))

if num1 > num2 and num1 != num2:
    print(f'{num1} é  maior que {num2}')
elif num2 > num1 and num2 != num1:
    print(f'{num2}é  menor que {num1}')