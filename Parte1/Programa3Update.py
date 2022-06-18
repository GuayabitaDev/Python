#Mejora del Programa3.py

#Valores del 17 de Junio de 2022
USD_CAD = 1.30 #Dolar Cadiense
USD_MXN = 20.34 #Pesos Mexicanos
USD_CLP = 876.80 #Pesos Chilenos
USD_AR = 122.87 #Pesos Argentinos
USD_COP = 3898.17 #Pesos Colombianos

Moneda = input("Selecciona la Moneda que deseas convertir a dolar! \n"
               "CAD - Dolar Canadiense \n"
               "MXN - Pesos Mexicanos \n"
               "CLP - Pesos Chilenos \n"
               "AR - Pesos Argentinos \n"
               "COP - Pesos Colombianos \n")

Cantidad = float(input("Inserte la cantidad de $ a convertir a dolares! \n"))

if Moneda == "CAD":
    print("$",Cantidad, "de CAD son {}".format(Cantidad / USD_CAD))

elif Moneda == "MXN":
    print("$",Cantidad, "de MXN son {}".format(Cantidad / USD_MXN))

elif Moneda == "CLP":
    print("$",Cantidad, "de CLP son {}".format(Cantidad / USD_CLP))

elif Moneda == "AR":
    print("$",Cantidad, "de AR son {}".format(Cantidad / USD_AR))

elif Moneda == "COP":
    print("$",Cantidad, "de COP son {}".format(Cantidad / USD_COP))