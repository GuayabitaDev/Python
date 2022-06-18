#Juego de adivinar un numero.

import random

Ganador = random.randint(1, 10)
Usuario = int(input("Elige un numero al azar entre 1 y 10: "))

if Usuario == Ganador:
    print ("Felicidades haz acertado!")

if Usuario != Ganador:
    print("No acertaste :(")

if Usuario > 10: #Comprueba si el valor dado por el Usuario es Mayor a 10.
    print("Te pasaste del limite. Vuelve a intentarlo!")

if Usuario < 1: #Comprueba si el valor dado por el usuario es Menor a 1.
    print("Te quedaste corto del limite. Vuelve a intentarlo!")

print("El numero ganador era: {}".format(Ganador)) #Esto permite imprimir numeros y darles su formato apropiado para ello.