#Programa para ver si alguien aplica para un desuento al ir al Zoologico.

edad = int(input("Digame su edad: "))
carnet = input("Digame su tipo de carnet (F/P/F+/N")

if (25 < edad < 35 and carnet == "E") or edad < 10 or (edad > 65 and carnet == "P") or carnet == "F+":
    #La expresion AND como su traduccion lo dice es Y asi que cuando se hacen condiciones es posible agregar otro requisito para cumplir la tarea.
    #La expresion OR como su traduccion lo dice es O asi que cuando se hacen condiciones es posible agregar otra forma de cumplir alguna tarea.

    print("Se te aplica el descuento.")
else:
    print("No se te aplica el descuento.")
