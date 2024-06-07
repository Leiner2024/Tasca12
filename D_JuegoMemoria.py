import pygame
import sys
import math
import time
import random

def main():
    print("Se está ejecutando el módulo D, Juego de Memoria")
    # Inicialización de Pygame
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    # Variables y configuraciones
    altura_boton = 45
    medida_cuadro = 180
    nombre_imagen_oculta = "PNGs_JuegoMemoria/oculta.png"
    imagen_oculta = pygame.image.load(nombre_imagen_oculta)
    segundos_mostrar_pieza = 1

    # Clase Cuadro
    class Cuadro:
        def __init__(self, fuente_imagen):
            self.mostrar = True
            self.descubierto = False
            self.fuente_imagen = fuente_imagen
            self.imagen_real = pygame.image.load(fuente_imagen)

    # Todo el juego; un arreglo de objetos Cuadro
    cuadros = [
        [Cuadro("PNGs_JuegoMemoria/coco.png"), Cuadro("PNGs_JuegoMemoria/coco.png"),
        Cuadro("PNGs_JuegoMemoria/manzana.png"), Cuadro("PNGs_JuegoMemoria/manzana.png")],
        [Cuadro("PNGs_JuegoMemoria/limón.png"), Cuadro("PNGs_JuegoMemoria/limón.png"),
        Cuadro("PNGs_JuegoMemoria/naranja.png"), Cuadro("PNGs_JuegoMemoria/naranja.png")],
        [Cuadro("PNGs_JuegoMemoria/pera.png"), Cuadro("PNGs_JuegoMemoria/pera.png"),
        Cuadro("PNGs_JuegoMemoria/piña.png"), Cuadro("PNGs_JuegoMemoria/piña.png")],
        [Cuadro("PNGs_JuegoMemoria/plátano.png"), Cuadro("PNGs_JuegoMemoria/plátano.png"),
        Cuadro("PNGs_JuegoMemoria/sandía.png"), Cuadro("PNGs_JuegoMemoria/sandía.png")],
    ]

    # Colores
    color_blanco = (231, 195, 196)
    color_gris = (242, 190, 87)
    color_azul = (157, 91, 42)

    # Sonidos
    sonido_fondo = pygame.mixer.Sound("WAVs_JuegoMemoria/fondo.wav")
    sonido_clic = pygame.mixer.Sound("WAVs_JuegoMemoria/clic.wav")
    sonido_exito = pygame.mixer.Sound("WAVs_JuegoMemoria/ganador.wav")
    sonido_fracaso = pygame.mixer.Sound("WAVs_JuegoMemoria/equivocado.wav")
    sonido_voltear = pygame.mixer.Sound("WAVs_JuegoMemoria/voltear.wav")

    # Ajustar tamaño de la pantalla
    anchura_pantalla = 750  # Nuevo ancho de pantalla
    altura_pantalla = 800  # Nuevo alto de pantalla
    anchura_boton = anchura_pantalla

    # Fuente para el botón
    tamanio_fuente = 24
    fuente = pygame.font.SysFont("Times New Roman", tamanio_fuente)
    xFuente = int((anchura_boton / 2.2725) - (tamanio_fuente / 2))
    yFuente = int(altura_pantalla - altura_boton + 10)

    # Botón
    boton = pygame.Rect(0, altura_pantalla - altura_boton, anchura_boton, altura_pantalla)

    # Banderas
    ultimos_segundos = None
    puede_jugar = True
    juego_iniciado = False
    x1 = None
    y1 = None
    x2 = None
    y2 = None

    # Funciones
    def ocultar_todos_los_cuadros():
        for fila in cuadros:
            for cuadro in fila:
                cuadro.mostrar = False
                cuadro.descubierto = False

    def aleatorizar_cuadros():
        cantidad_filas = len(cuadros)
        cantidad_columnas = len(cuadros[0])
        for y in range(cantidad_filas):
            for x in range(cantidad_columnas):
                x_aleatorio = random.randint(0, cantidad_columnas - 1)
                y_aleatorio = random.randint(0, cantidad_filas - 1)
                cuadro_temporal = cuadros[y][x]
                cuadros[y][x] = cuadros[y_aleatorio][x_aleatorio]
                cuadros[y_aleatorio][x_aleatorio] = cuadro_temporal

    def comprobar_si_gana():
        if gana():
            pygame.mixer.Sound.play(sonido_exito)
            reiniciar_juego()

    def gana():
        for fila in cuadros:
            for cuadro in fila:
                if not cuadro.descubierto:
                    return False
        return True

    def reiniciar_juego():
        global juego_iniciado
        juego_iniciado = False

    def iniciar_juego():
        pygame.mixer.Sound.play(sonido_clic)
        global juego_iniciado
        for i in range(3):
            aleatorizar_cuadros()
        ocultar_todos_los_cuadros()
        juego_iniciado = True

    # Iniciar pantalla
    pantalla_juego = pygame.display.set_mode((anchura_pantalla, altura_pantalla))
    pygame.display.set_caption('Proyecto Python - Leiner X.')
    pygame.mixer.Sound.play(sonido_fondo, -1)

    # Ciclo del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar:
                xAbsoluto, yAbsoluto = event.pos
                if boton.collidepoint(event.pos):
                    if not juego_iniciado:
                        iniciar_juego()
                else:
                    if not juego_iniciado:
                        continue
                    x = math.floor(xAbsoluto / medida_cuadro)
                    y = math.floor(yAbsoluto / medida_cuadro)
                    cuadro = cuadros[y][x]
                    if cuadro.mostrar or cuadro.descubierto:
                        continue
                    if x1 is None and y1 is None:
                        x1 = x
                        y1 = y
                        cuadros[y1][x1].mostrar = True
                        pygame.mixer.Sound.play(sonido_voltear)
                    else:
                        x2 = x
                        y2 = y
                        cuadros[y2][x2].mostrar = True
                        cuadro1 = cuadros[y1][x1]
                        cuadro2 = cuadros[y2][x2]
                        if cuadro1.fuente_imagen == cuadro2.fuente_imagen:
                            cuadros[y1][x1].descubierto = True
                            cuadros[y2][x2].descubierto = True
                            x1 = None
                            x2 = None
                            y1 = None
                            y2 = None
                            pygame.mixer.Sound.play(sonido_clic)
                        else:
                            pygame.mixer.Sound.play(sonido_fracaso)
                            ultimos_segundos = int(time.time())
                            puede_jugar = False
                    comprobar_si_gana()

        ahora = int(time.time())
        if ultimos_segundos is not None and ahora - ultimos_segundos >= segundos_mostrar_pieza:
            cuadros[y1][x1].mostrar = False
            cuadros[y2][x2].mostrar = False
            x1 = None
            y1 = None
            x2 = None
            y2 = None
            ultimos_segundos = None
            puede_jugar = True

        pantalla_juego.fill(color_blanco)
        x = 0
        y = 0
        for fila in cuadros:
            x = 0
            for cuadro in fila:
                if cuadro.descubierto or cuadro.mostrar:
                    pantalla_juego.blit(cuadro.imagen_real, (x, y))
                else:
                    pantalla_juego.blit(imagen_oculta, (x, y))
                x += medida_cuadro
            y += medida_cuadro

        if juego_iniciado:
            pygame.draw.rect(pantalla_juego, color_blanco, boton)
            pantalla_juego.blit(fuente.render("Iniciar Juego", True, color_gris), (xFuente, yFuente))
        else:
            pygame.draw.rect(pantalla_juego, color_azul, boton)
            pantalla_juego.blit(fuente.render("Iniciar Juego", True, color_blanco), (xFuente, yFuente))

        pygame.display.update()