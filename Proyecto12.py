import random
import B
import C
import D_JuegoMemoria
import E
import F
import G

# Menú de opciones
def Menu():
    op = 0
    while op < 1 or op > 7:
        print("""
        Programa principal
        1. Listas con números aleatorios
        2. Fichero que se guarda auto.
        3. El Juego de la Memoria
        4. App de Clases y Herencias
        5. Scrapping de la Bolsa
        6. App para Servicios Web
        7. Salir
        """)
        op = int(input("Introduce una Opción: "))
        if op < 1 or op > 7:
            print("Opción no valida \n")
        else:
            return op

# Programa Principal
op = 1
while op != 7:
    op = Menu()
    match op:
        case 1:
            B.main()
            print("FIN del EX1😀")
        case 2:
            C.main()
            print("FIN del EX2😀")
        case 3:
            D_JuegoMemoria.main()
            print("FIN del EX3😀")
        case 4:
            E.main()
            print("FIN del EX4😀")
        case 5:
            F.main()
            print("FIN del EX5😀")
        case 6:
            G.main()
            print("FIN del EX6😀")
        case 7:
            print("Adiós, el Proyecto fue terminado.😀")
