#Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20%
#do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.

salario = float(input("Qual o salario do trabalhador? "))
prest_emprestimo = float(input("Digite o valor da prestação do esmprestimo: "))

lim_prestacao = 0.2*salario

if prest_emprestimo > lim_prestacao:
    print("Infelizmente o emprestimo não pode ser concedido. ")

else:
    print("Parabens! Seu emprestimo foi concedido.")    
