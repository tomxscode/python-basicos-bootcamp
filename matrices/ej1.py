matriz = [[1, 2, 3], [-1,0,2]]

resultado = 0

for indice_interior in range(len(matriz[0])):
  resultado = resultado + (matriz[0][indice_interior] * matriz[1][indice_interior])
  print(f"Operando {matriz[0][indice_interior]} x {matriz[1][indice_interior]}")
  
print(f"El resultado es: {resultado}")