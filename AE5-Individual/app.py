usuario1 = {'nombre': 'Daniela', 'edad': 15, 'genero': 'femenino', 'direccion': 'calle falsa 123', 'telefono': '123456789'}
usuario2 = {'nombre': 'Juan', 'edad': 20, 'genero': 'masculino', 'direccion': 'calle verdadera 456', 'telefono': '987654321'}
usuario3 = {'nombre': 'Maria', 'edad': 25, 'genero': 'femenino', 'direccion': 'calle falsa 789', 'telefono': '555555555'}

junta_vecinos = [usuario1, usuario2, usuario3]

for usuario in junta_vecinos:
  print("Nombre: ", usuario['nombre'])
  print("Edad: ", usuario['edad'])
  print("Genero: ", usuario['genero'])
  print("Direccion: ", usuario['direccion'])
  print("Telefono: ", usuario['telefono'])
  
# manera ideal
class Usuario:
  def __init__(self, nombre, edad, genero, direccion, telefono):
    self.nombre = nombre
    self.edad = edad
    self.genero = genero
    self.direccion = direccion
    self.telefono = telefono
    
usuario1_objeto = Usuario('Daniela', 15, 'femenino', 'calle falsa 123', '123456789')