matriz = [[[5, 2, 1], [2, 1, 2], [4, 1, 3]], [[1, 4, 2], [0, 3, 0], [2, 1, 3]]]

# Crear una lista para almacenar los resultados
resultados = []

producto = 0
producto_anterior = 0

# Iterar sobre las filas de la matriz
for i in range(len(matriz[0])):
    # Iterar sobre las columnas de la matriz
    for j in range(len(matriz[0][0])):
        # Inicializar el producto para cada par de elementos
        producto_anterior = resultados[-1] if resultados else 0
        producto = matriz[0][i][j] * matriz[1][i][j]
        total = producto_anterior + producto
        # Agregar el producto a la lista de resultados
        resultados.append(total)

print(resultados)