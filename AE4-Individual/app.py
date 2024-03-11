# GLOBALES
import random
cantidad_personas = 7
formularios_por_persona = 5

formularios = ["Hábitos alimenticios", "Experiencia laboral", "Actividades recreativas", "Atletismo", "Natación", "Deportes en general", "Empleabilidad"]

formularios_asignados = []

for p in range(cantidad_personas):
  formularios_asignados.append([])
  for f in range(formularios_por_persona):
    formulario = random.choice(formularios)
    while formulario in formularios_asignados:
      formulario = random.choice(formularios)
    formularios_asignados[p].append(formulario)
    
for p in range(cantidad_personas):
  print(f"Persona {p+1}: {formularios_asignados[p]}")