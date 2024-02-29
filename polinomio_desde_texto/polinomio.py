def calcular_polinomio(nombre_archivo, base):
  resultado = 0
  grado = 0
  with open(nombre_archivo, 'r') as archivo:
    for linea in archivo:
      valor = int(linea.strip())
      resultado += valor * (base ** grado)
      grado += 1
  return resultado

nombre_archivo = 'polinomio.txt'
base = 2