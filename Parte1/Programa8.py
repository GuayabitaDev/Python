#Esto es un combate pokemon con variaciones dependiendo de tus elecciones. Elige sabiamente!

Ganaste = "Felicidades debido a tus sabias decisiones lograste ganar el combate!"
Perdiste = "Que lastima! Vuelve a intentarlo."
Huiste = "Escapas sin problemas! Sin embargo el combate termina."

YourHP = 100
EnemyHP = 100

print("Bienvenido Entrenador Pokemon, este sera tu primer combate contra Ash cuyo pokemon es Pikachu tipo electrico, \n"
      "como es tu primer combate elige un pokemon entre, \n"  
      "A - Greninja (Tipo Agua) \n"
      "B - Pterodactyl (Tipo Tierra) \n"
      )
Pokemon = input("Cual es tu eleccion? \n")

#--------------------------------------------------------------------------------------------------------------------

if Pokemon == "A":
    print("Seleccionaste a Greninja, estas en desventaja pero aun asi este combate no es imposible! \n")
    CombateInicial = (input("El combate empezo! Ash saca a Pikachu y tu a Greninja, que decides? \n"
                          "A - Atacar \n"
                          "B - Bolsa \n"
                          "C - Huir \n"
    ))
    if CombateInicial == "A":
        print("Le bajaste 15 HP a tu enemigo pero te contrataca y te hace un ataque supereficaz que te quita 50 \n")
        YourHP -= 50
        EnemyHP -= 15

        CombateA1 = (input("Cual es tu siguente movimiento? \n"
                              "A - Atacar \n"
                              "B - Bolsa \n"
                              "C - Huir \n"))
        if CombateA1 == "A":
            print("Le bajaste 20 HP a tu enemigo pero te contrataca con otro ataque supereficaz y debilita a tu Pokemon \n")
            print(Perdiste)

        #Final de la Opcion A



    elif CombateInicial == "B":
        print("Sacaste una capsula de Defensa X y tu defensa sube mucho, aun asi tu enemigo contrataca y te quita 20HP \n")
        YourHP -= 20
        
        CombateB1 = (input("Cual es tu siguente movimiento? \n"
                              "A - Atacar \n"
                              "B - Bolsa \n"
                              "C - Huir \n"))
        if CombateB1 == "A":
            print ("Le bajaste 20 HP a tu enemigo pero te contrataca y te quita 20 HP \n")
            YourHP -= 20
            EnemyHP -= 20

        elif CombateB1 == "B":
            print("Sacas otra Capsula de Defensa X y tu defensa vuelve a subir mucho, pero tu enemigo contrataca y te baja 10HP \n")
            YourHP -= 10

            CombateB2 = (input("Cual es tu siguiente movimiento? \n"
                                  "A - Atacar \n"
                                  "B - Bolsa \n"
                                  "C - Huir \n"))


        elif CombateB1 == "C":
            print(Huiste)

    elif CombateInicial == "C":
        print(Huiste)

        #Final de la Opcion C