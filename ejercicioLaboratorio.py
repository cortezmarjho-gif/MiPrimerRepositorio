import random

rondas = int(input("cuantas rondas quieres: "))
i = 1

puntosJ = 0
puntosC = 0

# while para las partidas
while i <= rondas:
    print("ronda", i)
    jugador = input("elige piedra, papel o tijera: ").lower()

    num = random.randint(1, 3)

    # "select case" en python sería if
    if num == 1:
        cpu = "piedra"
    elif num == 2:
        cpu = "papel"
    else:
        cpu = "tijera"

    print("la compu saco:", cpu)

    # if para ganador
    if jugador == cpu:
        print("empate")
    elif (jugador == "piedra" and cpu == "tijera") or \
         (jugador == "papel" and cpu == "piedra") or \
         (jugador == "tijera" and cpu == "papel"):
        print("ganaste")
        puntosJ += 1
    else:
        print("perdiste")
        puntosC += 1

    i += 1
    print()

# for para mostrar resultados
for x in range(1):
    print("tus puntos:", puntosJ)
    print("puntos compu:", puntosC)

if puntosJ > puntosC:
    print("ganaste el juego")
elif puntosJ < puntosC:
    print("perdiste el juego")
else:
    print("quedaron empate")