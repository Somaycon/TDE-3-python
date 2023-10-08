ANO_ATUAL = 2023

dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

if ano <= ANO_ATUAL:
  
    if 1 <= mes <= 12:
   
        if mes == 2:  
            if eh_bissexto(ano):
                dias_no_mes = 29
            else:
                dias_no_mes = 28
        elif mes in (4, 6, 9, 11):  
            dias_no_mes = 30
        else:
            dias_no_mes = 31

        if 1 <= dia <= dias_no_mes:
            print("Data válida")
        else:
            print("Data inválida")
    else:
        print("Data inválida")
else:
    print("Data inválida")
