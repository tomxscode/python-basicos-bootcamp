import time

usuarios = []

# Validaciones
while True:
  print("\tIngrese una opción:\n\t1. Ingresar Usuarios\n\t2. Listar Usuarios\n\t0. Salir")
  opcion = input("Ingrese una opción: ")
  if not opcion.isdigit() or int(opcion) not in range(0, 3):
    print("Opción inválida. Por favor, ingrese una opción válida.")
    continue
  
  if opcion == "1":
    usuarios.append([])
    edad_valida = False

    nombre = input("Ingrese su nombre: ")
    password = input("Ingrese su contraseña: ")

    while not edad_valida:
      edad = input("Ingrese su edad: ")
      if edad.isdigit():
        edad_valida = True
      else:
        print("La edad ingresada no es válida.")
        edad_valida = False
    
    usuarios[-1].append(nombre)
    usuarios[-1].append(password)
    usuarios[-1].append(edad)
    print("Usuario agregado correctamente.")
        
  elif opcion == "2":
    print("-- Impresión de usuarios --")
    for usuario in usuarios:
      print(f"Nombre: {usuario[0]}\nContraseña: {usuario[1]}\nEdad: {usuario[2]}")
      time.sleep(5)
    print(f"Cantidad de usuarios {len(usuarios)}")
  elif opcion == "0":
    print("Saliendo del programa...")
    break