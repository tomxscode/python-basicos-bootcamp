class Alumno:
  def __init__(self, nombre, apellido, edad, asistencia, comuna):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.asistencia = asistencia
    self.comuna = comuna

  def __str__(self):
    return f"{self.nombre} {self.apellido} {self.edad} {self.asistencia} {self.comuna}"
  
# Crear lista de alumnos
alumnos = []
alumnos.append(Alumno("Juan", "Perez", 20, True, "Santiago"))
alumnos.append(Alumno("Maria", "Gomez", 19, False, "Los Ángeles"))
alumnos.append(Alumno("Pedro", "Rodriguez", 18, True, "Cabrero"))
alumnos.append(Alumno("Ana", "Martinez", 17, False, "Concepción"))

# Imprimir lista de alumnos
for alumno in alumnos:
  print(alumno)