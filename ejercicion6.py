numero_uno = int(input("Dame un número: "))
numero_dos = int(input("Dame un número dos: "))

decision = input("Si es la opción 1 es suma, la opción 2 es resta: ")

if decision == "1":
    resultado = numero_uno + numero_dos
    print("Tu resultado es:", resultado)
elif decision == "2":
    resultado = numero_uno - numero_dos
    print("Tu resultado es:", resultado)
else:
    print("Opción no válida")
