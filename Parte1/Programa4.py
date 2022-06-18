#Este programa te prepara un chocolate

print("Voy a la cocina")
print("Abro el refrigerador")

Leche = input("Hay Leche en el refrigerador? (S/N)")
Chocolate = input("Hay Chocolate en la alacena? (S/N)")

if Leche != "S" or Chocolate != "S": #La expresion '!=' dice que si el valor es distinto a la string dada entonces ejecutara el comando en este caso Print.
    print("Tengo que ir al SuperMercado")

    if Leche != "S": #Esto determina si el valor es distinto a 'S' entonces ejecutara el comando print.
        print("Agrego Leche a la lista de compras.")

    if Chocolate != "S": #Esto determina si el valor es distinto a 'S' entonces ejecutara el comando print.
        print("Agrego Chocolate a la lista de compras.")

print("Ponemos la leche en el vaso")
print("Ponemos el Chocolate en el vaso")
print("Mezclamos!")