# utilizando los conocimentos de programacion
# definimos el "while"
from argparse import OPTIONAL
from optparse import Option, OptionGroup
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

        while True:              # Mientras que se verdadero imprimira el siguiente menu
            print("BEBIDAS")
            print("A| café")
            print("B| chocolate")
            print("C| maca")
            print("D| quinua")
            print("E| refresco")
            print("F| REGRESAR")

            OptionGroup==input("SELECIONE SU BEBIDA [A..f]: ")
            if OptionGroup=="A" or OptionGroup=="a":
                print("Café")
            elif OptionGroup=="B" or OptionGroup=="b":
                print("Chocoloate")
            elif OptionGroup=="C" or OptionGroup=="c":
                print("Maca")
            elif OptionGroup=="D" or OptionGroup=="d":
                print("Quinua")
            elif OptionGroup=="E" or OptionGroup=="e":
                print("Refresco") 
            elif OptionGroup=="F" or OptionGroup=="f":
                print("Volvemos al menu")
                break
            else:
                print("Opcion erronea")



            




