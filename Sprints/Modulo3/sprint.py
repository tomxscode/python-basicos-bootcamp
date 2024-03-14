import random
import re

def generar_contraseña():
    """Genera una contraseña aleatoria."""
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return ''.join(random.choice(caracteres) for _ in range(12))  # Aumenta la longitud de la contraseña

def validar_contraseña(contraseña):
    """Valida si una contraseña cumple con los criterios de tener al menos una letra minúscula, una letra mayúscula, un número y un carácter especial."""
    regex_minuscula = re.compile('[a-z]')
    regex_mayuscula = re.compile('[A-Z]')
    regex_numero = re.compile('[0-9]')
    regex_especial = re.compile('[!@#$%^&*()]')
    return bool(regex_minuscula.search(contraseña) and regex_mayuscula.search(contraseña) and regex_numero.search(contraseña) and regex_especial.search(contraseña))

def validar_telefono(telefono):
    """Valida si un número de teléfono tiene exactamente 8 dígitos."""
    return telefono.isdigit() and len(telefono) == 8

def validar_usuario(usuario, usuarios_existentes):
    """Valida si un nombre de usuario contiene solo caracteres alfanuméricos y guiones bajos y no está en uso previamente."""
    if usuario in usuarios_existentes:
        return False, "El nombre de usuario ya está en uso."
    if len(usuario) < 3 or len(usuario) > 20:  # Longitud mínima y máxima del nombre de usuario
        return False, "El nombre de usuario debe tener entre 3 y 20 caracteres."
    if not re.match("^[a-zA-Z0-9_]*$", usuario):
        return False, "El nombre de usuario solo puede contener letras, números y guiones bajos."
    return True, ""

def obtener_datos_usuario(usuario_tipo, usuarios_existentes):
    """Obtiene los datos del usuario (nombre de usuario y teléfono) de manera interactiva."""
    while True:
        nombre_usuario = input(f"Ingrese el nombre de usuario para {usuario_tipo}: ")
        valido, mensaje = validar_usuario(nombre_usuario, usuarios_existentes)
        if valido:
            break
        else:
            print(mensaje)
    telefono = input(f"Ingrese el número telefónico para {nombre_usuario}: ")
    while not validar_telefono(telefono):
        print("Número telefónico inválido. Debe contener exactamente 8 dígitos numéricos.")
        telefono = input("Ingrese el número telefónico válido: ")
    return nombre_usuario, telefono

def crear_cuentas(usuarios):
    """Crea cuentas de usuario para los tipos de usuario proporcionados."""
    cuentas = {}
    for usuario_tipo, cantidad in usuarios.items():
        usuarios_existentes = cuentas.keys()
        for _ in range(cantidad):
            nombre_usuario, telefono = obtener_datos_usuario(usuario_tipo, usuarios_existentes)
            contraseña = generar_contraseña()
            while not validar_contraseña(contraseña):
                contraseña = generar_contraseña()
            cuentas[nombre_usuario] = {"tipo": usuario_tipo, "contraseña": contraseña, "teléfono": telefono}
    return cuentas

def mostrar_cuentas(cuentas):
    """Muestra las cuentas de usuario creadas."""
    print("Cuentas creadas exitosamente:")
    for nombre_usuario, datos in cuentas.items():
        print(f"Tipo: {datos['tipo']}, Usuario: {nombre_usuario}, Contraseña: {datos['contraseña']}, Teléfono: {datos['teléfono']}")

def main():
    # Definir los tipos de usuarios y la cantidad deseada para cada uno
    usuarios = {
        "Funcionario": 4,
        "Paciente": 4,
        "Organización social": 2
    }

    # Crear las cuentas de usuario
    cuentas = crear_cuentas(usuarios)

    # Mostrar las cuentas creadas
    mostrar_cuentas(cuentas)

if __name__ == "__main__":
    main()