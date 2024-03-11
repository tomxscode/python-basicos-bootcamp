stock_producto = int(input("Ingrese el stock del producto: "))
print(f"Se registraron {stock_producto} unidades del producto")

# A la hora de hacer el pedido
productos_seleccionados = int(input("Ingrese la cantidad de productos seleccionados: "))
# Se comprueba que exista stock
if productos_seleccionados > stock_producto:
  print("No hay stock suficiente")
  exit()
elif productos_seleccionados > 20:
  print("No se pueden solicitar más de 20 unidades en un mismo pedido")
  exit()
else:
  print("La cantidad ingresada es válida.")

if productos_seleccionados > 12 and stock_producto >= (productos_seleccionados + 1):
  productos_seleccionados = productos_seleccionados + 1
  print("Se entregó una unidad extra del producto por compra mayorista")
print(f"Se entregaron {productos_seleccionados} unidades del producto")
# Se modifica la cantidad de productos
stock_producto = stock_producto - productos_seleccionados
# Se imprime el stock disponible
print(f"El stock disponible ahora es de {stock_producto} unidades")