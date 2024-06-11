from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¿Qué onda?"

def main():
    print("Se está ejecutando el módulo G")
    app.run()

if __name__ == "__main__":
    main()