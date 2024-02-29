def leer_archivo(nombre_archivo):
  with open(nombre_archivo) as archivo:
    lista = archivo.readlines()
    lista = [l.strip() for l in lista]
  return lista

lista = leer_archivo('nombres.txt')
print("Datos en el archivo:" + str(lista))

lista_numeros = leer_archivo('numeros.txt')
print("Archivo 2 (numeros.txt)")
for numero in lista_numeros:
  print(int(numero))