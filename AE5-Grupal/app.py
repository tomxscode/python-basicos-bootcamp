import time

# Información de clientes: nombre, edad, identificador único con un diccionario
clientes = [
  {"nombre": "Juan", "edad": 25, "id": "1"},
  {"nombre": "Pedro", "edad": 30, "id": "2"},
  {"nombre": "María", "edad": 35, "id": "3"},
  {"nombre": "Ana", "edad": 40, "id": "4"},
  {"nombre": "Luis", "edad": 45, "id": "5"},
  {"nombre": "Carlos", "edad": 50, "id": "6"},
  {"nombre": "Sofía", "edad": 55, "id": "7"},
  {"nombre": "Miguel", "edad": 60, "id": "8"},
  {"nombre": "Jorge", "edad": 65, "id": "9"},
  {"nombre": "Laura", "edad": 70, "id": "10"}
]

# Información de productos: nombre, precio, identificador único y color con un diccionario
productos = [
  {"nombre": "Leche", "precio": 1.5, "id": 1, "color": "blanco"},
  {"nombre": "Pan", "precio": 2.0, "id": 2, "color": "negro"},
  {"nombre": "Queso", "precio": 3.0, "id": 3, "color": "rojo"},
  {"nombre": "Fideos", "precio": 4.0, "id": 4, "color": "verde"},
  {"nombre": "Aceite", "precio": 5.0, "id": 5, "color": "azul"}
]

while True:
  print("1. Agregar Cliente")
  print("2. Agregar Producto")
  print("3. Mostrar Clientes")
  print("4. Mostrar Productos")
  print("5. Eliminar Cliente")
  print("6. Eliminar Producto")
  print("7. Salir")
  opcion = input("Ingrese una opción: ")

  if opcion == "1":
    nombre = input("Ingrese el nombre del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))
    id = input("Ingrese el ID del cliente: ")
    clientes.append({"nombre": nombre, "edad": edad, "id": id})
    print("Cliente agregado exitosamente.")
  elif opcion == "2":
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    id = int(input("Ingrese el ID del producto: "))
    color = input("Ingrese el color del producto: ")
    productos.append({"nombre": nombre, "precio": precio, "id": id, "color": color})
    print("Producto agregado exitosamente.")
  elif opcion == "3":
    print("Listado de clientes:")
    for cliente in clientes:
      print(f"Nombre: {cliente['nombre']}, Edad: {cliente['edad']}, ID: {cliente['id']}")
      time.sleep(2)
    print(f"Cantidad de clientes: {len(clientes)}")
  elif opcion == "4":
    print("Listado de productos:")
    for producto in productos:
      print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']},  ID:{producto['id']}, Color: {producto['color']}")
      time.sleep(2)
    print(f"Cantidad de productos: {len(productos)}")
  elif opcion == "5":
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")
    # Preguntar si el id_cliente está en el listado de clientes
    if not id_cliente in [cliente["id"] for cliente in clientes]:
      print("ID de cliente no encontrado.")
      continue
    # Eliminar registro
    for cliente in clientes:
      if cliente["id"] == id_cliente:
        clientes.remove(cliente)
        print("Cliente eliminado exitosamente.")
        break
  elif opcion == "6":
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    # Preguntar si el id_producto está en el listado de productos
    if not id_producto in [producto["id"] for producto in productos]:
      print("ID de producto no encontrado.")
      continue
    # Eliminar registro
    for producto in productos:
      if producto["id"] == id_producto:
        productos.remove(producto)
        print("Producto eliminado exitosamente.")
        break
  elif opcion == "7":
    print("Adiós...")
    break
  else:
    print("Opción inválida.")
    
for cliente in clientes:
  print(cliente["id"])
  # Agregar "_piloto" al final de cada ID
  cliente["id"] += "_piloto"
  
# Imprimir los nuevos ID
for cliente in clientes:
  print(cliente["id"])
  
# Eliminar los ultimos 4
clientes = clientes[:-4]
print(clientes)