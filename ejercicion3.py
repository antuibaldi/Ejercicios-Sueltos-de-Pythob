def oferta_partido():
    lista=["1 Gano","2 Perdio","3 Empato","4 Salir de programa"]

    print ("Elija opciones")
    print ("-------------------------------------------------------")

    for opncion in lista:
        print (opncion)

puntaje=0

oferta_partido()

gano_perdio_empato=int(input("Ingrese la opcion de 1 a 4: "))

while gano_perdio_empato < 4:
    if gano_perdio_empato==1:
        puntaje=puntaje+3
        print("GANO")
    elif gano_perdio_empato==2:
        puntaje=puntaje+1
        print("EMPATO")
    elif gano_perdio_empato==3:
        print("PERDIO")
    gano_perdio_empato=int(input("Ingrese la opcion de 1 a 4: "))

print ("El resultado es: "+(str(puntaje)))