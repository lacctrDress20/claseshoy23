# utilizando los conocimentos de programacion
# definimos el "while"
from argparse import OPTIONAL
from optparse import Option
from pickle import TRUE


while True:
    print("La comelona")
    print("Menu")
    print("A| BEBIDAS ") 
    print("B| COMIDAS")
    print("C| POSTRES")
    print("D| SALIR")        #agregando otra opcion para tener mas completo la seccion de menu 
    Option==input("Selecione una opcion [A..B]: ")
    if Option=="A" or "a":       # colocamos las 2 posibles formas de escritura para acceder al menu

        while TRUE:              # Mientras que se verdadero imprimira el siguiente menu
            print("BEBIDAS")
            print("A| café")
            print("B| chocolate")
            print("C| maca")
            print("D| quinua")
            print("E| refresco")
            print("F| REGRESAR")

            Option==input("SELECIONE SU BEBIDA [A..f]: ")

            if Option=="A" or Option=="a":
                print("Café")
            elif Option=="B" or Option=="b":
                print("Chocoloate")
            elif Option=="C" or Option=="c":
                print("Maca")
            elif Option=="D" or Option=="d":
                print("Quinua")
            elif Option=="E" or Option=="e":
                print("Refresco")
                print("volver al inicio")
                break
            else:
                print("Opcion erronea")




