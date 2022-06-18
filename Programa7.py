#Test de PandaCommunity

Title = "Bienvenido a Examen sobre PandaCommunity"
print(Title)

Correct = "Respuesta Correcta!"
Wrong = "Respuesta Incorrecta!"
Invalid = "Respuesta Invalida!"
Score = 0

#----------------------------------------------------------------------------------------

Q1 = input("En que dia se creo PandaCommunity? \n"
           "A - 21 de Septiembre de 2021\n"
           "B - 15 de Noviembre de 2019\n"
           "C - 11 de Agosto de 2020\n")

if Q1 == "A":
    print(Wrong)
    Score += 0

elif Q1 == "B":
    print(Wrong)
    Score += 0

elif Q1 == "C":
    print(Correct)
    Score += 20

else:
    print(Invalid)

#----------------------------------------------------------------------------------------

Q2 = input("Como se llamaba PandaCommunity antes? \n"
           "A - Best Friends Code\n"
           "B - Veil Development\n"
           "C - Ninguna de las anteriores\n")

if Q2 == "A":
    print(Correct)
    Score += 20

elif Q2 == "B":
    print(Wrong)
    Score += 0

elif Q2 == "C":
    print(Wrong)
    Score += 0

else:
    print(Invalid)

#----------------------------------------------------------------------------------------

Q3 = input("Cuando se lanzo PandaHub? \n"
           "A - 15 de Diciembre\n"
           "B - 1 de Septiembre\n"
           "C - 1 de Enero\n")

if Q3 == "A":
    print(Wrong)
    Score += 0

elif Q3 == "B":
    print(Correct)
    Score += 20

elif Q3 == "C":
    print(Wrong)
    Score += 0

else:
    print(Invalid)

#----------------------------------------------------------------------------------------

Q4 = input("Cual fue el primer plugin hecho por Risas y Tulio? \n"
           "A - PandaHub\n"
           "B - PandaGKits\n"
           "C - FullPvP\n")

if Q4 == "A":
    print(Wrong)
    Score += 0

elif Q4 == "B":
    print(Wrong)
    Score += 0

elif Q4 == "C":
    print(Correct)
    Score += 20

else:
    print(Invalid)

#----------------------------------------------------------------------------------------

Q5 = input("IMPORTANTE: Quien es el mas guapo de Panda? \n"
           "A - Risas\n"
           "B - Tulio\n"
           "C - Todas las anteriores\n")

if Q5 == "A":
    print(Wrong)
    Score += 0

elif Q5 == "B":
    print(Correct)
    Score += 20

elif Q5 == "C":
    print(Wrong)
    Score += 0

else:
    print(Invalid)

#----------------------------------------------------------------------------------------
print("Tu puntuacion es de", Score)

if Score == 100:
    print("La respuesta siempre es Tulio!")

#----------------------------------------------------------------------------------------
