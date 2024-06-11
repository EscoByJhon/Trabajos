# Inicializar el número de asiento
numero_asiento = 1

# Crear una lista vacía que representará el autobús
autobus = []

# Generar los números de asiento y agregarlos al autobús
for _ in range(10):  # 10 filas
    fila = []
    for _ in range(4):  # 4 asientos por fila
        fila.append(numero_asiento)
        numero_asiento += 1
    autobus.append(fila)

# Mostrar el autobús por pantalla
for fila in autobus:
    for asiento in fila:
        print(asiento, end=" ")
    print()  # Salto de línea después de cada fila
