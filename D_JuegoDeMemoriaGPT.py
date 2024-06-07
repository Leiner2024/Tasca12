import pygame
import sys
import math
import time
import random

# Empezar Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Variables y configuraciones
ALTURA_BOTON = 45
MEDIDA_CUADRO = 180
IMAGEN_OCULTA = pygame.image.load("/home/leiner/Documentos/VS Personal/Tasca12-main/PNGs_JuegoMemoria/oculta.png")
SEGUNDOS_MOSTRAR_PIEZA = 1

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
        # Al crear un cuadro, se muestra y no está descubierto
        self.mostrar = True
        self.descubierto = False
        self.fuente_imagen = fuente_imagen
        self.imagen_real = pygame.image.load(fuente_imagen)

# Funciones del juego
def ocultar_todos_los_cuadros(cuadros):
    # Oculta todos los cuadros
    for fila in cuadros:
        for cuadro in fila:
            cuadro.mostrar = False
            cuadro.descubierto = False

def aleatorizar_cuadros(cuadros):
    # Mezcla los cuadros al azar
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
    # Verifica si todos los cuadros están descubiertos
    return all(cuadro.descubierto for fila in cuadros for cuadro in fila)

def reiniciar_juego():
    # Reinicia el juego
    global juego_iniciado
    juego_iniciado = False

def iniciar_juego(cuadros):
    # Inicia el juego, mezclando y ocultando los cuadros
    pygame.mixer.Sound.play(SONIDO_CLIC)
    for _ in range(3):
        aleatorizar_cuadros(cuadros)
    ocultar_todos_los_cuadros(cuadros)
    return True

# Función principal
def main():
    print("Se está ejecutando el módulo D, Juego de Memoria")

    # Tamaño de la pantalla y configuración del botón
    anchura_pantalla = 745
    altura_pantalla = 800
    anchura_boton = anchura_pantalla

    xFuente = int((anchura_boton / 2.2725) - (TAMANIO_FUENTE / 2))
    yFuente = int(altura_pantalla - ALTURA_BOTON + 10)

    # Configuración del botón
    boton = pygame.Rect(0, altura_pantalla - ALTURA_BOTON, anchura_boton, ALTURA_BOTON)

    # Variables del juego
    ultimos_segundos = None
    puede_jugar = True
    juego_iniciado = False
    x1 = y1 = x2 = y2 = None

    # Crear y mezclar los cuadros del juego
    imagenes = ["coco", "manzana", "limón", "naranja", "pera", "piña", "plátano", "sandía"]
    cuadros = [Cuadro(f"/home/leiner/Documentos/VS Personal/Tasca12-main/PNGs_JuegoMemoria/{imagen}.png") for imagen in imagenes for _ in range(2)]
    random.shuffle(cuadros)
    cuadros = [cuadros[i:i + 4] for i in range(0, len(cuadros), 4)]

    # Configuración de la pantalla del juego
    pantalla_juego = pygame.display.set_mode((anchura_pantalla, altura_pantalla))
    pygame.display.set_caption('Proyecto Python - Leiner X.')
    pygame.mixer.Sound.play(SONIDO_FONDO, -1)

    # Bucle principal del juego
    while True:
        # Manejo de eventos de Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and puede_jugar:  # Si se hace clic con el ratón y se puede jugar
                xAbsoluto, yAbsoluto = event.pos  # Obtener la posición del ratón
                if boton.collidepoint(event.pos):  # Si se hace clic en el botón
                    if not juego_iniciado:  # Si el juego no ha comenzado
                        juego_iniciado = iniciar_juego(cuadros)  # Iniciar el juego
                else:
                    if not juego_iniciado:  # Si el juego no ha comenzado
                        continue  # Saltar el resto del código y continuar con el siguiente evento
                    x = math.floor(xAbsoluto / MEDIDA_CUADRO)  # Calcular la posición en la cuadrícula (columna)
                    y = math.floor(yAbsoluto / MEDIDA_CUADRO)  # Calcular la posición en la cuadrícula (fila)
                    cuadro = cuadros[y][x]  # Obtener el cuadro en la posición clicada
                    if cuadro.mostrar or cuadro.descubierto:  # Si el cuadro ya está mostrando o descubierto
                        continue  # Saltar el resto del código y continuar con el siguiente evento
                    if x1 is None and y1 is None:  # Si no hay primer cuadro seleccionado
                        x1, y1 = x, y  # Guardar la posición del primer cuadro
                        cuadros[y1][x1].mostrar = True  # Mostrar el primer cuadro
                        pygame.mixer.Sound.play(SONIDO_VOLTEAR)  # Reproducir sonido de voltear
                    else:  # Si ya hay un primer cuadro seleccionado
                        x2, y2 = x, y  # Guardar la posición del segundo cuadro
                        cuadros[y2][x2].mostrar = True  # Mostrar el segundo cuadro
                        cuadro1 = cuadros[y1][x1]  # Obtener el primer cuadro
                        cuadro2 = cuadros[y2][x2]  # Obtener el segundo cuadro
                        if cuadro1.fuente_imagen == cuadro2.fuente_imagen:  # Si las imágenes coinciden
                            cuadro1.descubierto = cuadro2.descubierto = True  # Marcar ambos cuadros como descubiertos
                            x1 = x2 = y1 = y2 = None  # Resetear las posiciones seleccionadas
                            pygame.mixer.Sound.play(SONIDO_CLIC)  # Reproducir sonido de éxito
                        else:  # Si las imágenes no coinciden
                            pygame.mixer.Sound.play(SONIDO_FRACASO)  # Reproducir sonido de fracaso
                            ultimos_segundos = int(time.time())  # Guardar el tiempo del fallo
                            puede_jugar = False  # Bloquear el juego hasta ocultar los cuadros
                    if gana(cuadros):  # Comprobar si se ha ganado el juego
                        pygame.mixer.Sound.play(SONIDO_EXITO)  # Reproducir sonido de éxito
                        reiniciar_juego()  # Reiniciar el juego

        ahora = int(time.time())  # Obtener el tiempo actual
        if ultimos_segundos is not None and ahora - ultimos_segundos >= SEGUNDOS_MOSTRAR_PIEZA:
            # Si ha pasado el tiempo de mostrar las piezas incorrectas
            cuadros[y1][x1].mostrar = cuadros[y2][x2].mostrar = False  # Ocultar los cuadros
            x1 = y1 = x2 = y2 = None  # Resetear las posiciones seleccionadas
            ultimos_segundos = None  # Resetear el contador de tiempo
            puede_jugar = True  # Permitir jugar de nuevo

        # Dibujar la pantalla del juego
        pantalla_juego.fill(COLOR_BLANCO)  # Rellenar la pantalla con color blanco
        for y, fila in enumerate(cuadros):  # Recorrer las filas de cuadros
            for x, cuadro in enumerate(fila):  # Recorrer los cuadros en cada fila
                imagen = cuadro.imagen_real if cuadro.descubierto or cuadro.mostrar else IMAGEN_OCULTA
                # Elegir la imagen a mostrar (real o oculta)
                pantalla_juego.blit(imagen, (x * MEDIDA_CUADRO, y * MEDIDA_CUADRO))
                # Dibujar la imagen en la pantalla

        # Dibujar el botón
        color_boton = COLOR_AZUL if not juego_iniciado else COLOR_GRIS  # Elegir el color del botón
        texto_boton = FUENTE.render("Iniciar Juego" if not juego_iniciado else "Juego en Progreso", True, COLOR_BLANCO)
        # Elegir el texto del botón
        pygame.draw.rect(pantalla_juego, color_boton, boton)  # Dibujar el botón
        pantalla_juego.blit(texto_boton, (xFuente, yFuente))  # Dibujar el texto del botón

        pygame.display.update()  # Actualizar la pantalla para mostrar los cambios

if __name__ == "__main__":
    main()
