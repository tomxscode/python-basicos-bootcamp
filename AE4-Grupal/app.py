import random, time
productos = [120, 150]
stock_total = productos[0] + productos[1]
proveedores = [150, 150]
contador = 0
contador_proveedores = [0, 0]

while stock_total != 0:
  if contador % 10 == 0:
    print(f"Stock disponible por producto: (1) {productos[0]} unidades, (2) {productos[1]} unidades")
  compras = [random.randint(1, 10), random.randint(1, 10)]
  for i in range(len(compras)):
    # Proveedores
    if productos[i] < 100:
      if proveedores[i] >= 50:
        proveedores[i] -= 50
        productos[i] += 50
        print(f"Se enviaron 50 unidades más al proveedor del producto {i}")
      elif proveedores[i] < 50 and proveedores[i] > 0:
        productos[i] += proveedores[i]
        proveedores[i] = 0
        print(f"El proveedor del producto {i} no tiene más stock y se rellenó con lo restante")
      else:
        if contador_proveedores[i] == 0:
          contador_proveedores[i] = 1
          print(f"El proveedor del producto {i} no tiene más stock")
    if compras[i] > productos[i] and productos[i] != 0:
      compras[i] = productos[i]
    elif productos[i] == 0:
      compras[i] = 0
    productos[i] -= compras[i]
  contador += 1
  stock_total = productos[0] + productos[1]
  time.sleep(3)  