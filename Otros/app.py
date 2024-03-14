# Productos
productos = ["Clavo", "Pantalla", "Celular", "Teclado", "Mouse"]
precios = [400, 59000, 63000, 6000, 2000]
cantidades = []

subtotal = []

# Ingreso de cantidades por consola
longitud_lista = len(productos)
for i in range(longitud_lista):
  print("Ingrese la cantidad de " + productos[i] + " que desea comprar:")
  while True:
    try:
      cantidades.append(int(input()))
      break
    except ValueError:
      print("Por favor ingrese un número entero.")
  
  # Calculo de subtotal
  subtotal_auxiliar = cantidades[i] * precios[i]
  # Suma del IVA (19%)
  subtotal_auxiliar = subtotal_auxiliar * 1.19
  subtotal.append(subtotal_auxiliar)

# Devuelve factura + IVA
print("Factura:")
for i in range(longitud_lista):
  print(productos[i] + " x " + str(cantidades[i]) + " = $" + str(subtotal[i]) + " (incluye IVA)")