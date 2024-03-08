def log(func):
  def wrapper(*args, **kwargs):
    resultado = func(*args, **kwargs)
    with open("logs.txt", "a") as a:
      a.write(f"Funcion {func.__name__} ejecutado con los argumentos {args} y {kwargs} | Resultado: {resultado}\n")
    return resultado
  return wrapper

@log
def suma(a, b):
  return a + b

print(suma(5, 6))