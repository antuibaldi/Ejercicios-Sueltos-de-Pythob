import random

numero_aletorio= random.randint(0,20)

sumador=0

while sumador<3:
    pedir_numero=int(input("Dame un numero: "))
    if pedir_numero==numero_aletorio:
        print("GANASTE")
        sumador==3
    else:
        sumador=sumador+1
        if sumador==3:
            print("PERDISTE")