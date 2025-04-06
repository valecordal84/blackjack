import random

print("Bienvenido al juego de Blackjack")

def repartir():    
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(cartas)
    return carta

def puntuacion(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    
    if 11 in cartas and sum (cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
        
    return sum(cartas)

def comparacion (puntuacion_j, puntuacion_d):
    if puntuacion_j == puntuacion_d:
        return "Empate"
    elif puntuacion_d == 0:
        return "La casa gana"
    elif puntuacion_j == 0:
        return "Blackjack! Ganaste "
    elif puntuacion_j > 21:
        return "Perdiste, sumaste mas de 21"
    elif puntuacion_d > 21:
        return "Ganaste! Dealer suma mas de 21"
    elif puntuacion_j > puntuacion_d:
        return "Ganaste!"
    else:
        return "Perdiste! "

jugador = []
dealer = []
puntuacion_jugador = -1
puntuacion_dealer = -1
juego_terminado = False



for a in range(2):
    jugador.append(repartir())
    dealer.append(repartir())

while not juego_terminado:
    puntuacion_jugador = puntuacion(jugador)
    puntuacion_dealer = puntuacion(dealer)
    print(f"Tus cartas son: {jugador}, tienes {puntuacion_jugador}")
    print(f"La carta del dealer es: {dealer[0]}")
    

    if puntuacion_jugador == 0 or puntuacion_dealer == 0 or puntuacion_jugador > 21:
        juego_terminado = True 
    else:
        pedir = input("Quieres pedir otra carta? \n escribe 's' para pedir una carta mas o 'n' para plantarte: ")
        if pedir == "s":
            jugador.append(repartir())
        else:
            juego_terminado = True
            
while puntuacion_dealer != 0 and puntuacion_dealer < 17:
    dealer.append(repartir()) 
    puntuacion_dealer = puntuacion(dealer)
    
print(f"Tu mano es {jugador} tienes {puntuacion_jugador}, la mano del dealer es {dealer} tiene {puntuacion_dealer}")
print (comparacion(puntuacion_jugador, puntuacion_dealer))

