import pygame
import sys
import math
import time
import random

# Inicialización de Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Variables y configuraciones
ALTURA_BOTON = 45
MEDIDA_CUADRO = 180
IMAGEN_OCULTA = pygame.image.load("/home/leiner/Documentos/VS Personal/Tasca12-main/PNGs_JuegoMemoria/oculta.png")
SEGUNDOS_MOSTRAR_PIEZA = 2

# Colores
COLOR_BLANCO = (231, 195, 196)
COLOR_GRIS = (242, 190, 87)
COLOR_AZUL = (157, 91, 42)

# Sonidos
SONIDO_FONDO = pygame.mixer.Sound("/home/leiner/Documentos/VS Personal/Tasca12-main/WAVs_JuegoMemoria/fondo.wav")
SONIDO_CLIC = pygame.mixer.Sound("/home/leiner/Documentos/VS Personal/Tasca12-main/WAVs_JuegoMemoria/clic.wav")
SONIDO_EXITO = pygame.mixer.Sound("/home/leiner/Documentos/VS Personal/Tasca12-main/WAVs_JuegoMemoria/ganador.wav")
SONIDO_FRACASO = pygame.mixer.Sound("/home/leiner/Documentos/VS Personal/Tasca12-main/WAVs_JuegoMemoria/equivocado.wav")
SONIDO_VOLTEAR = pygame.mixer.Sound("/home/leiner/Documentos/VS Personal/Tasca12-main/WAVs_JuegoMemoria/voltear.wav")

# Fuente para el botón
TAMANIO_FUENTE = 24
FUENTE = pygame.font.SysFont("Times New Roman", TAMANIO_FUENTE)

# Clase Cuadro
class Cuadro:
    def __init__(self, fuente_imagen):
        self.mostrar = True
        self.descubierto = False
        self.fuente_imagen = fuente_imagen
        self.imagen_real = pygame.image.load(fuente_imagen)

# Funciones del juego
def ocultar_todos_los_cuadros(cuadros):
    for fila in cuadros:
        for cuadro in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False

def aleatorizar_cuadros(cuadros):
    cantidad_filas = len(cuadros)
    cantidad_columnas = len(cuadros[0])
    for y in range(cantidad_filas):
        for x in range(cantidad_columnas):
            x_aleatorio = random.randint(0, cantidad_columnas - 1)
            y_aleatorio = random.randint(0, cantidad_filas - 1)
            cuadro_temporal = cuadros[y][x]
            cuadros[y][x] = cuadros[y_aleatorio][x_aleatorio]
            cuadros[y_aleatorio][x_aleatorio] = cuadro_temporal

def gana(cuadros):
    return all(cuadro.descubierto for fila in cuadros for cuadro in fila)

def reiniciar_juego():
    global juego_iniciado
    juego_iniciado = False

def iniciar_juego(cuadros):
    pygame.mixer.Sound.play(SONIDO_CLIC)
    for _ in range(3):
        aleatorizar_cuadros(cuadros)
    ocultar_todos_los_cuadros(cuadros)
    return True

# Función principal
def main():
    print("Se está ejecutando el módulo D, Juego de Memoria")

    # Ajustar tamaño de la pantalla
    anchura_pantalla = 745
    altura_pantalla = 800
    anchura_boton = anchura_pantalla

    xFuente = int((anchura_boton / 2.2725) - (TAMANIO_FUENTE / 2))
    yFuente = int(altura_pantalla - ALTURA_BOTON + 10)

    # Botón
    boton = pygame.Rect(0, altura_pantalla - ALTURA_BOTON, anchura_boton, ALTURA_BOTON)

    # Banderas
    ultimos_segundos = None
    puede_jugar = True
    juego_iniciado = False
    x1 = y1 = x2 = y2 = None

    # Inicializar cuadros del juego
    imagenes = ["coco", "manzana", "limón", "naranja", "pera", "piña", "plátano", "sandía"]
    cuadros = [Cuadro(f"/home/leiner/Documentos/VS Personal/Tasca12-main/PNGs_JuegoMemoria/{imagen}.png") for imagen in imagenes for _ in range(2)]
    random.shuffle(cuadros)
    cuadros = [cuadros[i:i + 4] for i in range(0, len(cuadros), 4)]

    # Iniciar pantalla
    pantalla_juego = pygame.display.set_mode((anchura_pantalla, altura_pantalla))
    pygame.display.set_caption('Proyecto Python - Leiner X.')
    pygame.mixer.Sound.play(SONIDO_FONDO, -1)

    # Ciclo del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar:
                xAbsoluto, yAbsoluto = event.pos
                if boton.collidepoint(event.pos):
                    if not juego_iniciado:
                        juego_iniciado = iniciar_juego(cuadros)
                else:
                    if not juego_iniciado:
                        continue
                    x = math.floor(xAbsoluto / MEDIDA_CUADRO)
                    y = math.floor(yAbsoluto / MEDIDA_CUADRO)
                    cuadro = cuadros[y][x]
                    if cuadro.mostrar or cuadro.descubierto:
                        continue
                    if x1 is None and y1 is None:
                        x1, y1 = x, y
                        cuadros[y1][x1].mostrar = True
                        pygame.mixer.Sound.play(SONIDO_VOLTEAR)
                    else:
                        x2, y2 = x, y
                        cuadros[y2][x2].mostrar = True
                        cuadro1 = cuadros[y1][x1]
                        cuadro2 = cuadros[y2][x2]
                        if cuadro1.fuente_imagen == cuadro2.fuente_imagen:
                            cuadro1.descubierto = cuadro2.descubierto = True
                            x1 = x2 = y1 = y2 = None
                            pygame.mixer.Sound.play(SONIDO_CLIC)
                        else:
                            pygame.mixer.Sound.play(SONIDO_FRACASO)
                            ultimos_segundos = int(time.time())
                            puede_jugar = False
                    if gana(cuadros):
                        pygame.mixer.Sound.play(SONIDO_EXITO)
                        reiniciar_juego()

        ahora = int(time.time())
        if ultimos_segundos is not None and ahora - ultimos_segundos >= SEGUNDOS_MOSTRAR_PIEZA:
            cuadros[y1][x1].mostrar = cuadros[y2][x2].mostrar = False
            x1 = y1 = x2 = y2 = None
            ultimos_segundos = None
            puede_jugar = True

        pantalla_juego.fill(COLOR_BLANCO)
        for y, fila in enumerate(cuadros):
            for x, cuadro in enumerate(fila):
                imagen = cuadro.imagen_real if cuadro.descubierto or cuadro.mostrar else IMAGEN_OCULTA
                pantalla_juego.blit(imagen, (x * MEDIDA_CUADRO, y * MEDIDA_CUADRO))

        color_boton = COLOR_AZUL if not juego_iniciado else COLOR_GRIS
        texto_boton = FUENTE.render("Iniciar Juego" if not juego_iniciado else "Juego en Progreso", True, COLOR_BLANCO)
        pygame.draw.rect(pantalla_juego, color_boton, boton)
        pantalla_juego.blit(texto_boton, (xFuente, yFuente))

        pygame.display.update()

if __name__ == "__main__":
    main()