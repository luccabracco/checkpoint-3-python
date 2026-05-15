temperaturas =  [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

sala_mais_critica = 0
maximo_critico = -1

for i in range (len(temperaturas)):
    sala_atual = temperaturas[i]
    numero_sala = i + 1

    media = sum(sala_atual) / len(sala_atual)

    critico = 0
    for temp in sala_atual:
        if temp >= 33:
            critico += 1

    print(f"Sala {numero_sala}")
    print(f"Média: {media}")
    print(f"Registros Criticos: {critico}")
    print()

    if critico > maximo_critico:
        maximo_critico = critico
        sala_mais_critica = numero_sala

print(f"Sala com maior risco: Sala {sala_mais_critica}")