# utilizando los conocimentos de programacion
# definimos el "while"
while True:
    print("La comelona")
    print("Menu")
    print("A| BEBIDAS ") 
    print("B| COMIDAS")
    print("C| POSTRES")
    print("D| SALIR")        #agregando otra opcion para tener mas completo la seccion de menu 

opcion="menu" or "Menu"

# Definimos la condicion if"si"
# colocamos el listado de menu

if opcion=="menu" or "Menu": # colocamos las 2 posibles formas de escritura para acceder al menu

    while true:              # Mientras que se verdadero imprimira el siguiente menu
        print("BEBIDAS")
        print("A| café")
        print("B| chocolate")
        print("C| maca")
        print("D| quinua")
        print("E| refresco")
        print("F| REGRESAR")

        opcion2==input("SELECIONE SU BEBIDA [A..f]: ")

        if opcion2=="A" or "a":
            print("Café")
        elif opcion2=="B" or "b":
            print("Chocoloate")
        elif opcion2=="C" or "c":
            print("Maca")
        elif opcion2=="D" or "d":
            print("Quinua")
        elif opcon2=="E" or "e":
            print("Refresco")
            break
        else:
           print()




