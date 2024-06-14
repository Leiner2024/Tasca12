# Clase base Animal
class Animal:
    def __init__(self, nombre, edad):
        # Inicializa las propiedades nombre y edad
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        # Método genérico para el sonido de un animal
        return "Hace algún Sonido"
    
    def edad(self):
        # Método genérico para la edad de un animal
        return "Alguna Edad"

# Clase Perro que hereda de Animal
class Perro(Animal):
    def sonido(self):
        # Método específico para el sonido de un perro
        return "Guau"

# Clase Gato que hereda de Animal
class Gato(Animal):
    def sonido(self):
        # Método específico para el sonido de un gato
        return "Miau Miau"

# Función principal
def main():
    # Mensaje indicando que el módulo se está ejecutando
    print("Se está ejecutando el módulo E.")
    # Lista de objetos Perro y Gato
    l = [Perro("Firulais", 1), Gato("Garfield", 2)]
    # Itera sobre la lista de animales y muestra sus detalles
    for e in l:
        print("{} tiene {} años y dice {}".format(e.nombre, e.edad, e.sonido()))

# Llama a la función principal
main()
