# Crear una matriz vacía de tamaño 3x4
matriz = []

# Pedir al usuario que ingrese los elementos numéricos uno por uno
for i in range(3):  # Para cada fila (3 filas en total)
    fila = []  # Crear una fila vacía
    for j in range(4):  # Para cada columna (4 columnas en total)
        elemento = int(input(f"Ingrese el elemento en la posición [{i}][{j}]: "))  # Solicitar al usuario que ingrese un elemento
        fila.append(elemento)  # Agregar el elemento a la fila
    matriz.append(fila)  # Agregar la fila a la matriz

# Mostrar la matriz ordenadamente
print("Matriz:")
for fila in matriz:  # Para cada fila en la matriz
    for elemento in fila:  # Para cada elemento en la fila
        print(elemento, end=" ")  # Mostrar el elemento seguido de un espacio
    print()  # Salto de línea para pasar a la siguiente fila
