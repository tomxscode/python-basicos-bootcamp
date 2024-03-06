def validar_password(password):
  if len(password) < 8:
    return False
  
  tiene_minuscula = False
  tiene_mayuscula = False
  tiene_digito = False
  
  for char in password:
    if char.islower():
      tiene_minuscula = True
    elif char.isupper():
      tiene_mayuscula = True
    elif char.isdigit():
      tiene_digito = True
  
  return tiene_minuscula and tiene_mayuscula and tiene_digito

# Ejemplo de uso:
contrasena = input("Ingrese su contraseña: ")

if validar_password(contrasena):
  print("La contraseña es válida.")
else:
  print("La contraseña no cumple con los criterios necesarios.")
