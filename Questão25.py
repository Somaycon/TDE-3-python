a = float(input("Digite o coeficiente 'a' (diferente de zero): "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

if a == 0:
    print("Não é uma equação de segundo grau, pois 'a' deve ser diferente de zero.")
else:
    
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        print("Não existe raiz real.")
    elif discriminante == 0:
        raiz = -b / (2*a)
        print(f"Raiz única: {raiz}")
    else:
        raiz1 = (-b + (discriminante**0.5)) / (2*a)
        raiz2 = (-b - (discriminante**0.5)) / (2*a)
        print(f"Duas raízes reais: {raiz1} e {raiz2}")
