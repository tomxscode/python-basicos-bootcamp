def leer_archivo(nombre_archivo):
  with open(nombre_archivo) as archivo:
    return [i for i in archivo.read().split("\n")]

lista = leer_archivo('nombres.txt')
print("Datos en el archivo:" + str(lista))

lista_numeros = leer_archivo('numeros.txt')
print("Archivo 2 (numeros.txt)")
for numero in lista_numeros:
  print(int(numero))