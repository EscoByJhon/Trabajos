# Crear el arreglo manualmente
arreglo = [[[ 'amarillo', 'rojo', 'Naranja'],
             ['Verde', 'amarillo', 'Blanco'],
             ['Blanco', 'Naranja', 'Verde']],
            
            [[ 'Naranja', 'rojo', 'amarillo'],
             ['Blanco', 'Verde', 'rojo'],
             ['Verde', 'Blanco', 'amarillo']],
            
            [[ 'rojo', 'amarillo', 'Verde'],
             ['Naranja', 'Blanco', 'Naranja'],
             ['amarillo', 'Verde', 'rojo']]]

# Inicializar contadores
num_amarillo = 0
num_rojo = 0
num_naranja = 0
num_verde = 0
num_blanco = 0

# Recorrer el arreglo y contar la cantidad de cada color
for matriz in arreglo:
    for fila in matriz:
        for color in fila:
            if color == 'amarillo':
                num_amarillo += 1
            elif color == 'rojo':
                num_rojo += 1
            elif color == 'Naranja':
                num_naranja += 1
            elif color == 'Verde':
                num_verde += 1
            elif color == 'Blanco':
                num_blanco += 1

# Mostrar la información
print("Número de elementos 'amarillo':", num_amarillo)
print("Número de elementos 'rojo':", num_rojo)
print("Número de elementos 'Naranja':", num_naranja)
print("Número de elementos 'Verde':", num_verde)
print("Número de elementos 'Blanco':", num_blanco)

