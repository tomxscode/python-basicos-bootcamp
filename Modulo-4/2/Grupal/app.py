from datetime import datetime

#Crear clases:
class Cliente():
  # idcliente, nombre, apellido, correo, fecha registro, __saldo (encapsulado)
  def __init__(self, idcliente, nombre, apellido, correo, fecha_registro, saldo, convenio = "Sin convenio"):
    self.idcliente = idcliente
    self.nombre = nombre
    self.apellido = apellido
    self.correo = correo
    self.fecha_registro = fecha_registro
    self.convenio = convenio
    self.__saldo = saldo
    
  def obtener_saldo(self):
    return self.__saldo
  
  def depositar_saldo(self, monto):
    self.__saldo += monto
    return self.__saldo
  
  def cambiar_producto(self, producto_entrante, producto_saliente):
    valor_entrante = producto_entrante.valor_neto
    valor_saliente = producto_saliente.valor_neto
    if valor_entrante < valor_saliente:
      diferencia = valor_saliente - valor_entrante
      if self.obtener_saldo() < diferencia:
        return "Saldo insuficiente"
      else:
        self.depositar_saldo(-diferencia)
    producto_entrante.stock += 1
    producto_saliente.stock -= 1
    return "Producto cambiado con éxito"
  
  def devolver(self, producto_devuelto, buen_estado=True):
    if buen_estado:
      producto_devuelto.stock += 1
      self.depositar_saldo(producto_devuelto.valor_neto)
      return "Devolución exitosa"
    else:
      return "No se puede devolver un artículo en mal estado"
    
class Producto():
  # sku, nombre, categoria, proveedor, stock, valor_neto, __impuesto = 1.19 (encapsulado)
  def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto = 1.19, descuento = 0):
    self.sku = sku
    self.nombre = nombre
    self.categoria = categoria
    self.proveedor = proveedor
    self.stock = stock
    self.valor_neto = valor_neto
    self.descuento = descuento
    self.__impuesto = impuesto
    
class Vendedor():
  # run, nombre, apellido, seccion, __comision = 0
  def __init__(self, run, nombre, apellido, seccion, comision = 0, turno_noche = False):
    self.run = run
    self.nombre = nombre
    self.apellido = apellido
    self.seccion = seccion
    self.__comision = comision
    self.turno_noche = turno_noche
  
  def vender(self, producto, cliente):
    # Calcular si cliente tiene saldo
    if not cliente.obtener_saldo() >= producto.valor_neto:
      return "Saldo insuficiente"
    # Ver si hay existencias del producto
    if producto.stock <= 0:
      return "No hay existencias"
    
    producto.stock -= 1
    comision = producto.valor_neto * 0.005
    self.__comision += comision
    cliente.depositar_saldo(-producto.valor_neto)
    return "Venta exitosa"
    
  def canje_comision(self, vendedor, producto):
    if not isinstance(vendedor, Vendedor):
      return "No es un vendedor"
    # Al comprar con comisión se rebaja a un 40%
    valor_producto = producto.valor_neto * 0.6
    if vendedor.__comision >= valor_producto:
      vendedor.__comision -= valor_producto
      self.__comision -= valor_producto
      producto.stock -= 1
      return "Canje exitoso"
    else:
      return "No se puede canjear"
    
class Proveedor():
  # rut, nombre legal, razon social, pais, tipo_persona
  def __init__(self, rut, nombre_legal, razon_social, pais, tipo_persona):
    self.rut = rut
    self.nombre_legal = nombre_legal
    self.razon_social = razon_social
    self.pais = pais
    self.tipo_persona = tipo_persona
    
  def proveer(self, producto, stock_a_proveer):
    if not producto.proveedor == self:
      return "Producto no proveido por este proveedor"
    
    producto.stock += stock_a_proveer
    return "Stock exitosamente agregado"
    
proveedor1 = Proveedor(1, "Adidas", "Adidas SpA", "Chile", "Juridica")
proveedor2 = Proveedor(2, "Nike", "Nike Ltda", "Chile", "Juridica")
proveedor3 = Proveedor(3, "Puma", "Puma S.A", "Chile", "Juridica")
proveedor4 = Proveedor(4, "Matías Alveal", "Importaciones Alveal EIRL", "Chile", "Natural")
    
# crear 5 productos
producto1 = Producto(1, "Zapatillas", "Deportivas", proveedor1, 10, 15000)
producto2 = Producto(2, "Poleras", "Deportivas", proveedor2, 5, 10000)
producto3 = Producto(3, "Zapatos", "Deportivos", proveedor1, 8, 20000)
producto4 = Producto(4, "Poleron", "Deportivos", proveedor4, 3, 5000)
producto5 = Producto(5, "Chaquetas", "Deportivas", proveedor3, 7, 30000)

# crear 5 vendedores
vendedor1 = Vendedor(1, "Juan", "Perez", "Ventas")
vendedor2 = Vendedor(2, "Maria", "Gomez", "Ventas")
vendedor3 = Vendedor(3, "Pedro", "Rodriguez", "Ventas")
vendedor4 = Vendedor(4, "Ana", "Martinez", "Ventas")
vendedor5 = Vendedor(5, "Luis", "Gonzalez", "Ventas")

# crear 5 clientes
cliente1 = Cliente(1, "Juan", "Perez", "XXXXXXXXXXXXXX", datetime.now(), 5000)
cliente2 = Cliente(2, "Maria", "Gomez", "XXXXXXXXXXXXXX", datetime.now(), 10000)
cliente3 = Cliente(3, "Pedro", "Rodriguez", "XXXXXXXXXXXXXX", datetime.now(), 15000)
cliente4 = Cliente(4, "Ana", "Martinez", "XXXXXXXXXXXXXX", datetime.now(), 20000)
cliente5 = Cliente(5, "Luis", "Gonzalez", "XXXXXXXXXXXXXX", datetime.now(), 25000)

# Bodega virtual de productos
def bodega_virtual():
    return {
        1: {"nombre": "ZAPATILLAS", "cantidad": 20},
        2: {"nombre": "POLERAS", "cantidad": 10},
        3: {"nombre": "ZAPATOS", "cantidad": 15},
        4: {"nombre": "POLERÓN", "cantidad": 3},
        5: {"nombre": "CHAQUETA", "cantidad": 5},
        6: {"nombre": "GUANTES", "cantidad": 4}
    }

# Actualizar productos en bodega
def almacenar_stock(bodega, id_producto, cantidad):
    # Buscar producto por ID
    producto = bodega.get(id_producto)
    if producto:
        # Actualizar cantidad
        producto["cantidad"] += cantidad
    else:
        print("Producto no existe")

# Actualizar stock de un producto en bodega
def actualizar_stock(bodega, id_producto, cantidad):
    if id_producto in bodega:
        bodega[id_producto]["cantidad"] = cantidad
    else:
        print("Producto no existe")
    return bodega
        
# Productos y cantidades disponibles en bodega      
def unidades_disponibles(bodega):
    return {producto["nombre"]: producto["cantidad"] for producto in bodega.values()}
        
# Stock disponeble de un producto
def stock_disponible_producto(bodega, id_producto):
    if id_producto in bodega:
        return bodega[id_producto]["cantidad"]
    else: 
        return 0

# Productos y cantidades disponibles mayor a especificada a petición usuario 
def producto_unidad_usuario(bodega, cantidad):
    return [producto["nombre"] for producto in bodega.values() if producto["cantidad"] > cantidad]

# Ingresar usuarios
def ingresar_usuario(diccionario_clientes):
    nombre = input("Ingresa el nombre del cliente: ")
    apellido = input("Ingresa el apellido del cliente: ")
    correo = input("Ingresa el correo del cliente: ")
    # fecha de registro = hoy
    fecha_registro = datetime.now().strftime("%d/%m/%Y")
    id_cliente = max(diccionario_clientes.keys()) + 1 if diccionario_clientes else 1
    nuevo_cliente = Cliente(id_cliente, nombre, apellido, correo, fecha_registro, 0)
    diccionario_clientes[id_cliente] = nuevo_cliente
    return id_cliente
  
# listar usuarios
def listar_usuarios(diccionario_clientes):
    return [f"{cliente.idcliente} - {cliente.nombre} {cliente.apellido} - {cliente.correo} - {cliente.fecha_registro}" for cliente in diccionario_clientes.values()]

# Clientes registrados
def clientes_registrados(clientes):
    return len(clientes)

# Solicitud de compra
def solicitar_compra(id_cliente, id_producto, cantidad=1, bodega=None, diccionario_clientes=None):
    if not bodega:
        return "Bodega no especificada"
    
    # Comprobar que el producto exista
    if id_producto not in bodega:
        return "Producto no existe"
    
    # Comprobar que diccionario_clientes no sea none
    if not diccionario_clientes:
        return "Diccionario de clientes no especificado"
    
    if id_cliente not in diccionario_clientes:
        return "Usuario no registrado"
    
    stock_disponible = bodega[id_producto]["cantidad"]
    
    if stock_disponible >= cantidad:
        bodega[id_producto]["cantidad"] -= cantidad
        return "Compra aprobada y en camino 🛻"
    else:
        return "No hay suficiente stock, compra cancelada 😔"

# Menu opciones a usuario      
def menu():
    print("1. Ver unidades totales disponibles 📈")
    print("2. Ver unidades disponibles de un producto en particular 🔍")
    print("3. Ver productos con más de un número de unidades en stock 📦")
    print("4. Ingresar usuario 🧑")
    print("5. Mostrar cantidad de usuarios registrados en la tienda 👪")
    print("6. Solicitar compra 🏪")
    print("7. Listar usuarios")
    print("8. Salir")
    opcion = int(input("Selecciona una opción 🙂: "))
    return opcion

def comprobar_existencia_producto(id_producto):
    if id_producto in bodega:
        return True
    else:
        return False

# Crea bodega
bodega = bodega_virtual()
# Clientes registrados
clientes = {}

# Obtener opciones del menú seleccionadas por usuario
while True:
    opcion = menu()
    
    if opcion == 1:
        print("Unidades disponibles para cada producto: ", unidades_disponibles(bodega))
    elif opcion == 2:
        id_producto = int(input("Ingresa el ID del producto: "))
        # Comprobar que el producto exista
        if comprobar_existencia_producto(id_producto):
            print("Unidades disponibles del producto", id_producto, ":", bodega[id_producto]["cantidad"])
        else:
            print("Producto no existe")
    elif opcion == 3:
        cantidad = int(input("Ingresa el número de unidades solicitadas: "))
        productos_sobre_cantidad = producto_unidad_usuario(bodega, cantidad)
        if productos_sobre_cantidad:
            print("Productos con más de", cantidad, "unidades:", productos_sobre_cantidad)
        else:
            print("No hay productos con más de ", cantidad, " unidades disponibles")
    elif opcion == 4:
        nuevo_cliente_id = ingresar_usuario(clientes)
        print("Usuario registrado con ID: ", nuevo_cliente_id)
    elif opcion == 5:
        print("Total usuarios registrados: ", len(clientes))
    elif opcion == 6:
        id_cliente = int(input("Ingresa el ID del usuario: "))
        id_producto = int(input("Ingresa el ID del producto: "))
        cantidad = int(input("Ingresa la cantidad a comprar: "))
        if id_cliente in clientes:
            print(solicitar_compra(id_cliente, id_producto, cantidad, bodega, clientes))
        else:
            print("Cliente no existe")
    elif opcion == 7:
      # Listar usuarios
      print("Lista de usuarios registrados:")
      for usuario in listar_usuarios(clientes):
        print(usuario)
    elif opcion == 8:
        break
    else:
        print("Opción inválida. Elige una opción disponible en el menú.")