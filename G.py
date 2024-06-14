from flask import Flask

# Crea una instancia de la clase Flask para la aplicación web.
app = Flask(__name__)

# Define una ruta para la URL raíz ('/') de la aplicación.
@app.route('/')
def home():
    # Devuelve una respuesta simple cuando se accede a la URL raíz.
    return "¿Qué onda?"

def main():
    # Imprime un mensaje indicando que el módulo G se está ejecutando.
    print("Se está ejecutando el módulo G")
    # Ejecuta la aplicación Flask en el servidor local.
    app.run()

# Verifica si el archivo se está ejecutando como el programa principal.
if __name__ == "__main__":
    # Llama a la función main para iniciar la aplicación.
    main()
