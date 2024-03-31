# Definición de variables
cantidad_notas = 11
n = int(input("Ingrese la cantidad de datos a ordenar: "))
vector = []
nombre = []

# Solicitar y guardar los datos y nombres en las listas
for b in range(1, n+1):
    matematica = float(input("Ingrese la nota de Matematica: "))
    castellano = float(input("Ingrese la nota de Castellano: "))
    geografia = float(input("Ingrese la nota de Geografia: "))
    historia = float(input("Ingrese la nota de Historia: "))
    ecivica = float(input("Ingrese la nota de Educacion Civica: "))
    efisica = float(input("Ingrese la nota de Educacion Fisica: "))
    taller = float(input("Ingrese la nota de Taller: "))
    fisica = float(input("Ingrese la nota de Fisica: "))
    quimica = float(input("Ingrese la nota de Quimica: "))
    ingles = float(input("Ingrese la nota de Ingles: "))
    dibujo = float(input("Ingrese la nota de Dibujo: "))
    
    promedio = (matematica + castellano + geografia + historia + ecivica + efisica + taller + fisica + quimica + ingles + dibujo) / cantidad_notas
    vector.append(promedio)
    nombre.append(input("Ingrese el nombre: "))

# Ordenamiento de burbuja
for x in range(0, n-1):
    for a in range(0, n-x-1):
        if vector[a] > vector[a+1]:
            # Intercambiar valores numéricos
            aux_num = vector[a]
            vector[a] = vector[a+1]
            vector[a+1] = aux_num
            
            # Intercambiar nombres correspondientes
            aux_nom = nombre[a]
            nombre[a] = nombre[a+1]
            nombre[a+1] = aux_nom

# Mostrar los datos ordenados
print("Datos ordenados:")
for c in range(0, n):
    print("Número:", vector[c], " Nombre:", nombre[c])
