#Este programa es la continuacion del Programa 8, ya que lo decidi hacer desde 0 por muchas razones 
#la principal es que aprendi una forma de hacerlo mas sencilla y rapida. Inspirado en el combate Final de XYZ

from random import randint

#Estadisticas de Greninja
HP_Greninja = 100
IHP_Greninja = 100

#Estadisticas de Charizard
HP_Charizard = 100
IHP_Charizard = 100

while HP_Greninja > 0 and HP_Charizard > 0:
    #Funcion de los turnos del Combate
    
    #Turno de Charizard
    print("Turno de Charizard")
    AttackCharizard = randint(1,2)
    if AttackCharizard == 1:
        #Envite Igneo
        print("Charizard ha usado Envite Igneo!")
        HP_Greninja -= 20

    elif AttackCharizard == 2:
        #Puño Electrico
        print("Charizard ha usado Puño Electrico!")
        HP_Greninja -= 10

    else:
        #Acrobacias
        print("Charizard ha usado Acrobacias!")
        HP_Greninja -= 10

    print("La vida de Greninja es [{}]".format(HP_Greninja * "#"))
    print("La vida de Charizar es [{}]". format(HP_Charizard * "#"))
    input("Presiona ENTER para continuar...")

    #Turno de Greninja
    print("Turno de Greninja")
    AttackGreninja = None
    while AttackGreninja != "A" and AttackGreninja != "B" and AttackGreninja != "C":

        AttackGreninja = input("Que ataque quieres usar?")
        if AttackGreninja == "A":
            #Shuriken de Agua
            print("Greninja ha usado Shuriken de Agua!")
            HP_Charizard -= 20

        elif AttackGreninja == "B":
            #Corte
            print("Greninja ha usado Corte!")
            HP_Charizard -= 10

        elif AttackGreninja == "C":
            #Az Areo
            print("Greninja ha usado Az Aereo!")
            HP_Charizard -= 10

    print("La vida de Greninja es {} y la vida de Charizard es {}".format(HP_Greninja, HP_Charizard))
    input("Presiona ENTER para continuar...")

if HP_Charizard > HP_Greninja:
    print("Charizard es el Ganador!")
else:
    print("Greninja es el Ganador!")#Este programa es la continuacion del Programa 8, ya que lo decidi hacer desde 0 por muchas razones 
#la principal es que aprendi una forma de hacerlo mas sencilla y rapida. Inspirado en el combate Final de XYZ

from random import randint

#Estadisticas de Greninja
HP_Greninja = 100
IHP_Greninja = 100

#Estadisticas de Charizard
HP_Charizard = 100
IHP_Charizard = 100

while HP_Greninja > 0 and HP_Charizard > 0:
    #Funcion de los turnos del Combate
    
    #Turno de Charizard
    print("Turno de Charizard")
    AttackCharizard = randint(1,2)
    if AttackCharizard == 1:
        #Envite Igneo
        print("Charizard ha usado Envite Igneo!")
        HP_Greninja -= 20

    elif AttackCharizard == 2:
        #Puño Electrico
        print("Charizard ha usado Puño Electrico!")
        HP_Greninja -= 10

    else:
        #Acrobacias
        print("Charizard ha usado Acrobacias!")
        HP_Greninja -= 10

    print("La vida de Greninja es [{}]".format(HP_Greninja * "#"))
    print("La vida de Charizar es [{}]". format(HP_Charizard * "#"))
    input("Presiona ENTER para continuar...")

    #Turno de Greninja
    print("Turno de Greninja")
    AttackGreninja = None
    while AttackGreninja != "A" and AttackGreninja != "B" and AttackGreninja != "C":

        AttackGreninja = input("Que ataque quieres usar?")
        if AttackGreninja == "A":
            #Shuriken de Agua
            print("Greninja ha usado Shuriken de Agua!")
            HP_Charizard -= 20

        elif AttackGreninja == "B":
            #Corte
            print("Greninja ha usado Corte!")
            HP_Charizard -= 10

        elif AttackGreninja == "C":
            #Az Areo
            print("Greninja ha usado Az Aereo!")
            HP_Charizard -= 10

    print("La vida de Greninja es {} y la vida de Charizard es {}".format(HP_Greninja, HP_Charizard))
    input("Presiona ENTER para continuar...")

if HP_Charizard > HP_Greninja:
    print("Charizard es el Ganador!")
else:
    print("Greninja es el Ganador!")#Este programa es la continuacion del Programa 8, ya que lo decidi hacer desde 0 por muchas razones 
#la principal es que aprendi una forma de hacerlo mas sencilla y rapida. Inspirado en el combate Final de XYZ

from random import randint

#Estadisticas de Greninja
HP_Greninja = 100
IHP_Greninja = 100

#Estadisticas de Charizard
HP_Charizard = 100
IHP_Charizard = 100

while HP_Greninja > 0 and HP_Charizard > 0:
    #Funcion de los turnos del Combate
    
    #Turno de Charizard
    print("Turno de Charizard")
    AttackCharizard = randint(1,2)
    if AttackCharizard == 1:
        #Envite Igneo
        print("Charizard ha usado Envite Igneo!")
        HP_Greninja -= 20

    elif AttackCharizard == 2:
        #Puño Electrico
        print("Charizard ha usado Puño Electrico!")
        HP_Greninja -= 10

    else:
        #Acrobacias
        print("Charizard ha usado Acrobacias!")
        HP_Greninja -= 10

    print("La vida de Greninja es [{}]".format(HP_Greninja * "#"))
    print("La vida de Charizar es [{}]". format(HP_Charizard * "#"))
    input("Presiona ENTER para continuar...")

    #Turno de Greninja
    print("Turno de Greninja")
    AttackGreninja = None
    while AttackGreninja != "A" and AttackGreninja != "B" and AttackGreninja != "C":

        AttackGreninja = input("Que ataque quieres usar?")
        if AttackGreninja == "A":
            #Shuriken de Agua
            print("Greninja ha usado Shuriken de Agua!")
            HP_Charizard -= 20

        elif AttackGreninja == "B":
            #Corte
            print("Greninja ha usado Corte!")
            HP_Charizard -= 10

        elif AttackGreninja == "C":
            #Az Areo
            print("Greninja ha usado Az Aereo!")
            HP_Charizard -= 10

    print("La vida de Greninja es {} y la vida de Charizard es {}".format(HP_Greninja, HP_Charizard))
    input("Presiona ENTER para continuar...")

if HP_Charizard > HP_Greninja:
    print("Charizard es el Ganador!")
else:
    print("Greninja es el Ganador!")#Este programa es la continuacion del Programa 8, ya que lo decidi hacer desde 0 por muchas razones 
#la principal es que aprendi una forma de hacerlo mas sencilla y rapida. Inspirado en el combate Final de XYZ

from random import randint

#Estadisticas de Greninja
HP_Greninja = 100
IHP_Greninja = 100

#Estadisticas de Charizard
HP_Charizard = 100
IHP_Charizard = 100

while HP_Greninja > 0 and HP_Charizard > 0:
    #Funcion de los turnos del Combate
    
    #Turno de Charizard
    print("Turno de Charizard")
    AttackCharizard = randint(1,2)
    if AttackCharizard == 1:
        #Envite Igneo
        print("Charizard ha usado Envite Igneo!")
        HP_Greninja -= 20

    elif AttackCharizard == 2:
        #Puño Electrico
        print("Charizard ha usado Puño Electrico!")
        HP_Greninja -= 10

    else:
        #Acrobacias
        print("Charizard ha usado Acrobacias!")
        HP_Greninja -= 10

    print("La vida de Greninja es [{}]".format(HP_Greninja * "#"))
    print("La vida de Charizar es [{}]". format(HP_Charizard * "#"))
    input("Presiona ENTER para continuar...")

    #Turno de Greninja
    print("Turno de Greninja")
    AttackGreninja = None
    while AttackGreninja != "A" and AttackGreninja != "B" and AttackGreninja != "C":

        AttackGreninja = input("Que ataque quieres usar?")
        if AttackGreninja == "A":
            #Shuriken de Agua
            print("Greninja ha usado Shuriken de Agua!")
            HP_Charizard -= 20

        elif AttackGreninja == "B":
            #Corte
            print("Greninja ha usado Corte!")
            HP_Charizard -= 10

        elif AttackGreninja == "C":
            #Az Areo
            print("Greninja ha usado Az Aereo!")
            HP_Charizard -= 10

    print("La vida de Greninja es {} y la vida de Charizard es {}".format(HP_Greninja, HP_Charizard))
    input("Presiona ENTER para continuar...")

if HP_Charizard > HP_Greninja:
    print("Charizard es el Ganador!")
else:
    print("Greninja es el Ganador!")
