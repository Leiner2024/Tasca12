import requests

# Diccionario con los datos a pedir.
parametres = {
    "access_key": "9d39e29bff4eb2841c644d72789c3bac",
    "symbols": "AAPL"
}
# Pedimos la URL de la Info y parámetros
res = requests.get("http://api.marketstack.com/v1/eod", params=parametres)
# 200 = página BIEN
# 404 = Error de la Página
# 505 = Error de Server
def main():
    print("Se está ejecutando el módulo F")
    if res.status_code == 200:
        # Convierte la Respuesta JSON a Diccionario.
        dades = res.json()
        # Se muestra los valores que me interesan.
        print("El cambio de:", dades["data"][0]["exchange"])
        print("Ha abierto a:", dades["data"][0]["open"], "€")
        print("Ha cerrado a:", dades["data"][0]["close"], "€")
        print("El precio más alto del día fue:", dades["data"][0]["high"], "€")
        print("El precio más bajo del día fue:", dades["data"][0]["low"], "€")
        print("Día:", dades["data"][0]["date"])
    else:
        # Si el código de estado no es 200, imprime un mensaje de error.
        print("No hay datos.")
