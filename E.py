class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        return "Hace algún Sonido"
    def edad(self):
        return "Alguna Edad"

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau Miau"

def main():
    l=[Perro("Firulais", 1), Gato("Garfield", 2)]
    for e in l:
        print("{} tiene {} años y dice {}".format(e.nombre, e.edad, e.sonido()))
main()