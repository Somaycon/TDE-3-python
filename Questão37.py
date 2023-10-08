chegada_hora, chegada_minuto = map(int, input("Digite a hora e os minutos de chegada (hh mm): ").split())
partida_hora, partida_minuto = map(int, input("Digite a hora e os minutos de partida (hh mm): ").split())

diferenca_horas = partida_hora - chegada_hora
diferenca_minutos = partida_minuto - chegada_minuto

total_minutos = (diferenca_horas * 60 + diferenca_minutos + 59) // 60

if total_minutos <= 120:
    preco = total_minutos * 1.00
elif total_minutos <= 240:
    preco = 120 * 1.00 + (total_minutos - 120) * 1.40
else:
    preco = 120 * 1.00 + 120 * 1.40 + (total_minutos - 240) * 2.00

print(f"O preço cobrado pelo estacionamento é: R$ {preco:.2f}")
