import random
# La primera funció a desenvolupar ha de permetre treballar amb llistes,
# números aleatoris.
def main():
    print("Se está ejecutando el módulo B")
    # Aquí coloca el código que deseas ejecutar en el módulo B

    print("Hola, bienvenido al Creador de Lista Aleatoria")

    def crear_lista_aleatoria(longitud, minimo, maximo):
        lista = [random.randint(minimo, maximo) for i in range(longitud)]
        return lista

    # PP
    lista_pred = [2, 7, 14]
    # Aca definimos la longitud, el minimo y el maximo, 
    # a esto lo llamamos "lista_aleatoria".
    lista_aleatoria = crear_lista_aleatoria(4, 1, 100)

    # Imprimimos las Listas
    print("Lista aleatoria: ", lista_aleatoria)
    print("Lista Predeterminada: ", lista_pred)

"""
def ListasYNumerosAleatorios():
    print("hola")

    
    for i in range(3):
        Numero = int(input("Numero a insertar en la Lista: "))
        ListaUsuario.append(Numero)

ListaUsuario = []
ListaPred = [2,5,7]

ListasYNumerosAleatorios()

print("Lista de usuario: ", ListaUsuario)
print("Lista predeterminada: ", ListaPred)
"""