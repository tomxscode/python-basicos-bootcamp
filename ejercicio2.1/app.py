usuarios = ["Tomas", "Daniela", "Johanna", "Alan", "Hugo", "Pepe", "Luis"]

usuario_ingresado = input("Ingrese su usuario: ")
while usuario_ingresado not in usuarios:
  usuario_ingresado = input("Error, vuelva a ingresar su usuario: ")
  
print("Bienvenidx " + usuario_ingresado)
print("En el sistema hay registrados " + str(len(usuarios)) + " usuarios")

print("Lista de usuarios:")
for usuario in usuarios:
  print("- " + usuario)