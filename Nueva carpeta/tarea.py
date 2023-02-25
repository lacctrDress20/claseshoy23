def es_multiplo(numero,multiplo):
    return numero%multiplo==0
i=int(input('Numero: '))
if es_multiplo(i, 5):
    print("Es multiplo de 5")
else:
    print("No es múltiplo de 5")


      