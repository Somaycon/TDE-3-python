distancia_km = float(input("Digite a distância em Km percorrida: "))

litros_gasolina = float(input("Digite a quantidade de litros de gasolina consumidos: "))

consumo_km_por_litro = distancia_km / litros_gasolina

if consumo_km_por_litro < 8:
    mensagem = "Venda o carro!"
elif 8 <= consumo_km_por_litro <= 14:
    mensagem = "Econômico!"
else:
    mensagem = "Super econômico!"

print(f"Consumo: {consumo_km_por_litro} Km/l - {mensagem}")
