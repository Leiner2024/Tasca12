!Hola! Soy Leiner
Este es mi proyecto de AO. Lo primero que te recomiendo que hagas para que funcione todo correctamente
es descargar todo obviamente, usar VS Code, luego dirigirte hacia el programa llamado "D_JuegoMemoria", buscarás adentro del código las siguientes lineas:

########################
IMAGEN_OCULTA = pygame.image.load("PNGs_JuegoMemoria/oculta.png")
########################


########################
# Sonidos
SONIDO_FONDO = pygame.mixer.Sound("WAVs_JuegoMemoria/fondo.wav")
SONIDO_CLIC = pygame.mixer.Sound("WAVs_JuegoMemoria/clic.wav")
SONIDO_EXITO = pygame.mixer.Sound("WAVs_JuegoMemoria/ganador.wav")
SONIDO_FRACASO = pygame.mixer.Sound("WAVs_JuegoMemoria/equivocado.wav")
SONIDO_VOLTEAR = pygame.mixer.Sound("WAVs_JuegoMemoria/voltear.wav")
########################

########################
cuadros = [Cuadro(f"PNGs_JuegoMemoria/{imagen}.png") for imagen in imagenes for _ in range(2)]
########################


Luego procederas a modificar las rutas según en donde hayas descargado los ".WAV" y los ".PNG" y Listo.
